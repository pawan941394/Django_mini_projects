from django.db import models

# Create your models here.
class Contact(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    desc =  models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True ,blank=True)

    def __str__(self):
        return  self.name


