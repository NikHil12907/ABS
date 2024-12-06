from django.contrib import admin
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','user_type','is_active','is_staff')
    search_fields = ('username','email')
    list_filter = ('user_type','is_active')    


admin.site.register(CustomUser, CustomUserAdmin)
