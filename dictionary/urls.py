from django.urls import path

from . import views
# import api.views

urlpatterns = [
    path('',views.index, name='index'),
    path('search/', views.search, name='search'),
]