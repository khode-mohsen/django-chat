from django.urls import path
from chat import views

urlpatterns = [
    path('<str:slug>/', views.chatRoom, name='chat_slug'),
    path('',views.rooms),
]
