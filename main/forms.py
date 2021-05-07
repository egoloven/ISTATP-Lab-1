from django.forms import ModelForm, TextInput
from .models import Person, Role, Film
from django.contrib.auth.models import User

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'person_full_name'    ,
            'person_date_of_birth',
            'person_date_of_death',
            'gender'
        ]
class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = [
            'film_name',
            'film_description',
            'film_duration',
            'filmtype'
        ]

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = [
            'person',
            'film',
            'roletype'
        ]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'first_name',
        'last_name',
        'password'
        ]
        widgets = {
            'username': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Username'
                }
            ),
            'password': TextInput(
                attrs={
                    'type': 'password',
                    'class': 'form-control',
                    'placeholder': 'Password',
                    'id': 'exampleInputPassword1'
                }
            ),
            'email': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'email'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'First Name'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Last Name'
                }
            )
        }

class SigninForm(ModelForm):
    class Meta:
        model = User
        fields = [
        'username',
        'password'
        ]

        widgets = {
            'username': TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Username'
                }
            ),
            'password': TextInput(
                attrs={
                    'type': 'password',
                    'class': 'form-control',
                    'placeholder': 'Password',
                    'id': 'exampleInputPassword1'
                }
            )
        }