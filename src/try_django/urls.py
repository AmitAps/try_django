"""try_django URL Configuration

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
from django.urls import path,re_path #url

from news.views import article_detail, article_list_view

from .views import home_page,about_page,contact_page
urlpatterns = [
    path('tst-admin/', admin.site.urls),
    path('home/', home_page),
    path('news/',article_list_view),
    path('news/<int:article_id>/<str:slug>/',article_detail),
    #re_path(r'^news/(?P<article_id>\d+)/$',article_detail),
    # path('page/', about_page),
    # path('pages/', about_page),
    re_path('pages?/$', about_page),
    path('about/', about_page),
    path('contact/', contact_page),

]
