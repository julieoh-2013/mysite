from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook

# Create your views here.
def index(request):
    guestbook_list = Guestbook.objects.all().order_by("-regdate")
    return render(request, "guestbook/list.html",{'guestbook_list':guestbook_list})

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect("/guestbook")

def deleteform(request):
    id = request.GET['id']
    return render(request, "guestbook/deleteform.html",{'id':id})

def delete(request):
    Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete()
    return HttpResponseRedirect("/guestbook")