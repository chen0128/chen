from django.urls import path, include
from . import views
from .views import custom_logout

urlpatterns = [
    # 常规页面路由
    path('', views.index, name='index'),
    path('booking/', views.booking_list, name='booking_list'),
    path('booking/new/', views.booking_form, name='booking_form'),
    path('booking/payment/<int:booking_id>/', views.payment, name='payment'),
    path('buy_scenic_spot/<int:spot_id>/', views.buy_scenic_spot, name='buy_scenic_spot'),
    path('buy_room/<int:room_id>/', views.buy_room, name='buy_room'),
    path('buy_food/<int:food_id>/', views.buy_food, name='buy_food'),
    path('user_sharing/', views.user_sharing, name='user_sharing'),
    path('personal_center/', views.personal_center, name='personal_center'),

    # 登出路由（自定义登出视图） - 确保此路径优先
    path('logout/', custom_logout, name='logout'),

    # 管理员相关路由
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/view_scenic_spots/', views.view_scenic_spots, name='view_scenic_spots'),
    path('admin/add_scenic_spot/', views.add_scenic_spot, name='add_scenic_spot'),
    path('admin/edit_scenic_spot/<int:pk>/', views.edit_scenic_spot, name='edit_scenic_spot'),
    path('admin/delete_scenic_spot/<int:pk>/', views.delete_scenic_spot, name='delete_scenic_spot'),
    path('admin/view_rooms/', views.view_rooms, name='view_rooms'),
    path('admin/add_room/', views.add_room, name='add_room'),
    path('admin/edit_room/<int:pk>/', views.edit_room, name='edit_room'),
    path('admin/delete_room/<int:pk>/', views.delete_room, name='delete_room'),
    path('admin/view_foods/', views.view_foods, name='view_foods'),
    path('admin/add_food/', views.add_food, name='add_food'),
    path('admin/edit_food/<int:pk>/', views.edit_food, name='edit_food'),
    path('admin/delete_food/<int:pk>/', views.delete_food, name='delete_food'),
    path('admin/view_announcements/', views.view_announcements, name='view_announcements'),
    path('admin/add_announcement/', views.add_announcement, name='add_announcement'),
    path('admin/edit_announcement/<int:pk>/', views.edit_announcement, name='edit_announcement'),
    path('admin/delete_announcement/<int:pk>/', views.delete_announcement, name='delete_announcement'),

    # Django 默认认证路径（包含登录、密码重置等功能）
    path('accounts/', include('django.contrib.auth.urls')),  # 默认认证功能：登录、密码重置等
]
