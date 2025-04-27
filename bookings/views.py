from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import Booking, ScenicSpot, Room, Food, UserSharing, Announcement, UserProfile
from .forms import BookingForm, ScenicSpotForm, RoomForm, FoodForm, UserSharingForm, AnnouncementForm, UserProfileForm, \
    UserRegisterForm, PaymentForm
from datetime import datetime

from django.shortcuts import redirect

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                form.add_error(None, "您没有管理员权限")
    else:
        form = AdminLoginForm()
    return render(request, 'bookings/admin_login.html', {'form': form})

def admin_dashboard(request):
    return render(request, 'bookings/admin_dashboard.html')

def add_scenic_spot(request):
    if request.method == 'POST':
        form = ScenicSpotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = ScenicSpotForm()
    return render(request, 'bookings/add_scenic_spot.html', {'form': form})

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FoodForm()
    return render(request, 'bookings/add_food.html', {'form': form})

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = RoomForm()
    return render(request, 'bookings/add_room.html', {'form': form})

def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AnnouncementForm()
    return render(request, 'bookings/add_announcement.html', {'form': form})

def index(request):
    return render(request, 'bookings/index.html')


def scenic_spots(request):
    scenic_spots = ScenicSpot.objects.all()
    return render(request, 'bookings/scenic_spots.html', {'scenic_spots': scenic_spots})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'bookings/rooms.html', {'rooms': rooms})


def food(request):
    foods = Food.objects.all()
    return render(request, 'bookings/food.html', {'foods': foods})


def user_sharing(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = UserSharingForm(request.POST)
        if form.is_valid():
            sharing = form.save(commit=False)
            sharing.user = request.user
            sharing.save()
            messages.success(request, '分享内容已成功添加！')
            return redirect('user_sharing')
    else:
        form = UserSharingForm()

    user_sharings = UserSharing.objects.all().order_by('-created_at')
    return render(request, 'bookings/user_sharing.html', {'user_sharings': user_sharings, 'form': form})


def announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'bookings/announcements.html', {'announcements': announcements})


@login_required
def personal_center(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/personal_center.html', {'user': request.user,'bookings': bookings})


def admin_panel(request):
    return render(request, 'bookings/admin_panel.html')


def help_center(request):
    return render(request, 'bookings/help_center.html')


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.total_amount = calculate_total_amount(booking)
            booking.save()
            return redirect('payment', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    wechat_qr_url = "https://yourdomain.com/path_to_your_wechat_qr_code_image.jpg"  # 微信收款码图片的URL

    if request.method == 'POST':
        if 'payment_screenshot' in request.FILES:
            payment_screenshot = request.FILES['payment_screenshot']
            booking.payment_screenshot = payment_screenshot
            booking.payment_status = 'completed'
            booking.payment_date = datetime.now()
            booking.save()
            messages.success(request, '付款截图已上传，订单已完成。')
            return redirect('personal_center')

    return render(request, 'bookings/payment.html', {'booking': booking, 'wechat_qr_url': wechat_qr_url})


@login_required
def buy_scenic_spot(request, spot_id):
    scenic_spot = get_object_or_404(ScenicSpot, id=spot_id)
    if request.method == 'POST':
        booking = Booking(user=request.user, scenic_spot=scenic_spot, tour_date=datetime.now(),
                          total_amount=scenic_spot.price)
        booking.save()
        return redirect('payment', booking_id=booking.id)
    return render(request, 'bookings/buy_scenic_spot.html', {'scenic_spot': scenic_spot})


@login_required
def buy_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        booking = Booking(user=request.user, room=room, tour_date=datetime.now(), total_amount=room.price)
        booking.save()
        return redirect('payment', booking_id=booking.id)
    return render(request, 'bookings/buy_room.html', {'room': room})


@login_required
def buy_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        booking = Booking(user=request.user, food=food, tour_date=datetime.now(), total_amount=food.price)
        booking.save()
        return redirect('payment', booking_id=booking.id)
    return render(request, 'bookings/buy_food.html', {'food': food})

@login_required
def admin_dashboard(request):
    return render(request, 'bookings/admin_dashboard.html')

# 景区管理视图
@login_required
def view_scenic_spots(request):
    scenic_spots = ScenicSpot.objects.all()
    return render(request, 'bookings/view_scenic_spots.html', {'scenic_spots': scenic_spots})

@login_required
def add_scenic_spot(request):
    if request.method == 'POST':
        form = ScenicSpotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_scenic_spots')
    else:
        form = ScenicSpotForm()
    return render(request, 'bookings/add_scenic_spot.html', {'form': form})

@login_required
def edit_scenic_spot(request, pk):
    scenic_spot = get_object_or_404(ScenicSpot, pk=pk)
    if request.method == 'POST':
        form = ScenicSpotForm(request.POST, request.FILES, instance=scenic_spot)
        if form.is_valid():
            form.save()
            return redirect('view_scenic_spots')
    else:
        form = ScenicSpotForm(instance=scenic_spot)
    return render(request, 'bookings/edit_scenic_spot.html', {'form': form})

@login_required
def delete_scenic_spot(request, pk):
    scenic_spot = get_object_or_404(ScenicSpot, pk=pk)
    if request.method == 'POST':
        scenic_spot.delete()
        return redirect('view_scenic_spots')
    return render(request, 'bookings/delete_scenic_spot.html', {'scenic_spot': scenic_spot})

# 客房管理视图
@login_required
def view_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'bookings/view_rooms.html', {'rooms': rooms})

@login_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_rooms')
    else:
        form = RoomForm()
    return render(request, 'bookings/add_room.html', {'form': form})

@login_required
def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('view_rooms')
    else:
        form = RoomForm(instance=room)
    return render(request, 'bookings/edit_room.html', {'form': form})

@login_required
def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('view_rooms')
    return render(request, 'bookings/delete_room.html', {'room': room})

# 美食管理视图
@login_required
def view_foods(request):
    foods = Food.objects.all()
    return render(request, 'bookings/view_foods.html', {'foods': foods})

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_foods')
    else:
        form = FoodForm()
    return render(request, 'bookings/add_food.html', {'form': form})

@login_required
def edit_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('view_foods')
    else:
        form = FoodForm(instance=food)
    return render(request, 'bookings/edit_food.html', {'form': form})

@login_required
def delete_food(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('view_foods')
    return render(request, 'bookings/delete_food.html', {'food': food})

# 公告管理视图
@login_required
def view_announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'bookings/view_announcements.html', {'announcements': announcements})

@login_required
def add_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_announcements')
    else:
        form = AnnouncementForm()
    return render(request, 'bookings/add_announcement.html', {'form': form})

@login_required
def edit_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('view_announcements')
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'bookings/edit_announcement.html', {'form': form})

@login_required
def delete_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == 'POST':
        announcement.delete()
        return redirect('view_announcements')
    return render(request, 'bookings/delete_announcement.html', {'announcement': announcement})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'账户已创建，您现在可以登录了 {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def calculate_total_amount(booking):
    # 计算总金额的逻辑
    total_amount = 0
    if booking.scenic_spot:
        total_amount += booking.scenic_spot.price
    if booking.room:
        total_amount += booking.room.price
    if booking.food:
        total_amount += booking.food.price
    return total_amount



def custom_logout(request):
    logout(request)
    return redirect('index')  # 或者你可以设置为登出后的跳转页面