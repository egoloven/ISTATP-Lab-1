from import_export import resources
from .models import Person, Film

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person

class FilmResource(resources.ModelResource):
    class Meta:
        model = Film