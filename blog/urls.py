from django.urls import path, re_path, include
from blog import views



product_patterns = [
    path("", views.products),
    path("comments/", views.comments),
    path("questions/", views.questions),
    # path("new/", views.new),
    # path("top/", views.top),
]


urlpatterns = [
    path("index/<int:id>/", views.index),
    path("access/<int:age>/", views.access),
    path("user/", views.user),
    path("products/<int:id>/", include(product_patterns)),
    # path("products/", include(product_patterns)),
    # re_path(r"^about/", views.about, kwargs={'name': "Женя", 'age': 39}),
    # re_path(r"^contact/", views.contact),
    path("contact/", views.contact),
    path("details/", views.details),
    # re_path(r"^about/", views.about),
    # re_path(r"^about/contact", views.contact),
    # path("about/", views.about),
    path("about/", views.about),
    # path('user/<str:name>/<int:age>', views.user),
    # path('user/<str:name>/', views.user),
    # path('user/', views.user),
    # re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', views.user),
    # re_path(r'^user/(?P<name>\D+)/', views.user),
    # re_path(r'^user/(?P<age>\d+)', views.user),
    # re_path(r'^user/', views.user),

]
