
from django.urls import path
#from todo.views import todoListviews
from todo import views

urlpatterns = [
    path("list/", views.todoListviews.as_view()),
    path("admintodo/listcreate/", views.AdmintodoListCreateview.as_view()),
    path("create/",views.todocreateview.as_view()),

]