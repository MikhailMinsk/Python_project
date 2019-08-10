from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:page>/', views.other_page, name='other'),
    # account
    path('accounts/login/', views.ShopLoginView.as_view(), name='login'),
    path('accounts/logout/', views.ShopLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', views.ChangeUserPasswordView.as_view(), name='password_change'),
    path('accounts/register/', views.RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/activate/<str:sign>/', views.user_activate, name='register_activate'),
    path('accounts/register/delete/', views.DeleteUserView.as_view(), name='profile_delete'),
]