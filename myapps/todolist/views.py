from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from .models import Todolistitem


def index(request):
    return render(request, 'todolist/index.html')
    
def addItem(request):
	x= request.POST['content']
	new_item = Todolistitem(content = x)
	new_item.save()
	return HttpResponseRedirect('/todolist/') 

def deleteItem(request, i):
    y = Todolistitem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todolist/') 

@login_required
def Todolist(request):
    items= Todolistitem.objects.all()
    return render(request, 'todolist/page.html',
    {'all_items':items}) 
