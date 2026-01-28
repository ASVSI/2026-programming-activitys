from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout


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

def logout_view(request):
    logout(request)
    # Redirect to a desired page, e.g., the homepage or login page
    return redirect('home')