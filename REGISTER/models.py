from django.db import models

from django import forms

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


class CUSTOMER(models.Model):
    class ID_TYPES(models.TextChoices):
        WORK_ID = ("1", "Work ID")
        STUDENT_ID = ("2", "Student ID")

    """Model definition for CUSTOMER."""

    # TODO: Define fields here
    MOBILE_NUMBER = models.CharField(max_length=12)
    FIRST_NAME = models.CharField(max_length=30)
    LAST_NAME = models.CharField(max_length=30)
    ID_TYPE = models.CharField(max_length=10, choices=ID_TYPES.choices)
    ID_NUMBER = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=10, choices=Gender.choices, blank=True, null=True
    )
    DOB = models.DateField(blank=True, null=True, verbose_name="Date Of Birth")
    # NATIONAL =

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
