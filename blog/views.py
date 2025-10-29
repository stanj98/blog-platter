from django.shortcuts import render
from blog.models import Post
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView
)

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'

class PostCreateView(CreateView):
	model = Post
	fields = ['title', 'content']

#check out pytest when free

def about(request):

	return render(request, 'blog/about.html', {'title': 'About'})