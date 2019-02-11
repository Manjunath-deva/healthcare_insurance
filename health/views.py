from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect

def base(request):
    return render(request, 'health/base.html', {})
def index1(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            return redirect('index1')
        else:
            form = PostForm()
    return render(request, 'health/index1.html', {})
def login(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    return render(request, 'health/login.html', {})
