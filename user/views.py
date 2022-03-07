from django.shortcuts import render , redirect
from django.contrib import auth
from django.contrib.auth.models import User    # 장고의 유저모델을 가져옴
from django.contrib.auth.decorators import login_required  # 장고의  로그인 함수


# Create your views here.






def signup(request):
    if request.method == 'POST':
        # 만약 아이디가 중복이라면?.. 예외처리 해줘야함
        found_user = User.objects.filter(username= request.POST['username'])
        if len(found_user) > 0:
            return render(request, 'user/signup.html', {'error':'아이디가 이미 존재합니다'})
        else:
            new_user = User.objects.create_user(
                username=request.POST['username'],  # [] 안에있는건 html에 네임값
                password=request.POST['password']
            )
            auth.login(request,new_user)
            return redirect('index')
            #post 로 데이터가 들어왔을때
            # form 태그 요청일떄
            # 회원가입 + 로그인

    else:
        # 그냥 링크타고 들어왔을떄
        #회원가입 정보 입력하는 페이지 보여줘
        return render(request, 'user/signup.html')

def signin(request):
    if request.method == 'POST':
        #로그인
        found_user = auth.authenticate(request,
            username =request.POST['username'],
            password =request.POST['password']
                                       )
        if found_user is not None:
            auth.login(request, found_user)
            return redirect('index')
        else:
            return render(request, 'user/signin.html' , {'error': '사용자 정보가 존재하지 않습니다'})
    else:
        #로그인 정보 입력하는 페이지를 보여줌
        return render(request, 'user/signin.html')


@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('index')

#  redirect 와  render 차이
# render 동일한 url 에 html 만 띄어줌
# redirect  해당url로 가면서 해당 함수가 작동을함  즉 url 이 바뀜