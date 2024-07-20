from django.contrib import admin
from .models import UserProfile, CV_Dataset

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'userhash', 'activestatus', 'logintime', 'email']

@admin.register(CV_Dataset)
class ComputerVisionProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
