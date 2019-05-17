from django.db import models
from django.utils import timezone

class User_entity(models.Model):
    country = models.CharField(max_length=30, default='US')             # Required: US is the only supported country
    user_handle = models.CharField(max_length=30)                       # required: the end users Sila ENS handle
    first_name = models.CharField(max_length=30)                        # required: first name of the end user
    last_name = models.CharField(max_length=30)                         # required: last name of the end user
    street_address_1 = models.CharField(max_length=60)                  # required: physical address of end users
    city = models.CharField(max_length=30)                              # required: the end users city
    state = models.CharField(max_length=2)                              # required: the users state
    postal_code = models.CharField(max_length=10)                       # required: USPS zip code for the end users
    identity_value = models.CharField(max_length=9)                     # required: users social security number
    birthdate = models.DateField()                                      # required: users date of birth
    email = models.EmailField(max_length=100)                           # required: email address
    phone = models.CharField(max_length=10)                             # required: users US phone number
    crypto_address = models.CharField(max_length=42)                    # required: users ethereum address
    entity_name = models.CharField(max_length=100)                      # required: users full name
    private_key = models.CharField(max_length=256)                      # required: encrypted private key for address
    created_date = models.DateTimeField(default=timezone.now)           # date user is created

    def __str__(self):
        """String for representing the Model object."""
        return self.user_handle

class Developer(models.Model):
    dev_handle = models.CharField(max_length=256)
    crypto_address = models.CharField(max_length=42)
    private_key = models.CharField(max_length=256)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """String for representing the Model object."""
        return self.dev_handle

class SilaTransaction(models.Model):
    issue_amount = models.IntegerField()
    transfer_amount = models.IntegerField()
    redeem_amount = models.IntegerField()

class Transactions(models.Model):
    pass
    # transaction_object =

class Response(models.Model):
    pass
    # response_object =