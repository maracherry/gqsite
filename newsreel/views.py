from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
#defined in urls.py
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, '/var/www/genderqueeries/templates/newsreel/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, '/var/www/genderqueeries/templates/newsreel/post_detail.html',{'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('newsreel.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, '/var/www/genderqueeries/templates/newsreel/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('newsreel.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'newsreel/post_edit.html', {'form': form})
