
from django.shortcuts import render
from .models import Blog,Comment
from .forms import BlogForm,CommentForm,UserSignupForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def user_registration(request):
	if request.method=='POST':
		form = UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = UserSignupForm()
	return render(request,'registration/create_user.html',{'form':form})

def home(request):
	blogs = Blog.objects.all()
	latest_blog = Blog.objects.all().order_by('created_date')[0]
	context_dict = {
		'blogs':blogs,
		'latest_blog':latest_blog,
	}
	return render(request, 'blog/dashboard.html', context_dict)
@login_required
def add_blog(request):
	form = BlogForm()
	if request.method == 'POST':
		print(request.POST)
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')

	context_dict = {'form': form}
	return render(request, 'blog/add_blog.html', context_dict)


def blog_details(request, id):
	blog = Blog.objects.get(id=id)
	if request.method == 'POST':
		print(request.POST)
		form  = CommentForm(request.POST)
		print('hello')

		if form.is_valid():
			print('yes')
			comment = form.save(commit=False)
			comment.blog=blog
			comment.comment_by =request.user
			comment.save()
			print(comment)
			return redirect('home')
		else:
			print('no')
	request.session['last_viewed'] = blog.id
	comments= Comment.objects.filter(blog=blog)
	print(comments)
	context_dict = {'blog':blog,'comments':comments}
	return render(request, 'blog/blog_details.html', context_dict)

@login_required
def edit_blog(request, id):
	blog=Blog.objects.get(id=id)

	if request.method=='POST':
		form=BlogForm(request.POST, instance=blog)
		if form.is_valid():
			form.save()
			return redirect('home')
	form=BlogForm(instance=blog)
	context_dict={'form':form}
	return render(request, 'blog/edit_blog.html',context_dict)

@login_required
def delete_blog(request, id):
	blog=Blog.objects.get(id=id)
	blog.delete()
	return redirect('home')

# def home(request):
# 	return render(request, 'blog/home.html')
#
# def index(request):
# 	return render(request, 'index.html')
