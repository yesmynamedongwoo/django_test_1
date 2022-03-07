from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Article, Comment


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})



@login_required(login_url='signin')
# 로그인이 되어있을때
def new(request):
    if request.method == 'POST':
        # 포스트로 응답을 받으면 아래 정보를 보냄냄
        article = Article.objects.create(
            auther=request.user,
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('detail', article.pk)
        #article.pk 아티클의 정보를 같이 넘겨줌

    else:
        return render(request, 'blog/new.html')


@login_required(login_url='signin')
def detail(request, pk): # 사용자가 어떤 글을 보고자 했는지를 받아줘야함
    article = Article.objects.get(pk=pk)  #왼쪽의 pk 는 필드명, 오른쪽의 pk는 변수명
    return render(request, 'blog/detail.html', {'article':article}) # 왼쪽은 html 에서쓰는 변수 오른쪽은 views에서쓰는 변수

@login_required(login_url='signin') # 로그인하지 않을 경우 리다이렉트
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    # 남이 쓴 글에 대해서 수정 요청을 방지
    if request.user == article.auther:
        # POST 일때는 글 수정
        if request.method == 'POST':
            article.title =request.POST['title']
            article.content = request.POST['content']
            article.save()
            return redirect('detail',article.pk)
        else:
            return render(request, 'blog/edit.html', {'article':article})
    else:
        return render(request, 'blog/edit.html',{'error':'잘못된 접근입니다'} )


@login_required(login_url='signin') # 로그인하지 않을 경우 리다이렉트
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    # 남이 쓴 글에 대해서 수정 요청을 방지
    if request.user == article.author:
        article.delete()
        return redirect('index')
    else:
        return redirect('detail', article.pk)