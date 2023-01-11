from django.urls import path

from . import views

urlpatterns = [
    path("get_response/", views.ChatView.as_view(), name="chatview"),
    path('get_token/', views.LoginView.as_view(), name='get_token'),
]
