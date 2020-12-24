from django.shortcuts import render,redirect

# Create your views here.

from .forms import Usermodelform

from django.contrib import messages


def formregister(request):
    form = Usermodelform()

    if request.method == 'POST':
        print(request.POST)
        form = Usermodelform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are successfully registered')
            return redirect('/')

    context = {'form': form }
    return render(request, 'simpleapp_form/register.html' , context)







