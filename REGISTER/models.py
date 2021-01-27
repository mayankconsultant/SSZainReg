from django.db import models

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from django.core.exceptions import ValidationError

from PIL import Image

from django_countries.fields import CountryField

# Create your models here.

# UN_ID=(3,'UN ID'),
# POLICE_MILITARY_ID=(4,'Military,Polica,SPLM'),
# TRIBAL_ID=(5,'Tribal Chiefs Cert.'),
# NATIONAL_ID=(6,'National ID'),
# PASSPORT=(7,'Passport'),
# VOTING_ID=(8,'Voting Card'),
# DRIVING_LICENCE_ID=(9,'Driving License')

def customer_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'cust_{0}/{1}'.format(instance.MOBILE_NUMBER, filename)


class states(models.Model):
    name= models.CharField(max_length=100)


    def __str__(self):
        # return str(self.name).upper()
        return  self.name

    # def __unicode__(self):
    #         return str(self.name).upper()

class county (models.Model):
    name =models.CharField(max_length=100)
    states= models.ForeignKey(states,on_delete=models.DO_NOTHING)

    def __str__(self):
        return  self.name



class payam (models.Model):
    name =models.CharField(max_length=100)
    county = models.ForeignKey(county,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name



class Locations(models.Model):
    STATE =models.CharField(max_length=100)
    COUNTY  =models.CharField(max_length=100)
    PAYAM =models.CharField(max_length=100)
    BOMA =models.CharField(max_length=100, blank=True,null=True)

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
        UN_ID=("3",'UN ID'),
        POLICE_MILITARY_ID=("4",'Military,Polica,SPLM'),
        TRIBAL_ID=("5",'Tribal Chiefs Cert.'),
        NATIONAL_ID=("6",'National ID'),
        PASSPORT=("7",'Passport'),
        VOTING_ID=("8",'Voting Card'),
        DRIVING_LICENCE_ID=("9",'Driving License')

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
    COUNTRY =CountryField()
    ADDRESS = models.CharField(max_length=50, blank=True,null=True,
                              )
    STATE =models.ForeignKey(states,on_delete=models.DO_NOTHING)
    CITY = models.CharField(max_length=100)
    COUNTY = models.ForeignKey(county,on_delete=models.DO_NOTHING)
    PAYAM = models.ForeignKey(payam,on_delete=models.DO_NOTHING)
    BOMA = models.CharField(max_length=50,blank=True,null=True)
    ID_FILE =models.ImageField(upload_to = customer_directory_path)
    CREATED_DATE = models.DateField(auto_now_add=True)





    class Meta:
        """Meta definition for CUSTOMER."""

        verbose_name = "CUSTOMER"
        verbose_name_plural = "CUSTOMERS"

    def __str__(self):
        """Unicode representation of CUSTOMER."""
        return self.MOBILE_NUMBER + " " + self.FIRST_NAME + self.LAST_NAME

    def save(self, *args, **kwargs):
        super(CUSTOMER, self).save(*args, **kwargs)

        img = Image.open(self.ID_FILE.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.ID_FILE.path)

