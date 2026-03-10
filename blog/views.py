from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    post_list = Post.objects.select_related(
        'author',
        'location',
        'category'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]

    template = 'blog/index.html'
    context = {
        'post_list': post_list
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )

    if post.location and not post.location.is_published:
        pass
    template = 'blog/detail.html'
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
