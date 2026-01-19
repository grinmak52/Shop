from django.urls import path
from .views import MyLogoutView, MyLoginView, UserProfile, RegisterView


app_name = "accounts"

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("profile/", UserProfile.as_view(), name="profile"),
    path("register/", RegisterView.as_view(), name="register"),
]
