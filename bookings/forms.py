from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm  # 导入 AuthenticationForm
from .models import Booking, ScenicSpot, Room, Food, UserSharing, Announcement, UserProfile

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['scenic_spot', 'tour_date']

class ScenicSpotForm(forms.ModelForm):
    class Meta:
        model = ScenicSpot
        fields = ['name', 'description', 'location', 'price', 'image']  # 添加价格字段

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'description', 'price','image']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'image']

class UserSharingForm(forms.ModelForm):
    class Meta:
        model = UserSharing
        fields = ['title', 'content']

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'birth_date', 'profile_picture']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='卡号', max_length=16)
    card_expiry = forms.CharField(label='到期日期', max_length=5)
    card_cvc = forms.CharField(label='CVC', max_length=3)