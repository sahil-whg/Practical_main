from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserprofileForm
from .models import Userprofile
# Create your views here.
def userprofile(request):
    form = UserprofileForm(request.POST)
    if request.method == "POST":
        form = UserprofileForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserprofileForm()

        context = {
                'form':form
            }
        return render(request, 'main_page.html',context)
    else:
        context = {
            'form': form
        }
        return render(request, 'main_page.html',context)

def display(request):
    display = Userprofile.objects.all()
    for first in display:
        print(first.id)
    return render(request,'display.html',{'display':display})

def delete(request,*args, **kwargs):
    id_grab = Userprofile
    id_grab = kwargs['pk']
    query = Userprofile.objects.get(id=id_grab)
    query.delete()
    return HttpResponse("Deleted!")

def filter(request):
    query_all = Userprofile.objects.all()
    filter_lasttwo = query_all[::-2]
    return render(request,'filter_lasttwo.html',{'filter_lasttwo':filter_lasttwo})
