from django.urls import path, re_path
from blog import views


urlpatterns = [
    path("", views.index),
    re_path(r"^about/", views.about, kwargs={'name': "Женя", 'age': 39}),
    # re_path(r"^about/", views.about),
    # re_path(r"^about/contact", views.contact),
    # path("about/", views.about),
    re_path(r"^contact/", views.contact),
    path('user/<str:name>/<int:age>', views.user),
    path('user/<str:name>/', views.user),
    path('user/', views.user),
]
