import autocomplete_light

from taggit.models import Tag
from cities_light.models import City

autocomplete_light.register(City)
autocomplete_light.register(Tag)
