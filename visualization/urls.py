from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('1/', views.get_data),
    path('2/', views.get_data2),
    path('3', MyView.as_view()),
    path('4', MyView2.as_view()),
]
