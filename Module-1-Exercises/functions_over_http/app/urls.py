# app/urls.py
from django.urls import path
from .views import hey_you, how_old, order_total

urlpatterns = [
    path('hey/<str:name>/', hey_you, name='hey_you'),
    path('age-in/<int:end>/<int:birthyear>/', how_old, name='how_old'),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>/', order_total, name='order_total'),
]
