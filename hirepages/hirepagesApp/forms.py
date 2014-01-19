from django import forms
from django.forms import extras
from hirepagesApp.models import User, Looker
from django.core.exceptions import ValidationError

def validate_username_unique(value):
    '''Custom validator for user uniqueness.'''
    if User.objects.filter(email=value).exists():
        raise ValidationError(u'Sorry, %s already has an account!' % value)

class SignupForm(forms.Form):
    email = forms.CharField(max_length=30,
                                validators=[validate_username_unique])    
    password = forms.CharField(max_length=20, 
                                widget=forms.PasswordInput())
    firstName = forms.CharField(max_length=30)
    middleName = forms.CharField(max_length=30,
                                    required=False)
    lastName = forms.CharField(max_length=30)
    dateOfBirth = forms.DateField(widget=extras.SelectDateWidget(years=range(1999,1939,-1)))
    workNumber = forms.CharField(max_length=12,
                                    required=False)
    cellNumber = forms.CharField(max_length=12,
                                    required=False)

    RECRUITING = 0
    LOOKING = 1
    ROLE_IN_SYSTEM = ( (LOOKING, 'Looking'), (RECRUITING, 'Recruiting'),)
    role = forms.ChoiceField(widget=forms.RadioSelect,
                                        choices=ROLE_IN_SYSTEM)

    def role_choices(self):
        """
        Returns role's widget's default renderer, which can be used to 
            render the choices of a RadioSelect widget.
        """
        field = self['role']
        widget = field.field.widget

        attrs = {}
        auto_id = field.auto_id
        if auto_id and 'id' not in widget.attrs:
            attrs['id'] = auto_id

        name = field.html_name

        return widget.get_renderer(name, field.value(), attrs=attrs)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=30)
    password=forms.CharField(max_length=20,
                                widget=forms.PasswordInput())

class LookerForm(forms.Form):
    school = forms.CharField(max_length=50)

    INTERNSHIP = 0
    FULLTIME = 1
    JOBTYPECHOICES = ((INTERNSHIP, 'Internship'), (FULLTIME, 'FullTime'),)
    jobType = forms.ChoiceField(widget=forms.RadioSelect,
                                            choices=JOBTYPECHOICES)
    active = forms.BooleanField()
    skills = forms.CharField(max_length=100,
                                widget=forms.Textarea)


class ExperienceForm(forms.Form):
    startDate = forms.DateField()
    endDate = forms.DateField()
    position = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=200)
    tags = forms.CharField(max_length=100, widget=forms.Textarea)


