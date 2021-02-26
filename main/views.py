from django.shortcuts import render
from django.http import HttpResponse
from .models import Gender, Person, Genre, Studio, Film, Role, RoleType, FilmType, FilmToGenre, FilmToStudio

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