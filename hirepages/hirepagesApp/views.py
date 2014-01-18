from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from hirepagesApp.models import User, Looker
from hirepagesApp.forms import SignupForm

#################################################
############## SIGNUP, LOGIN ####################
#################################################

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User(email=cd['email'],
                    password=cd['pwd'],
                    firstName=cd['firstName'],
                    middleName=cd['middleName'],
                    lastName=cd['lastName'],
                    dateOfBirth=cd['dateOfBirth'],
                    workNumber=cd['workNumber'],
                    cellNumber=cd['cellNumber'],
                    role=cd['role'],)
            user.save()
            return render(request, 'login.html', Context())
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    
def login(request):
    return render(request, 'login.html', Context())

    


#################################################
########### LOOKER CRUD #########################
#################################################
 
def create_looking_page(request):
    ctx = Context()
    return render(request, 'edit_looking_page.html', ctx)

def read_looking_page(request):
    ctx = Context()
    lookingId = 0 #TODO get this from the user from the session
    looker = User.objects.filter(id=lookingId)
    return render(request, 'view_looking_page.html', ctx)

def edit_looking_page(request):
    ctx = Context()
    return render(request, 'edit_looking_page.html', ctx)

def update_looking_page(request):
    ctx = Context()
    return render(request, 'view_looking_page.html', ctx)

def delete_looking_page(request):
    ctx = Context()
    return render(request, 'launch_page.html', ctx)
