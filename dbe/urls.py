from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cal.views',
    # Examples:
    # url(r'^$', 'dbe.views.home', name='home'),
    # url(r'^dbe/', include('dbe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.urls')),
    (r"^month/(\d+)/(\d+)/(prev|next)/", "month"),
    (r"^month/(\d+)/(\d+)/", "month"),
    (r"^month$", "month"),
    (r"^day/(\d+)/(\d+)/(\d+)/", "day"),
    (r"^settings/", "settings"),
    (r"^(\d+)/", "main"),
    (r"", "main"),

)
