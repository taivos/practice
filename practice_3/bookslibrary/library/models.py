from django.db import models
from datetime import datetime


class Author(models.Model):
    first_name = models.CharField('first_name',        max_length=30)
    last_name = models.CharField('last_name', max_length=30)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return '/library/authors/%d/' % (self.id)


class Book(models.Model):
    title = models.CharField('title', max_length=128)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField('publication_date', default=datetime.now())

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/library/books/%d/' % (self.id)

    def get_authors(self):
        return ', '.join([author.first_name + ' ' + author.last_name for author in self.authors.all()])


class Publisher(models.Model):
    title = models.CharField('title', max_length=32)
    address = models.TextField('address')
    city = models.CharField('city', max_length=64)
    country = models.CharField('country', max_length=64)
    website = models.URLField('website')

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.website)
# Create your models here.
