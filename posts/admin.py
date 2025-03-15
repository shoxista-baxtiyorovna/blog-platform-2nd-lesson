from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'status', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'category', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

