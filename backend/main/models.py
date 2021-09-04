from django.db import models
from django.db.models.base import ModelBase

# Create your models here.


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.email)

    def to_dict(self):
        subscribe_dict = {}
        subscribe_dict['email'] = self.email 

        return subscribe_dict   