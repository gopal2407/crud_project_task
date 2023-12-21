from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    GENDER = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6, choices=GENDER)
    address = models.TextField()
    contact_no = PhoneNumberField(region="IN")
    city = models.CharField(max_length=20)
    aadhar_card_no = models.CharField(max_length=12)
    email = models.EmailField()

