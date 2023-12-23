from django.contrib import admin
from app_version_1.models import signup


class signupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'dob', 'password')


admin.site.register(signup, signupAdmin)
