from django.contrib import admin
from home.models import CustomUser

# Register your models here.
class CustomUserAdmin_by(admin.ModelAdmin):
    list_display=('name','id','email','number','date','is_active','is_staff','password')
admin.site.register(CustomUser,CustomUserAdmin_by)