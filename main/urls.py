from django.urls import path
from . import views

urlpatterns = [
    path(''                      , views.index                     , name='home'         ),
    path('people'                , views.PeopleListView.as_view()  , name='people'       ),
    path('films'                 , views.FilmsListView.as_view()   , name='films'        ),
    path('people/add'            , views.people_add                , name='people_add'   ),
    # path('films/add' , views.films_add  , name='films_add'  ),
    path('people/<int:pk>'       , views.PeopleDetailView.as_view(), name='person'       ),
    path('people/<int:pk>/update', views.PeopleUpdateView.as_view(), name='person_update'),
    path('people/<int:pk>/delete', views.PeopleDeleteView.as_view(), name='person_delete')
]
