from django.urls import path
from . import views
from todolist.views import *

urlpatterns = [
    path('todolist/',Todolist),
    path('additem/', addItem),
    path('deleteItem/<int:i>/', deleteItem), 
    path('updateItem/<int:i>/', updateItem),
    path("register/", register, name="register"),

]

handler404 = ‘todolist.views.error_404’
handler500 = ‘todolist.views.error_500’
handler403 = ‘todolist.views.error_403’
handler400 = ‘todolist.views.error_400’