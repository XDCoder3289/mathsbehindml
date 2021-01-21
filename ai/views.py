from django.shortcuts import render
from ai.models import Category, Post
from django.core.paginator import Paginator

def index(request):
    context_dict = {}
    category_list = Category.objects.all()
    context_dict['categories'] = category_list
    return render(request, 'index.html', context=context_dict)


def cat(request, category_name_slug):
    context_dict = {}
    category = Category.objects.get(slug=category_name_slug)
    posts = Post.objects.filter(category=category)
    context_dict['posts'] = posts
    context_dict['category'] = category
    return render(request, "category.html", context=context_dict)

def post(request, category_name_slug, post_name_slug):
    context_dict = {}
    post = Post.objects.get(slug=post_name_slug)
    posts = Post.objects.all()
    category = Category.objects.get(slug=category_name_slug)
    context_dict['post'] = post
    context_dict['posts'] = posts
    context_dict['category'] = category
    return render(request, 'post.html', context=context_dict)