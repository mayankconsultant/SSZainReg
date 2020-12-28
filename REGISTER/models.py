from django.db import models

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Create your models here.

# UN_ID=(3,'UN ID'),
# POLICE_MILITARY_ID=(4,'Military,Polica,SPLM'),
# TRIBAL_ID=(5,'Tribal Chiefs Cert.'),
# NATIONAL_ID=(6,'National ID'),
# PASSPORT=(7,'Passport'),
# VOTING_ID=(8,'Voting Card'),
# DRIVING_LICENCE_ID=(9,'Driving License')


class Gender(models.TextChoices):
    MALE = ("MALE", "MALE")
    FEMALE = ("FEMALE", "FEMALE")


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class State(models.Model):
    """Model definition for STATE."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,blank=True, null=True)

    class Meta:
        """Meta definition for STATE."""

        verbose_name = "STATE"
        verbose_name_plural = "STATES"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class City(models.Model):
    """Model definition for STATE."""

    # TODO: Define fields here
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.SET_NULL,blank=True, null=True)

    class Meta:
        """Meta definition for STATE."""

        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
            return self.name

    def __unicode__(self):
            return self.name

class CUSTOMER(models.Model):
    class ID_TYPES(models.TextChoices):
        WORK_ID = ("1", "Work ID")
        STUDENT_ID = ("2", "Student ID")
        UN_ID=(3,'UN ID'),
        POLICE_MILITARY_ID=(4,'Military,Polica,SPLM'),
        TRIBAL_ID=(5,'Tribal Chiefs Cert.'),
        NATIONAL_ID=(6,'National ID'),
        PASSPORT=(7,'Passport'),
        VOTING_ID=(8,'Voting Card'),
        DRIVING_LICENCE_ID=(9,'Driving License')

    """Model definition for CUSTOMER."""

    # TODO: Define fields here
    MOBILE_NUMBER = models.CharField(max_length=12)
    FIRST_NAME = models.CharField(max_length=30)
    LAST_NAME = models.CharField(max_length=30)
    ID_TYPE = models.CharField(max_length=30, choices=ID_TYPES.choices)
    ID_NUMBER = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=10, choices=Gender.choices,default=Gender.MALE
    )
    DOB = models.DateField(blank=True, null=True, verbose_name="Date Of Birth")
    NATIONAL =models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True,null=True)
    ADDRESS = models.CharField(max_length=50, blank=True,null=True,
                              )
    STATE =models.ForeignKey(State,on_delete=models.DO_NOTHING,blank=True,null=True)
    CITY = models.ForeignKey(City, on_delete=models.DO_NOTHING,blank=True,null=True)
    PAYAM = models.CharField(max_length=50,blank=True,null=True)
    BOMA = models.CharField(max_length=50,blank=True,null=True)

    confirmed=models.BooleanField(verbose_name="I confirm all details provided are true")

    class Meta:
        """Meta definition for CUSTOMER."""

        verbose_name = "CUSTOMER"
        verbose_name_plural = "CUSTOMERS"

    def __str__(self):
        """Unicode representation of CUSTOMER."""
        return self.msisdn + " " + self.first_name + self.last_name


class CustomerForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = CUSTOMER
        fields = "__all__"
        widgets = {
            'gender': forms.RadioSelect,
            'DOB': forms.DateInput(format=('%d/%b/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
        'MOBILE_NUMBER',
        Row(
                Column('FIRST_NAME', css_class='form-group col-md-6 mb-0'),
                Column('LAST_NAME', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        Row(
                Column('ID_TYPE', css_class='form-group col-md-6 mb-0'),
                Column('ID_NUMBER', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        Row(
                Column('gender', css_class='form-group col-md-6 mb-0'),
                Column('DOB', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        'ADDRESS',
        Row(
                Column('NATIONAL', css_class='form-group col-md-4 mb-0'),
                Column('STATE', css_class='form-group col-md-4 mb-0'),
                Column('CITY', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        Row(
                Column('PAYAM', css_class='form-group col-md-6 mb-0'),
                Column('BOMA', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
        Column('confirmed', css_class='form-group col-md-12 mt-3 mb-5 '),

        Submit('submit', 'Confirmed')
        )