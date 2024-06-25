from django.urls import path, re_path, include
from blog import views
from django.urls import path
from django.views.generic import TemplateView
from blog import views

# product_patterns = [
#     path("", views.products),
#     path("comments/", views.comments),
#     path("questions/", views.questions),
#     # path("new/", views.new),
#     # path("top/", views.top),
# ]

# Использование TemplateView, что бы сразу вернуть содержимое шаблона
# urlpatterns = [
#     path("", views.index),
#     path("about/", TemplateView.as_view(template_name="blog/about.html")),
#     path("contact/", TemplateView.as_view(template_name="blog/contact.html")),
# ]

# urlpatterns = [
#     path('', views.index),
#     path("about/", TemplateView.as_view(template_name="blog/about.html", extra_context={"header": "О сайте"})),
#     path('contact/', TemplateView.as_view(template_name="blog/contact.html")),
# ]

# Расширение шаблонов НТМL-страниц на основе базового шаблона

# urlpatterns = [
#     path("", views.index),
#     path("about/", views.about),
# ]

# Тестирование
urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
]



# urlpatterns = [
#     path("", views.index),
    # path("index/<int:id>/", views.index),
    # path("access/<int:age>/", views.access),
    # path("user/", views.user),
    # path("products/<int:id>/", include(product_patterns)),
    # # path("products/", include(product_patterns)),
    # # re_path(r"^about/", views.about, kwargs={'name': "Женя", 'age': 39}),
    # # re_path(r"^contact/", views.contact),
    # path("contact/", views.contact),
    # path("details/", views.details),
    # # re_path(r"^about/", views.about),
    # # re_path(r"^about/contact", views.contact),
    # # path("about/", views.about),
    # path("about/", views.about),
    # path('user/<str:name>/<int:age>', views.user),
    # path('user/<str:name>/', views.user),
    # path('user/', views.user),
    # re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', views.user),
    # re_path(r'^user/(?P<name>\D+)/', views.user),
    # re_path(r'^user/(?P<age>\d+)', views.user),
    # re_path(r'^user/', views.user),
# ]
