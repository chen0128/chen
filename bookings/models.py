from django.db import models
from django.contrib.auth.models import User

class ScenicSpot(models.Model):
    name = models.CharField('景区名称', max_length=200)
    description = models.TextField('景区描述')
    location = models.CharField('景区位置', max_length=200)
    price = models.DecimalField('价格', max_digits=10, decimal_places=2, default=0.0)
    image = models.ImageField('景区图片', upload_to='scenic_spots/', null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_type = models.CharField('房间类型', max_length=100)
    description = models.TextField('房间描述')
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    image = models.ImageField('房间图片', upload_to='rooms/', null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)


    def __str__(self):
        return self.room_type

class Food(models.Model):
    name = models.CharField('美食名称', max_length=200)
    description = models.TextField('美食描述')
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)
    image = models.ImageField('美食图片', upload_to='foods/', null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

class UserSharing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('分享标题', max_length=200)
    content = models.TextField('分享内容')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    title = models.CharField('公告标题', max_length=200)
    content = models.TextField('公告内容')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('电话', max_length=15)
    address = models.CharField('地址', max_length=255)
    birth_date = models.DateField('出生日期', null=True, blank=True)
    profile_picture = models.ImageField('头像', upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    scenic_spot = models.ForeignKey(ScenicSpot, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    tour_date = models.DateField('旅游日期', null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    total_amount = models.DecimalField('总金额', max_digits=10, decimal_places=2)
    payment_status = models.CharField('支付状态', max_length=20, choices=[('pending', '待支付'), ('completed', '已完成')], default='pending')
    payment_date = models.DateTimeField('支付日期', null=True, blank=True)
    payment_screenshot = models.ImageField('付款截图', upload_to='payment_screenshots/', null=True, blank=True)

    def __str__(self):
        return f'Booking {self.id} by {self.user.username}'