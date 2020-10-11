from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Userprofile(models.Model):
    name = models.CharField(default='', max_length=60)
    email = models.CharField(default='', max_length=50)
    country = models.CharField(default=0,max_length=100)
    books_name = models.CharField(default='', max_length=60)
    isbn = models.CharField(default='', max_length=60)
    author = models.CharField(default='', max_length=60)
    def create_profile(sender,**kwargs):
        if kwargs['created']:
            userprofile = Userprofile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile,sender=User)