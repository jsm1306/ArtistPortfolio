from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
