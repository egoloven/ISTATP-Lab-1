from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'person_full_name'    ,
            'person_date_of_birth',
            'person_date_of_death',
            'gender'
        ]