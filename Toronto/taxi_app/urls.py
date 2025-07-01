from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('rates',views.rates,name='rates'),
    path('niagara',views.niagara,name='niagara'),
    path('ajax',views.ajax,name='ajax'),
    path('ancaster',views.ancaster,name='ancaster'),
    path('blog',views.blog,name='blog'),
]