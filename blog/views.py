from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from .models import Post
from django.utils import timezone


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    name = 'Movsar'
    return render(request, 'blog/index.html', {'posts': posts, 'name2': name})


def index2(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index2.html', {'posts': posts})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка! СТраница не найдена</h1>')


def post_info(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_info.html', {'post': post})
# Create your views here.
