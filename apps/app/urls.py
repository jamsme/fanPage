from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('post', views.passwordHtml),
    path('database', views.database),
    path('password', views.password),
    path('add', views.add),
]