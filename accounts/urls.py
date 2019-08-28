from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.login_request),
    path('register/', views.register_request),
    path('logout/', views.logout_request),
    path('profile/<str:username>/', views.profile),
]
