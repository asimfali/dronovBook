from django.urls import path
from .views import index, other_page, LoginView, profile, by_rubric, BBLogoutView, ChangeUserInfoView, \
    BBPasswordChangeView, RegisterDoneView, RegisterUserView, user_activate

app_name = 'main'
urlpatterns = [
    path('accoouts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accoouts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accoouts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accoouts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accoouts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accoouts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('<str:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
