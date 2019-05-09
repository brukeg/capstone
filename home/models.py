from django.db import models

class User(models.Model):
    user_handle = models.CharField(max_length=30)
    first_nam = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10)
    ssn = models.CharField(max_length=9)
    dob = models.DateField()
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    crypto_address = models.CharField(max_length=42)
    entity_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.user_handle

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