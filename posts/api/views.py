from django.shortcuts import render
from django.http import JsonResponse
from ..models import Post
from .serializers import PostSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def get_all_post(request):
    all_posts = {}
    all_posts = Post.objects.all()
    print(all_posts)
    serializer = PostSerializer(
        all_posts, context={'request': request}, many=True)
    print(serializer, serializer.data)
    return JsonResponse(serializer.data, safe=False)
    # return JsonResponse({'all_posts': all_posts})


def create_post(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
