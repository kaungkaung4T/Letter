from django.contrib import admin
from application.models import Profile, AppModel

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_image']

class AppModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'image']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(AppModel, AppModelAdmin)