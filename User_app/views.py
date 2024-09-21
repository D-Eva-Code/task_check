from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import new_form
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
       register_forms= new_form(request.POST) 
       if register_forms.is_valid():
           register_forms.save()
           messages.success(request, 'New User Successfully Created')
           return redirect("index")
            
    else:
    
        register_forms= new_form()
    return render(request, "register.html", {"register_forms": register_forms})



# def logout(request):
#     if request.method =="POST":
#         return render(request, "logout.html")
#        
#     else:
#         # return render(request, "logout.html")
#         return redirect('login')

@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return render(request, "logout.html")
    return render(request, "logout.html")

# @login_required
# def user_logout(request):
#     logout(request)
#     # return redirect("login")
#     return render(request, "logout.html", {})

