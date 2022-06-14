from django.contrib import admin

from .models import Machine, Voiture,Personne

admin.site.register(Machine)
admin.site.register(Voiture)
admin.site.register(Personne)