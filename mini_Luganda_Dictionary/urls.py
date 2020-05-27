"""mini_Luganda_Dictionary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from dictionary import views

from django.conf import settings
from django.conf.urls.static import static

from api import api_views

urlpatterns = [
    path('api/translations/', api_views.DictionaryList.as_view()),
    path('api/translations/new/', api_views.DictionaryCreate.as_view()),
    path('api/translations/<int:id>/', api_views.DictionaryRetrieveUpdateDestroy.as_view()),

    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('search/',views.search, name='search'),
    path('add/',views.addWord, name='add'),

] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
