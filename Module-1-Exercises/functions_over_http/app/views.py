# app/views.py
from django.http import HttpResponse

def hey_you(request, name):
    return HttpResponse(f"Hey, {name.capitalize()}!")

def how_old(request, end, birthyear):
    age = int(end) - int(birthyear)
    return HttpResponse(str(age))

def order_total(request, burgers, fries, drinks):
    burger_price = 4.50
    fries_price = 1.5
    drinks_price = 1
    total = (int(burgers) * burger_price) + (int(fries) * fries_price) + (int(drinks) * drinks_price)
    return HttpResponse(f"Order Total: ${total:.2f}")
