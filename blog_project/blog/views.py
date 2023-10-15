from django.shortcuts import render
from .models import Post, Tag


def post_list(request):
    search_query = request.GET.get("search", None)
    if search_query:
        post_list =  Post.objects.filter(title__icontains = search_query)
    else:
        post_list =  Post.objects.all()
    return render(request, "blog/post_list.html", context={"post_list": post_list})


def tag_list(request):
    tag_list = Tag.objects.all()
    return render(request, "blog/tag_list.html", context={"tag_list": tag_list})


def post_detail(request,pk):
    post = Post.objects.get(pk = pk)
    return render(request, "blog/post_detail.html", context  =  {"post": post})


def tag_detail(request,pk):
    tag = Tag.objects.get(pk = pk)
    return render(request, "blog/tag_detail.html", context  =  {"tag": tag})