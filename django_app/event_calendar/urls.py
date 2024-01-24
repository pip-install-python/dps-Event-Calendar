from django.urls import path, include
from event_calendar import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('new_event/', views.new_event, name='new_event')
    # path('sp/', views.home_sp, name='casa'),
]