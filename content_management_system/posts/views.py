from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            print(request.FILES)
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # Truyền cả request.FILES vào form
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('post_list')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'posts/register.html', {'form': form})

# def search(request):
#     query = request.GET.get('q')
#     results = None
#     if query:
#         results = Post.objects.filter(your_field__icontains=query)
#     return render(request, 'posts/search.html', {'results': results})
@login_required
def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # Gán người dùng hiện tại là tác giả của bình luận
            comment.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comment_form': form})