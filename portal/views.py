from django.shortcuts import render
# from django.db import models
# from .models import Signup


# Create your views here.
def start_page(request):
    return render(request, 'dashboard/home.html', {})


# def save(self, *args, **kwargs):
#     if self.email is not None and self.email.strip() == "":
#         self.email = None
#     models.Model.save(self, *args, **kwargs)
