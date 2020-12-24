from django.db import models

# Create your models here.


class Userform(models.Model):

    STATE_CHOICES = (
        ('kerla','KERLA'),
        ('tamilnadu','TAMILNADU'),
    )




    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    regno = models.CharField(max_length=200,null=True)
    clg = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200, choices=STATE_CHOICES,null=True)
    zipcode = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.first_name +' '+self.last_name