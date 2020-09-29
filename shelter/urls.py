from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^animals/$', views.AnimalListView.as_view(), name='animals'),
    url(r'^animal/(?P<pk>\d+)$', views.AnimalDetailView.as_view(), name='animal-detail'),
    url(r'^shelter/(?P<pk>\d+)$', views.ShelterDetailView.as_view(),
        name='shelter-detail'),
    url(r'^animal/create/$', views.AnimalCreate.as_view(), name='animal_create'),
    url(r'^animal/(?P<pk>\d+)/update/$', views.AnimalUpdate.as_view(),
        name='animal_update'),
    url(r'^animal/(?P<pk>\d+)/delete/$', views.AnimalDelete.as_view(),
        name='animal_delete'),
    url(r'^shelter/create/$', views.ShelterCreate.as_view(), name='shelter_create'),
]
