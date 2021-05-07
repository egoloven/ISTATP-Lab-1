from django.contrib import admin
from .models import Gender, Person, Genre, Studio, Film, Role, RoleType, FilmType, FilmToGenre, FilmToStudio
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin

admin.site.register(Gender)
# admin.site.register(Person)
admin.site.register(Genre)
admin.site.register(Studio)
# admin.site.register(Film)
admin.site.register(Role)
admin.site.register(RoleType)
admin.site.register(FilmType)
admin.site.register(FilmToGenre)
admin.site.register(FilmToStudio)

@admin.register(Person)
class PersonAdmin(ExportActionMixin, ImportExportModelAdmin):
    list_display = ('person_full_name', 'person_date_of_birth', 'person_date_of_death', 'gender')
    actions = [ExportActionMixin.export_admin_action]

@admin.register(Film)
class FilmAdmin(ExportActionMixin, ImportExportModelAdmin):
    list_display = ('film_name', 'film_description', 'film_duration', 'filmtype')
    actions = [ExportActionMixin.export_admin_action]