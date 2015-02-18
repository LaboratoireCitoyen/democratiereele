from django.views import generic
from django.db.models import Q

from taggit.models import Tag
from complaints.models import Complaint, Action
from django.contrib.comments.models import Comment
from cities_light.models import City


class AutocompleteView(generic.TemplateView):
    template_name = 'autocomplete.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AutocompleteView, self).get_context_data(*args, **kwargs)

        q = self.request.GET.get('q', '')

        context['complaints'] = Complaint.objects.filter(
            Q(name__icontains=q)|Q(description__icontains=q))[:7]
        context['actions'] = Action.objects.filter(
            Q(name__icontains=q)|Q(description__icontains=q))[:7]
        context['tags'] = Tag.objects.filter(name__icontains=q)[:7]

        return context


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        context['complaints'] = Complaint.objects.all()[:7]
        context['actions'] = Action.objects.all()[:7]
        context['comments'] = Comment.objects.all()[:7]
        context['cities'] = City.objects.exclude(complaint=None)

        return context
