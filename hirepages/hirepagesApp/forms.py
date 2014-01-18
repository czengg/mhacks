from django import forms
from django.forms import extras

class SignupForm(forms.Form):
    email = forms.CharField(max_length=30)    
    password = forms.CharField(max_length=20)
    firstName = forms.CharField(max_length=30)
    middleName = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)
    dateOfBirth = forms.DateField(widget=extras.SelectDateWidget(years=range(1999,1939,-1)))
    workNumber = forms.CharField(max_length=12)
    cellNumber = forms.CharField(max_length=12)

    RECRUITING = 0
    LOOKING = 1
    ROLE_IN_SYSTEM = ( (LOOKING, 'Looking'), (RECRUITING, 'Recruiting'),)
    role = forms.ChoiceField(widget=forms.RadioSelect,
                                        choices=ROLE_IN_SYSTEM)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)

class LookerForm(forms.Form):
    school = forms.CharField(max_length=50)

    INTERNSHIP = 0
    FULLTIME = 1
    JOBTYPECHOICES = ((INTERNSHIP, 'Internship'), (FULLTIME, 'FullTime'),)
    jobType = forms.ChoiceField(widget=forms.RadioSelect,
                                            choices=JOBTYPECHOICES)
    active = forms.BooleanField()
    skills = forms.CharField(max_length=100)


class ExperienceForm(forms.Form):
    startDate = forms.DateField()
    endDate = forms.DateField()
    position = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=200)
    tags = forms.CharField(max_length=100, widget=forms.Textarea)


