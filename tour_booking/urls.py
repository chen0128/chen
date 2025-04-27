from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from bookings import views as bookings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bookings_views.index, name='index'),  # 根路径指向首页视图
    path('scenic_spots/', bookings_views.scenic_spots, name='scenic_spots'),
    path('rooms/', bookings_views.rooms, name='rooms'),
    path('food/', bookings_views.food, name='food'),
    path('user_sharing/', bookings_views.user_sharing, name='user_sharing'),
    path('announcements/', bookings_views.announcements, name='announcements'),
    path('personal_center/', bookings_views.personal_center, name='personal_center'),
    path('admin_panel/', bookings_views.admin_panel, name='admin_panel'),
    path('help_center/', bookings_views.help_center, name='help_center'),
    path('bookings/', include('bookings.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('accounts/register/', bookings_views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)