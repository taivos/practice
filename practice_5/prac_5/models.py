from django.db import models
from datetime import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType


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


class BooksImage(models.Model):
    book = models.ForeignKey(Book)
    smallImage = models.ImageField(upload_to="img")
    largeImage = models.ImageField(upload_to="smallimg", null=True, blank=True)
    cont = models.ForeignKey(ContentType)
    objNum = models.PositiveIntegerField()
    contObj = generic.GenericForeignKey("cont", "objNum")

    def __unicode__(self):
        return u'%s' % self.book

    def count(self):
        num = 0
        if self.smallImage:
            num += 1
        if self.largeImage:
            num += 1
        return(num)

    def view_smallImage(self):
        return u'<img src="%s"/>' % (self.smallImage.url)
    view_smallImage.allow_tags = True

    def view_largeImage(self):
        return u'<img src="%s"/>' % (self.largeImage.name)
    view_largeImage.allow_tags = True
# Create your models here.
