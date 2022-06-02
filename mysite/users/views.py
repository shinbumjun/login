from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User
# Create your views here.

def login_view(request):
    if request.method == "POST": # 만약에 POST라면
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("로그인 성공") # admin/1 -> 로그인 성공
            login(request, user) # -> 로그인된 상태(보여줄 수 있는것 만들기)
        else:
            print("로그인 실패") # 그 외 -> 로그인 실패

        # 참고 : https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.authenticate
    return render(request, "users/login.html") # 해당 위치

def logout_view(request):
    logout(request)
    return redirect("user:login") # 로그아웃이 끝났을 때는 로그인 페이지로

def signup_view(request): # 회원가입

    if request.method == "POST":
        print(request.POST) # POST라면 확인
        username = request.POST["username"] # 입력한 값 확인
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]

        user = User.objects.create_user(username, email, password) # 유저, 이메일, 비밀번호

        user.last_name = lastname # 추가적인 정보
        user.first_name = firstname
        user.student_id = student_id
        user.save()
        return redirect("user:login") # 회원가입을 하였으니 로그인하여라

    return render(request, "users/signup.html")