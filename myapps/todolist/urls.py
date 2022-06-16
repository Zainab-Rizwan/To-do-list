from django.urls import path
from . import views
from todolist.views import *

urlpatterns = [
    path('todolist/',Todolist),
    path('additem/', addItem),
    path('deleteItem/<int:i>/', deleteItem), 
]
