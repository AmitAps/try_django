from django.urls import path,re_path #url

from .views import (article_detail_view,
                        article_list_view,
                        #article_create_view,
                        article_update_view,
                        article_delete_view,
                        )

urlpatterns = [
    path('',article_list_view),
    #path('news/create/',article_create_view), #it will create issues with article_id and slug
    path('<int:article_id>/<str:slug>/',article_detail_view),
    #path('article-new/',article_create_view),
    path('<int:article_id>/<str:slug>/edit/',article_update_view),
    path('<int:article_id>/<str:slug>/delete/',article_delete_view),
    # #re_path(r'^news/(?P<article_id>\d+)/$',article_detail),
    # # path('page/', about_page),
    # # path('pages/', about_page),
    # re_path('pages?/$', about_page),
    # path('about/', about_page),
    # path('contact/', contact_page),

]
