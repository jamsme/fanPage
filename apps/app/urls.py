from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('database', views.database),
    path('post', views.passwordHtml),
    path('password', views.password),
    path('add', views.add),
]