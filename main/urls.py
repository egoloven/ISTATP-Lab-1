from django.urls import path
from . import views

urlpatterns = [
    path(''          , views.index      , name='home'       ),
    path('genders'   , views.genders    , name='genders'    ),
    path('people'    , views.people     , name='people'     ),
    path('films'     , views.films      , name='films'      ),
    path('people/add', views.people_add , name='people_add' ),
    # path('films/add' , views.films_add  , name='films_add'  ),
    path('people/<int:id>', views.person, name='person')
]
