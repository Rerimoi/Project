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
class UserProfile(models.Model):
    user_avatar = models.ImageField(height_field=100, width_field=100)
    full_name = models.CharField(max_length=50)
    id_no = models.IntegerField
    email = models.EmailField
    date_of_birth = models.DateField
    gender = models.CharField(max_length=10)
    mobile_no = models.IntegerField
    marital_status = models.CharField(max_length=10)
    postal_address = models.CharField
    education_level = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    admission_date = models.DateField(blank=True, null=True)
    volunteer_type = models.CharField(max_length=50)
    committee_type = models.CharField(max_length=50)
    position_held_from = models.DateField(blank=True, null=True)
    position_held_to = models.DateField(blank=True, null=True)

    def user(self):
        self.admission_date = timezone
        self.position_held_from = timezone
        self.position_held_to = timezone
        self.save()


# news updates model

class Update(models.Model):
    title = models.CharField(max_length=15)
    body = models.TextField
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()


# Membership payment model

class Payment(models.Model):
    membership_type = models.CharField(max_length=50)
    payment_description = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    payment_date = models.DateField(blank=True, null=True)

    def membership(self):
        self.payment_date = timezone.now()
        self.save()
        return "KSh" + self.amount
