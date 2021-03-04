from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models.query import EmptyQuerySet

from .models import Gender, Person, Genre, Studio, Film, Role, RoleType, FilmType, FilmToGenre, FilmToStudio
from .forms import PersonForm


def index(request):
	return render(request, 'main/index.html')

def genders(request):
    content_array = []

    genders_list = Gender.objects.all()

    for item in genders_list:
        gender = {
            'gender': item.gender_name,
            'description': item.gender_description
        }
        content_array.append(gender)

    return render(request, 'main/genders.html', { 'content_array': content_array })

def people(request):
    content_array = []

    people_objects = Person.objects.all()

    for item in people_objects:
        person = {
            'full_name': item.person_full_name
        }
        content_array.append(person)
    return render(request, 'main/people.html', { 'content_array': content_array })

def films(request):
    content_array = []

    film_objects = Film.objects.all()

    for item in film_objects:
        film = {
            'full_name': item.film_name
        }
        content_array.append(film)
    return render(request, 'main/films.html', { 'content_array': content_array })

def people_add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people')
        print(form.errors)

    form = PersonForm()
    return render(request, 'main/people_add.html', { 'form': form })

def person(request, id):
    person_obj = get_object_or_404(Person, pk=id)

    person = {
        'full_name': person_obj.person_full_name,
        'date_of_birth': person_obj.person_date_of_birth,
        'date_of_death': person_obj.person_date_of_death,
        'gender': person_obj.gender,
    }

    return render(request, 'main/person.html', { 'person': person })