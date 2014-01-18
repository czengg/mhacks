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
            request.session["user"] = cd['email']
            return render(request, 'login.html', Context())
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            pwd = cd['pwd']
            try:
                user = User.objects.get(email=email)
                if (pwd != user.password):
                    print "Incorrect password"
                    return render(request, 'login.html', {'form': form})
                else:  
                    request.session["user"] = email 
                    return render(request, 'explore_start.html', Context())
            except User.DoesNotExist:
                print "User does not exist. Please create account"
           
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    del request.session["user"]
    return render(reuqest, "login.html", Context())

    


#################################################
########### LOOKER CRUD #########################
#################################################
 
def create_looking_page(request):
    if "user" not in request.session:
        return render(request, 'error_page.html', {'error': 'Please log in'})

    user = User.objects.filter(email=request.session["user"])
    
    if request.method == 'POST':
        form = LookerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            school = cd['school']
            jobType = cd['jobType']
            active = cd['active']
            skills = cd['skills']
            looker = Looker(school=school, 
                            jobType=jobType, 
                            active=active, 
                            userProfile=user) 
            looker.save()

            for skill in skills.split(","):
                tag = Tag(tag=skill)
                tag.save()
                looker.tags.add(tag)
        return render(request, 'view_looking_page.html', Context())
 
    else:
        form = LookerForm()
        return render(request, 'edit_looking_page.html', {'form':form})


def read_looking_page(request):
    ctx = Context()
    if "user" not in request.session:
        return render(request, 'error_page.html', {'error': 'Please log in'})

    user = User.objects.filter(email=request.session["user"])

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


