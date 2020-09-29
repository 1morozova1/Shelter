from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from shelter.models import Shelter, Animal


@login_required
def index(request):
    shelter_list = Shelter.objects.all()

    return render(
        request,
        'index.html',
        context={
            'shelter_list': shelter_list,
        }
    )


class AnimalListView(generic.ListView):
    model = Animal
    paginate_by = 10

    def get_queryset(self):
        return Animal.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AnimalListView, self).get_context_data(**kwargs)
        return context


class AnimalDetailView(generic.DetailView):
    model = Animal


class ShelterDetailView(generic.DetailView):
    model = Shelter


class AnimalCreate(CreateView):
    model = Animal
    fields = '__all__'


class AnimalUpdate(UpdateView):
    model = Animal
    fields = '__all__'


class AnimalDelete(DeleteView):
    model = Animal
    success_url = reverse_lazy('animals')


class ShelterCreate(CreateView):
    model = Shelter
    fields = '__all__'
