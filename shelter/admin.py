from django.contrib import admin

from shelter.models import Animal, Shelter, Client


admin.site.register(Animal)
admin.site.register(Shelter)
admin.site.register(Client)
