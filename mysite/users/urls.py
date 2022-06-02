from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login", views.login_view, name='login'), # *name을 주면 템플릿에서 간단하게 사용 가능
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup")
]