from django.contrib import admin
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.unregister(User)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display=('book_id','title','author')
  search_fields=('title','author')
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff')
    