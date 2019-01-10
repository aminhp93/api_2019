from django.shortcuts import render
from django.http import JsonResponse
from ..models import Post
# Create your views here.


def get_all_post(request):
    all_posts = {}
    all_posts = Post.objects.all()
    print(all_posts)
    return JsonResponse({'all_posts': 'all_posts'})
