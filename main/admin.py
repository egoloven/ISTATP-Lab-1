from django.contrib import admin
from .models import Gender, Person, Genre, Studio, Film, Role, RoleType, FilmType, FilmToGenre, FilmToStudio


admin.site.register(Gender)
admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Film)
admin.site.register(Role)
admin.site.register(RoleType)
admin.site.register(FilmType)
admin.site.register(FilmToGenre)
admin.site.register(FilmToStudio)