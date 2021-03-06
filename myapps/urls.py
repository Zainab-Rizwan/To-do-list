"""myapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import include, path
from todolist import views as todolist
from users import views as user_views
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',todolist.index ),
    path('todolist/',todolist.Todolist ),
    path('addItem/',todolist.addItem ),
    path('deleteItem/<int:i>/',todolist.deleteItem ),
    path('updateItem/<int:i>/',todolist.updateItem ),
    path('register/', user_views.register),
    path('profile/', user_views.profile),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html')),



]

handler404 = 'todolist.views.error_404'
handler403 = 'todolist.views.error_403'
handler400 = 'todolist.views.error_400'
handler500 = 'todolist.views.error_500'
