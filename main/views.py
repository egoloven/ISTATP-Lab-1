from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models.query import EmptyQuerySet
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Gender, Person, Genre, Studio, Film, Role, RoleType, FilmType, FilmToGenre, FilmToStudio
from .forms import PersonForm


def index(request):
	return render(request, 'main/index.html')

class PeopleListView(ListView):
    model = Person
    context_object_name = 'content_array'
    template_name = 'main/people.html'

def people_add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people')

        print(form.errors)

    form = PersonForm()
    return render(request, 'main/people_add.html', { 'form': form })

class PeopleDetailView(DetailView):
    model = Person
    template_name = 'main/person.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        per = context['person']
        context['films'] = Film.objects.all()
        context['roles'] = Role.objects.filter(person=per.id)
        print(context)
        return context

class PeopleUpdateView(UpdateView):
    model = Person
    template_name = 'main/people_add.html'
    context_object_name = 'person'
    form_class = PersonForm

class PeopleDeleteView(DeleteView):
    model = Person
    success_url = '/people'
    template_name = 'main/people_delete.html'
    context_object_name = 'person'

class FilmsListView(ListView):
    model = Film
    context_object_name = 'content_array'
    template_name = 'main/films.html'

def films(request):
    content_array = []
    film_objects = Film.objects.all()
    for item in film_objects:
        film = {
            'full_name': item.film_name
        }
        content_array.append(film)

    return render(request, 'main/films.html', { 'content_array': content_array })