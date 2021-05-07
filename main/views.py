from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models.query import EmptyQuerySet
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User

from .models import Gender, Person, Genre, Studio, Film, Role, RoleType, FilmType, FilmToGenre, FilmToStudio
from .forms import PersonForm, FilmForm, UserForm, SigninForm
from django.core import serializers
import datetime
from django.http import HttpResponse
from .resources import PersonResource
from .resources import FilmResource
from tablib import Dataset
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate

def index(request):
    if not request.session.get('_auth_user_id', False):
        return render(request, 'main/index.html', {'user': None})

    user_id = request.session['_auth_user_id']
    user = User.objects.filter(id=user_id)
    print(user[0].email)
    print(user[0].username)
    print(user[0].user_permissions)
    return render(request, 'main/index.html', {'user': user[0]})

class PeopleListView(ListView):
    model = Person
    context_object_name = 'content_array'
    template_name = 'main/people.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_string = '{\'cols\': [{\'id\': \'age\', \'label\': \'Age\', \'type\': \'string\'}, {\'id\': \'count\', \'label\': \'Count\', \'type\': \'number\'}],'
        json_string += '\'rows\': ['
        age_counter = {
        '0-20': 0,
        '20-40': 0,
        '40-60': 0,
        '60+': 0
        }
        people = Person.objects.all()
        for person in people:
            if (datetime.date.today() - person.person_date_of_birth) < datetime.timedelta(days=20*365):
                age_counter['0-20'] += 1
            elif (datetime.date.today() - person.person_date_of_birth) < datetime.timedelta(days=40*365):
                age_counter['20-40'] += 1
            elif (datetime.date.today() - person.person_date_of_birth) < datetime.timedelta(days=60*365):
                age_counter['40-60'] += 1
            else:
                age_counter['60+'] += 1

        first = True
        for age, count in age_counter.items():
            if first:
                first = False
            else:
                json_string += ', '
            json_string += '{\'c\': [{ \'v\': '
            json_string += f'\'{age}\''
            json_string += '}, {\'v\': '
            json_string += f'{count}'
            json_string += '}]}'
        json_string += ']}'
        context['people_json'] = json_string
        return context

def people_add(request):
    error = ''
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people')
        error = form.errors

    return render(request, 'main/people_add.html', { 'form': form, 'error': error })

class PeopleDetailView(DetailView):
    model = Person
    template_name = 'main/person.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        per = context['person']
        context['films'] = Film.objects.all()
        context['roles'] = Role.objects.filter(person=per.id)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_string = '{\'cols\': [{\'id\': \'type\', \'label\': \'Type\', \'type\': \'string\'}, {\'id\': \'count\', \'label\': \'Count\', \'type\': \'number\'}],'
        json_string += '\'rows\': ['
        type_counter = {
        'feature-length film': 0,
        'short film': 0,
        'series': 0,
        'animation': 0,
        'anime': 0
        }
        films = Film.objects.all()
        for film in films:
            if film.filmtype.id == 1:
                type_counter['feature-length film'] += 1
            elif film.filmtype.id == 2:
                type_counter['short film'] += 1
            elif film.filmtype.id == 3:
                type_counter['series'] += 1
            elif film.filmtype.id == 4:
                type_counter['animation'] += 1
            else:
                type_counter['anime'] += 1

        first = True
        for ftype, count in type_counter.items():
            if first:
                first = False
            else:
                json_string += ', '
            json_string += '{\'c\': [{ \'v\': '
            json_string += f'\'{ftype}\''
            json_string += '}, {\'v\': '
            json_string += f'{count}'
            json_string += '}]}'
        json_string += ']}'
        context['films_json'] = json_string
        return context

def film_add(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people')

    form = FilmForm()
    return render(request, 'main/film_add.html', { 'form': form })

class FilmsDetailView(DetailView):
    model = Film
    template_name = 'main/film.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fil = context['film']
        context['roles'] = Role.objects.filter(film=fil.id)
        return context

class FilmsUpdateView(UpdateView):
    model = Film
    template_name = 'main/film_add.html'
    context_object_name = 'film'
    form_class = FilmForm

class FilmsDeleteView(DeleteView):
    model = Film
    success_url = '/films'
    template_name = 'main/film_delete.html'
    context_object_name = 'film'

def upload_people(request):
    already_exist_people = []
    wrong_data_input = None
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        #print(imported_data)

        for data in imported_data:
            if Person.objects.filter(person_full_name=data[1]).count() == 0:
                try:
                    value = Person(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4]
                    )
                    value.save()
                except:
                    wrong_data_input = 'wrong data'
                    return render(request, 'main/upload_people.html', {'already_exist': already_exist_people, 'wrong_data': wrong_data_input})
            else:
                already_exist_people.append(data[1])


    return render(request, 'main/upload_people.html', {'already_exist': already_exist_people, 'wrong_data': wrong_data_input})

def upload_films(request):
    already_exist_films = []
    wrong_data_input = None
    if request.method == 'POST':
        film_resource = FilmResource()
        dataset = Dataset()
        new_films = request.FILES['myfile']

        imported_data = dataset.load(new_films.read(),format='xlsx')
        #print(imported_data)

        for data in imported_data:
            if Film.objects.filter(film_name=data[1]).count() == 0:
                try:
                    value = Film(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4]
                    )
                    value.save()
                except:
                    wrong_data_input = 'wrong data'
                    return render(request, 'main/upload_films.html', {'already_exist': already_exist_films, 'wrong_data': wrong_data_input})
            else:
                already_exist_films.append(data[1])


    return render(request, 'main/upload_films.html', {'already_exist': already_exist_films, 'wrong_data': wrong_data_input})



def sign_up(request):
    error = None
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            return redirect('home')
        error = form.errors
    form = UserForm()
    return render(request, 'main/sign_up.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    error = None
    form = SigninForm()
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'invalid username or password'
            return render(request, 'main/login.html', {'form': form, 'error': error})


    return render(request, 'main/login.html', {'form': form, 'error': error})