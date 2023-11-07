# codingbat_over_http/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('warmup-1/near-hundred/<int:num>/', views.near_hundred, name='near-hundred'),
    path('warmup-2/string-splosion/<str:str>/', views.string_splosion, name='string-splosion'),
    path('string-2/cat-dog/<str:str>/', views.cat_dog, name='cat-dog'),
    path('logic-2/lone-sum/<int:a>/<int:b>/<int:c>/', views.lone_sum, name='lone-sum'),
    # Add similar URL patterns for other challenges
]
