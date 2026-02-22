from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog, Category


def post_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id, status=1)
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)