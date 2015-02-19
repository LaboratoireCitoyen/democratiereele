from django.conf import settings
from django.utils.translation import ugettext as _
from django.db import models
from django.core import urlresolvers

from decision.models import Poll
from autoslug import AutoSlugField
from django_markup.fields import MarkupField
from taggit.managers import TaggableManager


class ComplaintTaggableManager(TaggableManager):
    def get_joining_columns(self, reverse_join=False):
        if reverse_join:
            return (("poll_ptr_id", "object_id"),)
        else:
            return (("object_id", "poll_ptr_id"),)


class Complaint(Poll):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    name = models.CharField(max_length=250)
    slug = AutoSlugField(unique=True, populate_from='name')
    description = models.TextField(blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='complaints')

    city = models.ForeignKey('cities_light.city', 
            blank=True, null=True)
        
    tags = ComplaintTaggableManager()

    class Meta:
        ordering = ('creation_datetime',)

    def get_absolute_url(self):
        return urlresolvers.reverse('complaints_complaint_detail', args=(self.slug,))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Action(Poll):
    complaint = models.ForeignKey(Complaint, related_name='actions')
    name = models.CharField(max_length=250)
    slug = AutoSlugField(unique=True, populate_from='name')
    description = models.TextField(blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return urlresolvers.reverse('complaints_action_detail', 
                args=(self.complaint.slug, self.slug,))
