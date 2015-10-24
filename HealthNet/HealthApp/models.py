from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from abc import ABCMeta, abstractclassmethod
"""
The models.py is essentially where objects are declared. Currently, It holds the
PatientProfile object and the logItem object. These objects are most always referenced
in the views. In each class, fields are declared by giving the name followed by the type
of input field. Many of the models have a OneToOne link to another model. ManyToOne,
OneToMany, and ManyToMany are also other types of multiplicities allowed. These link the models.
"""

STATE_CHOICES = (
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

SUPPORTED_INSURANCE = (
    ('ExampleKey', 'ExampleValue')
)

MEDICINE_CATEGORIES = ()

#This is used to limit the entry boxes to 50 characters
MAX_LENGTH = 50

class InsuranceInfo(models.Model):
    provider = models.CharField(choices=SUPPORTED_INSURANCE)
    policyNumber = models.CharField(max_length=MAX_LENGTH)
    groupNumber = models.CharField(max_length=MAX_LENGTH)
    policyExpirationDate = models.DateField()
    premiumAmount = models.CharField(max_length=MAX_LENGTH)
    POLICY_TYPE = (('Primary', 'Primary'),('Secondary','Secondary'))
    policyType = models.CharField(choices=POLICY_TYPE)

class MedicalInfo(models.Model):
    tuberculosis = models.BooleanField(default=False)
    influenza = models.BooleanField(default=False)
    rheumatic = models.BooleanField(default=False)
    whoopingCough = models.BooleanField(default=False)
    tonsillitis = models.BooleanField(default=False)
    measles = models.BooleanField(default=False)
    mumps = models.BooleanField(default=False)
    frequentColds = models.BooleanField(default=False)
    germanMeasles = models.BooleanField(default=False)
    scarletFever = models.BooleanField(default=False)
    scarlatina = models.BooleanField(default=False)
    diphtheria = models.BooleanField(default=False)
    polio = models.BooleanField(default=False)
    chickenpox = models.BooleanField(default=False)
    coxsackie = models.BooleanField(default=False)
    pneumonia = models.BooleanField(default=False)
    highBloodPressure = models.BooleanField(default=False)
    migraine = models.BooleanField(default=False)
    strokes = models.BooleanField(default=False)
    kidneyDisease = models.BooleanField(default=False)
    arthritis = models.BooleanField(default=False)
    allergy = models.BooleanField(default=False)
    bleeding = models.BooleanField(default=False)
    syphilis = models.BooleanField(default=False)
    anemia = models.BooleanField(default=False)
    obesity = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    #add cancer with multiple selector
    #add diabetes with selector
    #possible fields such as last checkup etc.

class Profile(models.Model):
    firstName = models.CharField()
    middleName = models.CharField(blank=True)
    middleInitial = models.CharField(max_length=1)
    lastName = models.CharField()
    socialSecurity = models.CharField(max_length=9)
    citizen = models.BooleanField(default=True)
    dateOfBirth = models.DateField(blank=True)
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = ((MALE,'Male'),(FEMALE,'Female'),)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES,default=MALE)
    address = models.CharField(max_length=MAX_LENGTH)
    city = models.CharField(max_length=MAX_LENGTH)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=5)
    phoneNumber = models.CharField(max_length=14)


    email = models.EmailField(blank=False)
    #switch to email based login
    #choice of preferred hospital
    #choice of emergency contact info (linked to other patient if already in system)


class Patient(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(Profile, null=True)
    insuranceInfo = models.OneToOneField(InsuranceInfo, null=True)
    medicalInfo = models.OneToOneField(MedicalInfo, null=True)
    preferredHospital = models.ForeignKey(Hospital)
    prescriptions = models.ForeignKey(Prescription)
    doctor = models.ForeignKey(Doctor)
    #setting blank to true means this field will not be required


    def __str__(self):
        return self.user.username
    #custom methods can be defined
    def getName(self):
        return self.profileInfo.firstName + " " + self.profileInfo.lastName

    #def getType(self):
    #    return self.type


class Doctor(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(Profile, null=True)
    #Pertanint Methods here

class Nurse(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(Profile, null=True)
    #Pertanint Methods here

class Admin(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(Profile, null=True)
    #Pertanint Methods here

class Hospital(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=MAX_LENGTH)
    city = models.CharField(max_length=MAX_LENGTH)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=5)

class Prescription:
    #medication
    medicationCategory = models.ForeignKey(choices=MEDICINE_CATEGORIES)
    medication = models.CharField(choices=medicationCategory.choices)
    #strength
    strength = models.CharField(choices=)
    #amount
    amount = models.CharField(choices=)
    #frequnecy
    frequency = models.CharField(choices=)
    #purpose (treatment for?)
    purpose = models.TextField()
    #directions
    directions = models.TextField()
    #comments
    comments = models.TextField()

#class for medication categories that each hold a list of medications



#class Logmanager? with many methods?
    #the logmanager would also keep track of the statistics
    #and viewing/sorting as well as making pretty graphs
    #methods for adding/retrieving logitems and sorting

#classes for the various tests that can be preformed with appropriate fields
#in addition, an accompaning form will need to be created
#all tests classes can inherit from a base test class that the patient will hold
#a list of

class LogItem(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=MAX_LENGTH)
