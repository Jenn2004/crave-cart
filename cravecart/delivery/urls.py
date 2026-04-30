
from django.urls import include, path # pyright: ignore[reportMissingModuleSource]
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("open_signup", views.open_signup, name="open_signup"),
    path("open_signin", views.open_signin, name="open_signin"),
    path("signup", views.signup, name="signup")
]