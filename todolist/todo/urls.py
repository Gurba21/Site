from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('add',addTodo,name='add'),
    path('complete/<todo_id>',completeTodo,name='complete'),
    path('deletecomplete',deleteCompleted,name='deletecomplete'),
    path('deleteall',deleteALL,name='deleteall'),

]