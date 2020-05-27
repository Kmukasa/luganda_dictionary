from django.urls import path

from . import views
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('search/',views.search, name='search'),
    path('add/',views.addWord, name='add'),
]