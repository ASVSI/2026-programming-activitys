from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def home(request):
    form=UserCreationForm()
    if request.method == 'GET':
        
        form= UserCreationForm()
        context={
            "form":form
        }
        return render(request,'register.html',context=context)

    else:
        print(request.POST)
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('form is submited sucessfully ')
        else:
            return HttpResponse('form is invallid')
        return render(request, "register.html")