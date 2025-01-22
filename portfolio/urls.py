from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('aboutme/',views.aboutme,name='aboutme'),
]

