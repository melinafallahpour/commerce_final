from email.policy import default
from xml.dom import minidom
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    owner = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    category = models.CharField(max_length=64)
    link = models.CharField(max_length=128,default=None,blank=True,null=True)
    time = models.CharField(max_length=64)

class Bid(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    listingid = models.PositiveIntegerField(default=0)
    bid =models.PositiveIntegerField(default=0)

class Comment(models.Model):
    user = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    comment = models.TextField()
    listingid = models.PositiveIntegerField(default=0)


class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    listingid = models.PositiveIntegerField(default=0)

class Closedbid(models.Model):
    owner = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    listingid = models.PositiveIntegerField(default=0)
    winprice = models.PositiveIntegerField(default=0)


class Alllisting(models.Model):
    listingid = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=128,default=None,blank=True,null=True)