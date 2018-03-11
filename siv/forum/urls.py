from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('createopinion/<int:worry_message_id>', views.create_opinion_message, name='create_opinion'),
    path('categories', views.categories, name='categories'),
    path('createmessage', views.create_worry_message, name='create_message')
]