from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseNotFound
from .models import todolist, item
from Main.forms import CreatNewlist , Delete
# Create your views here.


def home(response):
    My_dict = {}
    return render(response ,'Main/home.html', My_dict)


def list(response , id):
    ls = todolist.objects.get(id = id)
    if ls in response.user.todolist.all():
        #to count progress
        num = 0
        notyet = 0
        done = 0
        #
        if response.method == "POST": 
        #delete the List
            if response.POST.get('delete'):
                li = todolist.objects.get(id = id)
                li.delete()
                return redirect('Home')
        #Add new Item to the List
            elif response.POST.get("newItem"):
                info = response.POST.get('new')
                ls.item_set.create(text=info, done = False)
        #save changes accured to the complete of Item_set (item)

            elif response.POST.get('save'):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id))=="clicked":
                        item.done = True
                    else:
                        item.done = False
                    item.save()

        for i in ls.item_set.all():
            num +=1
            if i.done == True:
                done += 1 
        if num > 0 :
            progress = done * 100 /num
        else:
            progress = 0
        My_dict = {'name':ls, 'progress':progress}
        return render(response ,'Main/list.html', My_dict)
    else:
        return HttpResponseNotFound('Doesnt exist')

def create(response):
    user = response.user
    if response.method == "POST":
        form = CreatNewlist(response.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = todolist(name = n)
            t.save()
            user.todolist.add(t)
            return redirect('Home')

    else:
        form = CreatNewlist()
    My_dict = {"form":form}
    return render(response , 'Main/create.html',My_dict)
def delete(response):
    if response.method == 'POST':
        form = Delete(response.POST)
        if form.is_valid():
            Id = form.cleaned_data['name']
            nu = todolist.objects.get(name = Id)
            nu.delete()
            return redirect('Home')
    else:
        form = Delete()
    My_dict = {"form": form}
    return render(response, 'Main/Delete.html', My_dict)