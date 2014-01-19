from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.forms.formsets import formset_factory

from hirepagesApp.models import User, Looker, Experience
from hirepagesApp.forms import *

#################################################
############## SIGNUP, LOGIN ####################
#################################################

def signup(request):
    print "in signup"
    if request.method == 'POST':
        print "post method"
        form = SignupForm(request.POST)
        if form.is_valid():
            print "valid form"
            cd = form.cleaned_data
            user = User(email=cd['email'],
                    password=cd['password'],
                    firstName=cd['firstName'],
                    middleName=cd['middleName'],
                    lastName=cd['lastName'],
                    dateOfBirth=cd['dateOfBirth'],
                    workNumber=cd['workNumber'],
                    cellNumber=cd['cellNumber'],
                    role=cd['role'],)
            user.save()
            request.session["user"] = cd['email']

            RECRUITING = 0
            LOOKING = 1

            if cd['role'] == RECRUITING:
                return render(request, 'createPageRecruiting.html', Context())
            elif cd['role'] == LOOKING:
                return render(request, 'createPageLooking.html', Context())
        else:
            print "invalid form"
            print form.errors
            return render(request, 'signup.html', {'form': form})
    else:
        print "get method"
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            pwd = cd['password']
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
    if "user" in request.session: 
        del request.session["user"]
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

    


#################################################
########### LOOKER CRUD #########################
#################################################
 
def createLookingPage(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

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
        return render(request, 'createPageLooking.html', Context())
 
    else:
        form = LookerForm()
        ExperienceFormSet = formset_factory(ExperienceForm())
        formset = ExperienceFormSet()
        return render(request, 'createPageLooking.html', {'form':form, 
                                                          'formset':formset})


def read_looking_page(request):
    ctx = Context()
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

    user = User.objects.filter(email=request.session["user"])
    looker = Looker.objects.filter(userProfile=user)
    ctx['school'] = looker.school
    ctx['jobType'] = looker.jobType
    ctx['active'] = looker.active
    ctx['tags'] = looker.tags.all() 
    return render(request, 'viewPageLooking.html', ctx)


def update_looking_page(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

    user = User.objects.filter(email=request.session["user"])
    
    if request.method == 'POST':
        form = LookerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    
    return render(request, 'createPageLooking.html', ctx)


def delete_looking_page(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

    user = User.objects.filter(email=request.session["user"])
    looker = Looker.objects.filter(userProfile=user)
    looker.delete() 
    return render(request, 'launch_page.html', Context())


