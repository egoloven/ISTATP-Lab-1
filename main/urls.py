from django.urls import path
from . import views

urlpatterns = [
    path(''                      , views.index                     , name='home'         ),
    path('people'                , views.PeopleListView.as_view()  , name='people'       ),
    path('films'                 , views.FilmsListView.as_view()   , name='films'        ),
    path('people/add'            , views.people_add                , name='people_add'   ),
    path('films/add'             , views.film_add                  , name='film_add'     ),
    path('people/<int:pk>'       , views.PeopleDetailView.as_view(), name='person'       ),
    path('films/<int:pk>'        , views.FilmsDetailView.as_view() , name='film'         ),
    path('people/<int:pk>/update', views.PeopleUpdateView.as_view(), name='person_update'),
    path('films/<int:pk>/update' , views.FilmsUpdateView.as_view() , name='film_update'  ),
    path('people/<int:pk>/delete', views.PeopleDeleteView.as_view(), name='person_delete'),
    path('films/<int:pk>/delete' , views.FilmsDeleteView.as_view() , name='film_delete'  ),
    path('people/upload'         , views.upload_people             , name='people_upload'),
    path('films/upload'          , views.upload_films              , name='films_upload' ),
    path('signup'                , views.sign_up                   , name='sign_up'      ),
    path('logout'                , views.logout_view               , name='logout'       ),
    path('login'                , views.login_view               , name='login'       )
]
