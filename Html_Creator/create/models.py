from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class  create(models.Model):
    body = RichTextField(blank=True, null=True)


