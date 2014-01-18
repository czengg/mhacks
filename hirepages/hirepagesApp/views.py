from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from hirepagesApp.models import User, Looker

#################################################
############## SIGNUP, LOGIN ####################
#################################################

def signup(request):
    if request.method == 'POST':
        roleType=2
        user = User(email=request.POST['email'],
                    password=request.POST['pwd'],
                    firstName=request.POST['firstName']
                    middleName=request.POST['middleName']
                    lastName=request.POST['lastName']
                    dateOfBirth=,
                    workNumber=,
                    cellNumber=,
                    role=roleType)
                         
    else:
        return render(request, 'signup_page.html', Context())

    
def login(request):
    return render(request, 'login_page.html', Context())

    


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
