from django.db import models


class Gender(models.Model):
    gender_name = models.CharField(
        'gender name',
        max_length=20
    )
    gender_description = models.CharField(
        'gender description',
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.gender_name

class Genre(models.Model):
    genre_name = models.CharField(
        'genre name',
        max_length=20
    )
    gender_description = models.CharField(
        'genre description',
        max_length=100,
        blank=True,
        null=True
    )

class Person(models.Model):
    person_full_name = models.CharField(
        'full name',
        max_length=60
    )
    person_date_of_birth = models.DateField()
    person_date_of_death = models.DateField(blank=True, null=True)
    gender = models.ForeignKey(
        Gender,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.person_full_name

# Studious class definition

class Studio(models.Model):
    studio_name = models.CharField(
        'studio name',
        max_length=60
    )
    studio_description = models.CharField(
        'studio description',
        max_length=200,
        blank=True,
        null=True
    )
    studio_foundation_date = models.DateField()
    studio_dissolution_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.studio_name

class FilmType(models.Model):
    filmtype_name = models.CharField(
        'film-type name',
        max_length=20
    )
    filmtype_description = models.CharField(
        'film-type description',
        max_length=80,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.filmtype_name

class Film(models.Model):
    film_name = models.CharField(
        'film name',
        max_length=50
    )
    film_description = models.CharField(
        'film description',
        max_length=150,
        blank=True,
        null=True
    )
    film_duration = models.DurationField()
    filmtype = models.ForeignKey(
        FilmType,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.film_name

class RoleType(models.Model):
    # maybe make small class [DR, AC, PR, ...] like enum
    roletype_name = models.CharField(
        'role-type name',
        max_length=15
    )
    roletype_description = models.CharField(
        'role-type description',
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.roletype_name

class Role(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )
    roletype = models.ForeignKey(
        RoleType,
        on_delete=models.CASCADE
    )

class FilmToGenre(models.Model):
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

class FilmToStudio(models.Model):
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )
    studio = models.ForeignKey(
        Studio,
        on_delete=models.CASCADE
    )