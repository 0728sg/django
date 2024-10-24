from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django import forms
from .models import Post
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required



def http_response(request):
    return HttpResponse('Hello')


def html_response(request):
    return render(request, 'index.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_index.html', {'posts': posts})

    search_query = request.GET.get('search', '')

    if search_query:
        posts = posts.filter(title__icontains=search_query)

    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/post_index.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/post_detail_view.html', {'post': post})


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    rate = forms.IntegerField()


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                rate=form.cleaned_data['rate']
            )
        elif form.is_valid():
            form.save()
            return redirect('post_success')
    else:
       form = PostModelForm()

    return render(request, 'create_post.html', {'form': form})


def post_success(request):
    return HttpResponse("Post created")


def profile_view(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {
        'profile': user_profile,
        'posts': user_posts
    })


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostModelForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})
