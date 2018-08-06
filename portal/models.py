from django.db import models
from django.utils import timezone


# Sign up model

class Signup(models.Model):
    username = models.TextField(max_length=30)
    email = models.EmailField
    password = models.CharField
    confirmPassword = models.CharField

    def signup(self):
        self.save()


# user profile model
class Profile(models.Model):
    user_avatar = models.ImageField(height_field="300", width_field="300")
    full_name = models.TextField(max_length="50")
    id_no = models.IntegerField
    email = models.EmailField
    date_of_birth = models.DateField
    gender = models.CharField(max_length=10)
    mobile_no = models.IntegerField
    marital_status = models.TextField(max_length=10)
    postal_address = models.CharField
    education_level = models.TextField(max_length="100")
    field_of_study = models.TextField(max_length="100")
    profession = models.TextField(max_length="100")
    admission_date = models.DateField
    volunteer_type = models.CharField(max_length="50")
    committee_type = models.CharField(max_length="30")
    position_held_from = models.DateField
    position_held_to = models.DateField

    @property
    def user(self):
        return self.Profile
        self.save()


# news updates model

class Updates(models.Model):
    title = models.TextField(max_length="15")
    text = models.TextField
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()


# Membership payment model

class Payment(models.Model):
    membership_type = models.TextField(max_length="50")
    payment_description = models.TextField(max_length="30")
    amount = models.IntegerField
    payment_date = models.DateField

    def membership(self):
        return self.Payment
        self.save()
