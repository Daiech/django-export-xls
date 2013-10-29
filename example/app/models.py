from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(User, blank=True, null=True)
    published = models.DateField('Published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
            blank=True)

    def __unicode__(self):
        return self.name