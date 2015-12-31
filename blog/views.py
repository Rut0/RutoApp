from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import BlogPost

# Create your views here.
def index(request):
    posts = get_list_or_404(BlogPost)
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def id(request, id):
    post = get_object_or_404(BlogPost, pk=id)
    context = {'post': post}
    return render(request, 'blog/index.html', context)


def word(request, word):
    post = get_object_or_404(BlogPost, title=word)
    context = {'post': post}
    return render(request, 'blog/index.html', context)
