from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('1/', MyView_Funtion1.as_view()),
    path('2/', MyView_Funtion2.as_view()),
    path('3/', MyView_Funtion3.as_view()),
    path('4/', MyView_Funtion4.as_view()),
    path('5/', MyView_Funtion5.as_view()),
    path('6/', MyView_Funtion6.as_view()),
    path('7/', MyView_Funtion1.as_view()),
    path('8/', MyView_Funtion1.as_view()),
]
