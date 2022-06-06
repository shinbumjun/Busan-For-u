from django.shortcuts import render
from blog.models import Category, Post
from django.views import generic # 글의 세부내용
from django.contrib.auth.mixins import LoginRequiredMixin # 글 작성하기 페이지
from django.views.generic.edit import CreateView # 글 작성하기 페이지 (로그인한 사람만 작성 가능)

# Create your views here.
def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6] # 최근에 작성된 순으로 불러오기 (내림차순으로 6개)
    context = {
        "post_latest": post_latest
    }
    
    return render(req, "index.html", context=context) # 여기로 이동 (index에 전달)

class PostDetailView(generic.DetailView): # 상세보기
    model = Post

class PostCreate(LoginRequiredMixin, CreateView): # 로그인 한 사람만 글 작성
    model = Post
    fields = ["title", "title_image", "content", "category"]

# class PostCreate(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ["title", "title_image", "content", "category"]

# def single(req): # single로 오면
#     context = {

#     }
    
#     return render(req, "single.html", context=context) # 여기로 이동

