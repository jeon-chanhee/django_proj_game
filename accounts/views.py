from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


# 로그인하지 않은 유저는 접근해서는 안 될 뷰
@login_required
def profile(request: HttpRequest):
    # if not request.user.is_authenticated: #  User 모델 인스턴스이거나 AnonymousUser 클래스 인스턴스
    # return redirect("/accounts/login/")
    return render(request, "accounts/profile.html")


def signup(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(
        request,
        "accounts/signup_form.html",
        {
            "form": form,
        },
    )
