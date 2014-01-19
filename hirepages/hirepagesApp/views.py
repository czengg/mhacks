from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect

from hirepagesApp.models import User, Looker, Experience, Tag
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
                return HttpResponseRedirect('/createrecruiting')
            else:
                return HttpResponseRedirect('/createlooking')
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
############## SEARCH ###########################
#################################################    

def search(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})
        
    if request.method == 'POST':
        print "hi"
    else:
        form = SearchForm()
        return render(request, 'exploreStart.html', {'form':form})

#################################################
########### LOOKER CRUD #########################
#################################################
 
def createLookingPage(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

    user = User.objects.get(email=request.session["user"])
    print "create looking" 
 
    if request.method == 'POST':
        form = LookerForm(request.POST)
        ExperienceFormSet = formset_factory(ExperienceForm)
        formset = ExperienceFormSet(request.POST)
        
        print "create looking post"        
        if form.is_valid():
            print "valid form"
            cd = form.cleaned_data
            school = cd['school']
            jobType = 0
            #jobType = cd['jobType']
            skills = cd['skills']
            degree = cd['degree']
            major = cd['major']
            looker = Looker(school=school, 
                            jobType=jobType, 
                            degree=degree, 
                            major=major,
                            userProfile=user) 
            looker.save()

            for skill in skills.split(","):
                tag = Tag(tag=skill)
                tag.save()
                looker.tags.add(tag)

            if formset.is_valid():
                for f in formset:
                    if f.is_valid():
                        print "valid form set"
                        cd = f.cleaned_data
                        exp= Experience(startDate=cd['startDate'],
                                        endDate=cd['endDate'], 
                                        position=cd['position'],
                                        company=cd['company'],
                                        description=cd['description'],
                                        lookerId=looker)
                        exp.save()
                        rawTags = cd['tags']
                        for rawTag in rawTags.split(","):
                            tag = Tag(tag=rawTag)
                            tag.save()
                            exp.tags.add(tag)
        else:
            print "not valid son"
            print form.errors
        return render(request, 'createPageLooking.html', {'form':form, 
                                                       'formset':formset})
 
    else:
        print "getting something..."
        if request.method == 'GET':
            print "create looking get"
        form = LookerForm()
        ExperienceFormSet = formset_factory(ExperienceForm)
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

    tags = [rawtag.tag for rawtag in looker.tags.all()]
    ctx['tags'] = ",".join(tags)

    experiences = Experience.objects.filter(lookerId=looker)
    expdict = dict()
    for experience in experiences:
        d = dict()
        d['startDate'] = experience.startDate
        d['endDate'] = experience.endDate
        d['description'] = experience.description
        d['position'] = experience.position
        d['company'] = experience.company
        tags = [rawtag.tag for rawtag in experience.tags.all()]
        d['tags'] = ",".join(tags)
        expdict[experience] = d
    ctx['experiences'] = expdict
    return render(request, 'viewPageLooking.html', ctx)


def updateLookingPage(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

    user = User.objects.get(email=request.session["user"])
    print "user"
    print user
    looker = Looker.objects.get(userProfile=user)
    print "looker"
    print looker   

    print "update looking"  
    if request.method == 'POST':
        print "update looking post"
        form = LookerForm(request.POST)
        ExperienceFormSet = formset_factory(ExperienceForm)
        formset = ExperienceFormSet(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            looker.school = cd['school']
            looker.major = cd['major']
            looker.degree = cd['degree']
            looker.jobType = cd['jobType']
            looker.tags.clear()
            looker.save()
 
            skills = cd['skills']
            for skill in skills.split(","):
                tag = Tag(tag=skill)
                tag.save()
                looker.tags.add(tag)

            oldexps = Experience.objects.filter(lookerId=looker.id)
            for oldexp in oldexps:
                oldexp.delete()

            if formset.is_valid():
                for f in formset:
                    if f.is_valid():
                        cd = f.cleaned_data
                        exp= Experience(startDate=cd['startDate'],
                                        endDate=cd['endDate'], 
                                        position=cd['position'],
                                        company=cd['company'],
                                        description=cd['description'],
                                        lookerId=looker)
                        exp.tags.clear()
                        exp.save()

                        rawTags = cd['tags']
                        for rawTag in rawTags.split(","):
                            tag = Tag(tag=rawTag)
                            tag.save()
                            exp.tags.add(tag)
        
            render(request, 'createPageLooking.html', {'form':form})
        else:
           render(request, 'createPageLooking.html', {'form':form, 
                                                      'error':'Problem updating looker'}) 
    else:
        print "update looking get"
        tags = [rawtag.tag for rawtag in looker.tags.all()]
        form = LookerForm(initial={'school':looker.school, 
                                   'major':looker.major,
                                   'degree':looker.degree,
                                   'jobType':looker.jobType,
                                   'skills':(",".join(tags)),})    
 
        experiences = Experience.objects.filter(lookerId=looker.id)
        count = experiences.count()
        print "count", count, looker.id
        ExperienceFormSet = formset_factory(ExperienceForm, extra=count-1)
        index = 0
       
        exps = []
        for exp in experiences:
            tags = [rawtag.tag for rawtag in exp.tags.all()]
            newExp = {'lookerId':exp.lookerId,
                      'startDate':exp.startDate,
                      'endDate':exp.endDate,
                      'description':exp.description,
                      'position':exp.position,
                      'company':exp.company, 
                      'tags':",".join(tags)}
            exps += [newExp]      

        formset = ExperienceFormSet(initial=exps)
        
        return render(request, 'createPageLooking.html', {'form':form,
                                                        'formset':formset})


def delete_looking_page(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

    user = User.objects.filter(email=request.session["user"])
    looker = Looker.objects.filter(userProfile=user)
    looker.delete() 
    return render(request, 'launch_page.html', Context())


####################################################
########### RECRUITER CRUD #########################
####################################################

def createRecruitingPage(request):
    if "user" not in request.session:
        return render(request, 'errorPage.html', {'error': 'Please log in'})

    user = User.objects.filter(email=request.session["user"])
    print "create recruiting"

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        PositionFormSet = formset_factory(PositionForm)
        formset = PositionFormSet(request.POST)

        print "create recruiting post"  
        if form.is_valid():
            print "valid form"
            cd = form.cleaned_data
            description = cd['description']
            name = cd['name']
            linkToWebsite = cd['linkToWebsite']
            company = Company(name=name,
                            description=description, 
                            linkToWebsite=linkToWebsite)

            if formset.is_valid():
                for f in formset:
                    if f.is_valid():
                        cd = f.cleaned_data
                        pos = Position(description=cd['description'],
                                        city=cd['city'],
                                        role=cd['role'],
                                        state=cd['state'])
                        pos.save()
                        company.save()

                        rawTags = cd['tags']
                        for rawTags in rawTags.split(","):
                            tag = Tag(tag=rawTag)
                            tag.save()
                            pos.tags.add(tag)
        else:
            print "not valid betch"
            print form.errors
        return render(request, 'createPageRecruiting.html', Context())

    else:
        print "getting something something..."
        if request.method == 'GET':
            print "create looking get"
        form = CompanyForm()
        PositionFormSet = formset_factory(PositionForm)
        formset = PositionFormSet()
        return render(request, 'createPageRecruiting.html', {'form':form,
                                                                'formset':formset})






