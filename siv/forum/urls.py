from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('opinions/<int:worry_message_id>', views.opinions_message, name='opinions'),
    path('categories', views.categories, name='categories'),
    path('createmessage', views.create_worry_message, name='create_message')
]