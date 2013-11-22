from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^library/(?P<sub>(books){0,1}?)$', 'library.views.books'),
    url(r'^library/books/(?P<sub>\d+?)/$', 'library.views.book'),
    url(r'^library/authors/?$', 'library.views.authors'),
    url(r'^library/authors/(?P<sub>\d+?)/$', 'library.views.author'),
    url(r'^orders/$', CustomersList.as_view(), name='order_list.html'),
    url(r'^orders_list/(?P<pk>\d+)/$', CustomerDetails.as_view(), name='customer.html'),
    url(r'^registration/$', 'bookslibrary.registration.views.registrate'),
    url(r'^login/$', 'bookslibrary.registration.views.log_in'),
    # url(r'^$', 'bookslibrary.views.home', name='home'),
    # url(r'^bookslibrary/', include('bookslibrary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
