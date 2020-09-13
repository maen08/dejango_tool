from django.shortcuts import render,redirect
from .models import Fullname
from .forms import FullnameForm



def fullname_view(request):
    form = FullnameForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
        
    args = {'form':form}
    return render(request, template_name='index.html',context=args)
        

