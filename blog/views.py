from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Главная страница</h2>")


def products(request, id):
    return HttpResponse(f"Товар {id}")


def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")


def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")


# def new(request):
#     return HttpResponse("Новые товары")


# def top(request):
#     return HttpResponse("Наиболее популярные товары")


# def about(request, name, age):
#     return HttpResponse(
#         f"""
#         <h2>О пользователе</h2>
#         <p>Имя: {name}</p>
#         <p>Возраст: {age}</p>
# """
#     )


# def contact(request):
#     return HttpResponse("<h2>Контакты</h2>")


# def user(request, name='UserNone', age=0):
#     return HttpResponse(f"<h2>Имя: {name}. Возраст: {age}</h2>")


# def user(request, name="UserNone", age=0):
#     return HttpResponse(f"<h2>Имя: {name}. Возраст: {age}</h2>")
