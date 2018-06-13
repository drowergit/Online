from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'birthday', )
    list_filter = ('birthday', )

admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(EmailVerfiRecord)