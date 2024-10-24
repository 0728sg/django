from django.contrib import admin
from .models import Post, Tag, Category



@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['titile', 'content', ' rate', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']


admin.site.register(Tag)
admin.site.register(Category)