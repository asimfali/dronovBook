from django.urls import path
from .views import index, other_page, LoginView, profile

app_name = 'main'
urlpatterns = [
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
