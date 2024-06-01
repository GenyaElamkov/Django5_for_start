from django.urls import path
from main_app import views


urlpatterns = [
    path("", views.index),
    path("accounts/<str:name>/<int:age>/", views.accounts),
    path("accounts/<str:name>/", views.accounts),
    path("accounts/", views.accounts),
    path("home/", views.home),
    path("message/", views.message),
]
