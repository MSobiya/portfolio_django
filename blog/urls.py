from django.urls import path
from . import views

urlpatterns = [
    #homepage of blog which will be accessed by localhost/blog/
    path('', views.allblogs, name="all_blogs"),

    #to open details/body of specific article we have to access localhost/blog/admin/1 for 1st block 2 for second blog, that's why we are using int.
    path('<int:blog_id>/', views.details, name="details"),
]

