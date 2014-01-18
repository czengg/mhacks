from django.db import models

class User(models.Model):
    recruiterProfile = models.OneToOneField(Recruiter)
    lookerProfile = models.OneToOneField(Looker)

    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30, 
                                    required=False)
    lastName = models.CharField(max_length=30)
    dateOfBirth = models.DateField()
    workNumber = models.CharField(max_length=12)
    cellNumber = 
    RECRUITING = 0
    LOOKING = 1
    ROLE_IN_SYSTEM = (
        (LOOKING, 'Looking'),
        (RECRUITING, 'Recruiting'),
    )
    role = models.PositiveIntegerField(choices=ROLE_IN_SYSTEM,
                                        default=LOOKING)

class Recruiter(models.Model):
    company = models.ForeignKey('Company')

class Company(models.Model):
    description = models.TextField(max_length=200)
    picture = models.ImageField()
    linkToWebsite = models.URLField()

class Position(models.Model):
    description = models.TextField(max_length=200)
    recruiter = models.ForeignKey('Recruiter')
    city = models.CharField(max_length=50)

    FULLTIME = 0
    INTERNSHIP = 1
    TYPE_OF_POSITION = (
        (FULLTIME, 'Looking'),
        (INTERNSHIP, 'Recruiting'),
    )
    role = models.PositiveIntegerField(choices=TYPE_OF_POSITION,
                                        default=FULLTIME)

    STATES = (
      ('AL', 'Alabama'),
      ('AK', 'Alaska'),
      ('AZ', 'Arizona'),
      ('AR', 'Arkansas'),
      ('CA', 'California'),
      ('CO', 'Colorado'),
      ('CT', 'Connecticut'),
      ('DE', 'Delaware'),
      ('DC', 'District of Columbia'),
      ('FL', 'Florida'),
      ('GA', 'Georgia'),
      ('HI', 'Hawaii'),
      ('ID', 'Idaho'),
      ('IL', 'Illinois'),
      ('IN', 'Indiana'),
      ('IA', 'Iowa'),
      ('KS', 'Kansas'),
      ('KY', 'Kentucky'),
      ('LA', 'Louisiana'),
      ('ME', 'Maine'),
      ('MD', 'Maryland'),
      ('MA', 'Massachusetts'),
      ('MI', 'Michigan'),
      ('MN', 'Minnesota'),
      ('MS', 'Mississippi'),
      ('MO', 'Missouri'),
      ('MT', 'Montana'),
      ('NE', 'Nebraska'),
      ('NV', 'Nevada'),
      ('NH', 'New Hampshire'),
      ('NJ', 'New Jersey'),
      ('NM', 'New Mexico'),
      ('NY', 'New York'),
      ('NC', 'North Carolina'),
      ('ND', 'North Dakota'),
      ('OH', 'Ohio'),
      ('OK', 'Oklahoma'),
      ('OR', 'Oregon'),
      ('PA', 'Pennsylvania'),
      ('PR', 'Puerto Rico'),
      ('RI', 'Rhode Island'),
      ('SC', 'South Carolina'),
      ('SD', 'South Dakota'),
      ('TN', 'Tennessee'),
      ('TX', 'Texas'),
      ('UT', 'Utah'),
      ('VT', 'Vermont'),
      ('VA', 'Virginia'),
      ('WA', 'Washington'),
      ('WV', 'West Virginia'),
      ('WI', 'Wisconsin'),
      ('WY', 'Wyoming'),
    )
    state = models.CharField(max_length=2,
                                choices=STATES)



