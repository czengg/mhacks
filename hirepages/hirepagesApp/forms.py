from django import forms

class SignupForm(forms.Form):
    email = forms.CharField(max_length=30)    
    password = forms.CharField(max_length=20)
    firstName = forms.CharField(max_length=30)
    middleName = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)
    dateOfBirth = forms.DateField()
    workNumber = forms.CharField(max_length=12)
    cellNumber = forms.CharField(max_length=12)

    RECRUITING = 0
    LOOKING = 1
    ROLE_IN_SYSTEM = ( (LOOKING, 'Looking'), (RECRUITING, 'Recruiting'),)
    role = forms.IntegerField()
