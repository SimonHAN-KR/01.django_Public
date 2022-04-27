from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from data.models import *
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        if not (username and email and password and re_password):
            return render(request, "user/register.html", {'register_error': '위의 빈칸을 모두 입력해주시기 바랍니다.'})
        elif User.objects.filter(username=request.POST['username']).exists():
            return render(request, "user/register.html", {'register_error': '해당 ID는 이미 사용되고 있습니다.'})
        elif User.objects.filter(email=request.POST['email']).exists():
            return render(request, "user/register.html", {'register_error': '해당 E-mail에 해당하는 아이디가 이미 존재합니다.'})
        elif request.POST["password"] == request.POST["re_password"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            auth.login(request, user)

            profile = Profile()

            profile.user = user
            # # profile.u_name = request.POST["u_name"]
            # profile.gender = request.POST["gender"]
            # # profile.job = request.POST["job"]

            profile.save()

            return redirect("/")
        return render(request, "user/register.html", {'register_error': '비밀번호와 비밀번호 확인이 일치하지 않습니다.'})
    return render(request, "user/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if not (username and password):
            return render(request, 'user/login.html', {'login_error': 'ID와 Password를 모두 입력해주세요.'})
        elif user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return render(request, 'user/login.html', {'login_error': 'ID 혹은 Password가 일치하지 않습니다.'})
    else:
        return render(request, 'user/login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required  # 로그인이 되어 있어야만 해당 코드가 작동하게 해주는 데코레이터
def session_test(request):
    conn_user = request.user
    conn_profile = Profile.objects.get(user=conn_user)

    # if conn_profile.gender == "M":
    #     conn_profile.gender = "남성"
    # else:
    #     conn_profile.gender = "여성"
    #
    # if conn_profile.job == "P":
    #     conn_profile.job = "교수/강사(Professor/Lecturer)"
    # elif conn_profile.job == "S":
    #     conn_profile.job = "학생(Student)"
    # elif conn_profile.job == "R":
    #     conn_profile.job = "연구원(Researcher)"
    # else:
    #     conn_profile.job = "기타(Etc.)"

    context = {  # 여기에는 데이터 베이스 형식과 동일하게 작성 해야함. 벤치 확인
        'username': conn_user.username,
        'user_email': conn_user.email,
        # 'user_gender' : conn_profile.gender,
        # 'user_job' : conn_profile.job,
        }
    return render(request, '/', context=context)
    # 이제 urls 와 html 순서대로 작성하기


def index(request):
    return render(request, 'index.html')
