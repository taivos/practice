from django.db import models
from datetime import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from utils.models import TimeStampedModel


class Author(TimeStampedModel):
    first_name = models.CharField('first_name',        max_length=30)
    last_name = models.CharField('last_name', max_length=30)
    email = models.EmailField(blank=True, null=True)
    birthyear = models.IntegerField('Birth year', null=True)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return '/library/authors/%d/' % (self.id)


class Book(TimeStampedModel):
    title = models.CharField('title', max_length=128)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField('publication_date', default=datetime.now())
    description = models.TextField(null=False, blank=False, default="")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/library/books/%d/' % (self.id)

    def get_authors(self):
        return ', '.join([author.first_name + ' ' + author.last_name for author in self.authors.all()])


class Publisher(TimeStampedModel):
    title = models.CharField('title', max_length=32)
    address = models.TextField('address')
    city = models.CharField('city', max_length=64)
    country = models.CharField('country', max_length=64)
    website = models.URLField('website')

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.website)


class BooksImage(TimeStampedModel):
    book = models.ForeignKey('Book')
    smallImage = models.ImageField(upload_to="photo_small")
    largeImage = models.ImageField(upload_to="photo", null=True, blank=True)
    contType = models.ForeignKey(ContentType)
    objId = models.PositiveIntegerField()
    contentObj = generic.GenericForeignKey("contType", "objId")

    def __unicode__(self):
        return u'%s' % self.book

    def view_smallImage(self):
        return u'<img src="%s"/>' % (self.smallImage.url)
    view_smallImage.allow_tags = True

    def view_largeImage(self):
        return u'<img src="%s"/>' % (self.largeImage.name)
    view_largeImage.allow_tags = True
# Create your models here.
