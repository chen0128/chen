from django.contrib import admin
from .models import Booking, ScenicSpot, Room, Food, UserSharing, Announcement, UserProfile

class ScenicSpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'price', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('created_at',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'description', 'price', 'created_at')
    search_fields = ('room_type',)
    list_filter = ('created_at',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'scenic_spot', 'room', 'food', 'tour_date', 'total_amount', 'payment_status', 'created_at', 'payment_screenshot')
    search_fields = ('user__username',)
    list_filter = ('payment_status', 'tour_date', 'created_at')

class UserSharingAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')
    search_fields = ('user__username', 'title')
    list_filter = ('created_at',)

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'birth_date')
    search_fields = ('user__username', 'phone')
    list_filter = ('birth_date',)

admin.site.register(ScenicSpot, ScenicSpotAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(UserSharing, UserSharingAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
