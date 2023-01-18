from django.urls import path

from . import views

app_name="posts"

urlpatterns=[
    path("",views.ideas_list,name="ideas_list"),
    path("ideas/create",views.ideas_create,name="ideas_create"),
    path("ideas/<int:pk>",views.ideas_retrieve,name="ideas_retrieve"),
    path("ideas/<int:pk>/update",views.ideas_update,name="ideas_update"),
    path("ideas/<int:pk>/delete",views.ideas_delete,name="ideas_delete"),
    path("devtool/list",views.devtool_list,name="devtool_list"),
    path("devtool/<int:pk>",views.devtool_retrieve,name="devtool_retrieve"),
    path("devtool/create",views.devtool_create,name="devtool_create"),
    path("devtool/<int:pk>/update",views.devtool_update,name="devtool_update"),
    path("devtool/<int:pk>/delete",views.devtool_delete,name="devtool_delete"),
    
]