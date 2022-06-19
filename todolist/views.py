from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from .models import TodoItem



def index(request):
    return render(request, 'todolist/index.html')
    
def addItem(request):
	x= request.POST['content']
	new_item = TodoItem.objects.create(name=x, user=request.user)
	new_item.save()
	return HttpResponseRedirect('/todolist/') 

def deleteItem(request, i):
    y = TodoItem.objects.get(id=i, user=request.user)
    y.delete()
    return HttpResponseRedirect('/todolist/') 

def updateItem(request, i):
    y = TodoItem.objects.get(id=i, user=request.user)
    y.name= request.POST.get(f"todo_{i}")
    y.save()
    return HttpResponseRedirect('/todolist/') 

@login_required(login_url='/index')
def Todolist(request):
    items = TodoItem.objects.filter(user=request.user)
    return render(request, "todolist/page.html",  {'all_items':items})

def error_404(request, exception):
        data = 404
        return render(request,'todolist/error.html', {'data':data})


def error_403(request, exception):
        data = 403
        return render(request,'todolist/error.html', {'data':data})

def error_400(request,  exception):
        data = 400
        return render(request,'todolist/error.html', {'data':data})

def error_500(request):
        data = 500
        return render(request,'todolist/error.html', {'data':data})




