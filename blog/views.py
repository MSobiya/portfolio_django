from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
	every_blogs = Blog.objects
	return render(request, 'blog/all_blogs.html', {'every_blogs' : every_blogs})


def details(request, blog_id):
	blog_detail = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/details.html', {'blog_detail' : blog_detail})