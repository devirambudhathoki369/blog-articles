from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status',)
    search_fields = ('title', 'category__category_name', 'author__username', 'status',)
    list_editable = ('status',)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)