from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def get_all_post(request):
    all_posts = Post.objects.all()
    return return JsonResponse({'all posts': all_posts})
