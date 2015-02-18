from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views import generic
from django.contrib import admin
from django.contrib.auth.decorators import login_required

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
    url(r'^complaints/', include('complaints.urls')),
    url(r'^$', HomeView.as_view()),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.comments.views.comments import post_comment 
from fluent_comments.views import post_comment_ajax

urlpatterns += patterns('', 
    url(r'^comments/post/ajax/$',
        login_required(post_comment_ajax),
        name='comments-post-comment-ajax'),
    url(r'^comments/post/$',
        login_required(post_comment),
        name='comments-post-comment'),
    url(r'^comments/', include('fluent_comments.urls')),
)
