from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(
        r'actions/create/$',
        views.ActionCreateView.as_view(),
        name='complaints_action_create'
    ),
    url(
        r'^(?P<complaint_slug>[\w-]+)/actions/(?P<slug>[\w-]+)/$', 
        views.ActionDetailView.as_view(),
        name='complaints_action_detail'
    ),
    url(
        r'create/$', 
        views.ComplaintCreateView.as_view(),
        name='complaints_complaint_create'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$', 
        views.ComplaintDetailView.as_view(),
        name='complaints_complaint_detail'
    ),
    url(
        r'^(?P<country_slug>([\w-]+|(all)))/(?P<region_slug>([\w-]+|(all)))/(?P<city_slug>([\w-]+|(all)))/(?P<tag>([\w-]+|(all)))/$', 
        views.ComplaintListView.as_view(),
        name='complaints_complaint_list'
    ),
)
