from django.views import generic
from django.core.urlresolvers import reverse
from django import http

import rules_light

from cities_light.models import City, Region, Country

from .models import Complaint, Action
from .forms import ComplaintForm, ActionForm


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
    queryset = Complaint.objects.select_related('city', 'city__region',
            'city__region__country')

    def get_context_data(self, *args, **kwargs):
        c = super(ComplaintDetailView, self).get_context_data(*args, **kwargs)

        c['action_form'] = ActionForm(
                initial={'complaint': self.object.pk},
                form_action=reverse('complaints_action_create'))
        return c


class ComplaintListView(generic.ListView):
    model = Complaint
    paginate_by = 10

    def get_queryset(self):
        q = Complaint.objects.all().select_related('city', 'city__region',
                'city__region__country').prefetch_related('tags')

        self.country_slug = self.kwargs.get('country_slug', 'all')
        self.region_slug = self.kwargs.get('region_slug', 'all')
        self.city_slug = self.kwargs.get('city_slug', 'all')
        self.tag = self.kwargs.get('tag', 'all')

        if self.country_slug != 'all':
            q = q.filter(city__region__country__slug=self.country_slug)

        if self.region_slug != 'all':
            q = q.filter(city__region__slug=self.region_slug)

        if self.city_slug != 'all':
            q = q.filter(city__slug=self.city_slug)

        if self.tag != 'all':
            q = q.filter(tags__name__in=[self.tag])

        return q

    def get_context_data(self, *args, **kwargs):
        c = super(ComplaintListView, self).get_context_data(*args, **kwargs)
        
        try:
            self.populate_context(c)
        except (City.DoesNotExist, Region.DoesNotExist, Country.DoesNotExist):
            raise http.Http404()

        return c

    def populate_context(self, context):
        if self.city_slug != 'all':
            context['city'] = City.objects.get(slug=self.city_slug,
                region__slug=self.region_slug, 
                region__country__slug=self.country_slug)
            context['region'] = context['city'].region
            context['country'] = context['city'].region.country

        elif self.region_slug != 'all':
            context['region'] = Region.objects.get(slug=self.region_slug,
                    country__slug=self.country_slug)
            context['country'] = context['region'].country

        elif self.country_slug != 'all':
            context['country'] = Country.objects.get(slug=self.country_slug)

        if self.tag != 'all':
            context['tag'] = self.tag


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
