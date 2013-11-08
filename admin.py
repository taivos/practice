from django.contrib import admin
from library.models import *
from django.contrib.contenttypes import generic


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    list_display_links = ('last_name', 'first_name',)
    ordering = ('last_name', 'first_name',)


class BooksImageInline(generic.GenericTabularInline):
    model = BooksImage


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date', 'num', 'get_smallImage', 'get_largeImage', )
    inlines = (BooksImageInline,)
    list_display_links = ('title',)
    list_editable = ('publisher',)
    '''list_filter = ('authors', 'publisher','publication_date')'''
    ordering = ('title',)
    search_fields = ('title',)
    date_hierarchy = 'publication_date'
    fieldsets = (
        (None, {'fields': ('title', 'authors')}),
        ('Output data', {'classes': ('collapse',), 'description': u'About book and publisher', 'fields': ('publisher', 'publication_date'), }))

    def num(self, obj):
        i = 0
        for c in BooksImage.objects.filter(id=obj.id):
            if c.smallImage:
                i += 1
            if c.largeImage:
                i += 1
        return i
    num.allow_tags = True

    def get_smallImage(self, obj):
        link = ""
        for c in BooksImage.objects.filter(id=obj.id):
            link = c.view_smallImage()
        return link
    get_smallImage.allow_tags = True

    def get_largeImage(self, obj):
        link = ""
        for c in BooksImage.objects.filter(id=obj.id):
            link = c.largeImage()
        return link
    get_largeImage.allow_tags = True


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city')
    list_display_links = ('title',)
    ordering = ('title',)
    list_filter = ('country', 'city')
    fieldsets = (
        (None, {'fields': ('title', 'website')}),
        ('Contact information', {'classes': ('collapse',), 'fields': ('country', 'city', 'address'), }),)


class BooksImageAdmin(admin.ModelAdmin):
    list_display = ('book', 'view_smallImage', 'view_largeImage', 'count', )

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BooksImage, BooksImageAdmin)
