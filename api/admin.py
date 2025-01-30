from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "github_url", "current_datetime"]

admin.site.register(User, UserAdmin)