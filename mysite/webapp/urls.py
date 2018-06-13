from django.urls import path, include
from webapp import views

urlpatterns = [
    path('', views.index, name='index' )
]
