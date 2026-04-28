
from django.urls import include, path # pyright: ignore[reportMissingModuleSource]
from . import views

urlpatterns = [
    path('', views.home)
]