from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('opinions/<int:worry_message_id>', views.opinions_message, name='opinions')
]