from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('database', views.database),
    path('post', views.passwordHtml),
    path('password', views.password),
    path('add', views.add),
    path('submitPost', views.submitPost),
    path('append', views.append),
    path('delete/<int:post_id>', views.delete),
    path('pinterest', views.pinterest),
    path('pinterestForm', views.pinterestForm)
]