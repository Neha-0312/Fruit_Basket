from django.db import models

# Create your models here.
class Apples(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')

class Oranges(models.Model):
    name1=models.CharField(max_length=100)
    price1=models.IntegerField()
    desc1=models.TextField()
    img1=models.ImageField(upload_to='pics')


class Grapes(models.Model):
    name2=models.CharField(max_length=100)
    price2=models.IntegerField()
    desc2=models.TextField()
    img2=models.ImageField(upload_to='pics')



class usercontact(models.Model):
    name3=models.CharField(max_length=100)
    email3=models.EmailField(max_length=254, blank=False)
    comment3=models.TextField()
