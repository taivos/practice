from django.db import models
from library.models import Book
from utils.models import TimeStampedModel

# Create your models here.


class Customer(TimeStampedModel):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    address = models.TextField()
    email = models.EmailField(null=True)

    def __unicode(self):
        return u'%s %s' % (self.firstName, self.lastName)


class Order(TimeStampedModel):
    itemid = models.ForeignKey(Book)
    create = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField()
    customer = models.ForeignKey(Customer)

    def __unicode(self):
        return self.itemid
