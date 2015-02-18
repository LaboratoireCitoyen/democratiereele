from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views import generic
from django.contrib import admin

from .views import AutocompleteView, HomeView

import rules_light
rules_light.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('account.urls')),
    url(r'^decision/', include('decision.urls')),
    url(r'^autocomplete/$', AutocompleteView.as_view(),
        name='autocomplete'),
    url(r'^autocomplete-light/', include('autocomplete_light.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^complaints/', include('complaints.urls')),
    url(r'^$', HomeView.as_view()),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
