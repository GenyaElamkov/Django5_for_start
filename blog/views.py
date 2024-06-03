from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)


# def index(request):
#     return HttpResponse("<h2>Главная страница</h2>")


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


def about(request, name, age):
    return HttpResponse("About")


def contact(request):
    return HttpResponseRedirect("/about")


def details(request):
    return HttpResponsePermanentRedirect("/")


# def user(request, name='UserNone', age=0):
#     return HttpResponse(f"<h2>Имя: {name}. Возраст: {age}</h2>")


def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "NoneName")
    return HttpResponse(f"<h2>Имя: {name}. Возраст: {age}</h2>")


# def user(request, name="UserNone", age=0):
#     return HttpResponse(f"<h2>Имя: {name}. Возраст: {age}</h2>")


def index(request, id):
    people = [None, "Bob", "Sam", "Tom"]
    # если пользователь найден, возвращаем его
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    # если нет, то возвращаем ошибку 404
    return HttpResponseNotFound("Not Found")


def access(request, age):
    # если возраст НЕ входит в диапазон 1-110, посылаем ошибку 400
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    # если возраст больше 17, то доступ разрешен
    if age > 17:
        return HttpResponse("Доступ разрешен")
    # если нет, то возвращаем ошибку 403
    return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")
