from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import (
    Layout, Fieldset, HTML, Row, Column, Panel,
    ButtonHolder, ButtonHolderPanel, ButtonGroup, Button, Submit,
    InlineField, InlineJustifiedField,
    SwitchField, InlineSwitchField
)

from threadedcomments.models import ThreadedComment

import rules_light

from .models import Complaint, Action
from .forms import ComplaintForm, ActionForm


def get_comments_flat(obj):
    ctype = ContentType.objects.get_for_model(obj)
    return ThreadedComment.objects.filter(
            content_type=ctype, object_pk=obj.pk).order_by('-submit_date')


@rules_light.class_decorator
class ComplaintCreateView(generic.CreateView):
    model = Complaint
    form_class = ComplaintForm

    def get_form(self, form_class):
        form = super(ComplaintCreateView, self).get_form(form_class)
        form.instance.author = self.request.user
        return form


@rules_light.class_decorator
class ComplaintDetailView(generic.DetailView):
    model = Complaint
    queryset = Complaint.objects.select_related('city', 'city__region', 'city__region__country')

    def get_context_data(self, *args, **kwargs):
        c = super(ComplaintDetailView, self).get_context_data(*args, **kwargs)

        c['action_form'] = ActionForm(
                initial={'complaint': self.object.pk},
                form_action=reverse('complaints_action_create'))
        return c


class ComplaintListView(generic.ListView):
    model = Complaint

    def get_queryset(self):
        q = Complaint.objects.all().select_related()

        city_id = self.kwargs.get('city_id', 'all')
        if city_id != 'all':
            q = q.filter(city__pk=city_id)

        return q


@rules_light.class_decorator
class ActionDetailView(generic.DetailView):
    model = Action


@rules_light.class_decorator
class ActionCreateView(generic.CreateView):
    model = Action
    form_class = ActionForm

    def get_form(self, form_class):
        form = super(ActionCreateView, self).get_form(form_class)
        form.instance.author = self.request.user
        return form
