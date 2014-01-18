from django.db import models

# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=50)


class Looker(models.Model):
    INTERNSHIP = 0
    FULLTIME = 1
    JOBTYPECHOICES = ((INTERNSHIP, 'Internship'), (FULLTIME, 'FullTime'),)

    school = models.CharField(max_length=50)
    jobType = models.IntegerField(choices=JOBTYPECHOICES, default=FULLTIME)
    active = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)


class Experience(models.Model):
    lookerId= models.ForeignKey(Looker)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField(max_length=200)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)


