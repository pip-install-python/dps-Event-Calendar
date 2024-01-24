from django.urls import path, include
from user_account import views

urlpatterns = [
    path('', views.user_profile, name='account_payment_settings'),
    path('settings/', views.account_settings, name='account_settings'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_view, name='logout')

    # path('sp/', views.home_sp, name='casa'),
]