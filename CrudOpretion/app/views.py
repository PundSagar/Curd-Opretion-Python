from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST' :
        fm = StudentRegistration(request.POST)
        if fm.is_valid():

            # fm.save()
            name1 = fm.cleaned_data['name']
            email1 = fm.cleaned_data['email']
            pass1 = fm.cleaned_data['password']
            reg = User(name=name1, email=email1, password= pass1)
            reg.save()
            fm = StudentRegistration()
    else :
         fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'app/addandshow.html',{'form': fm, 'stu':stud})



def update_data(request, id):
    pi = User.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        else:
           pi = User.objects.get(pk=id)
           fm = StudentRegistration(instance=pi)
    return render(request, 'app/updatestudent.html', {'form' : fm})



def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')




    