from django.contrib import admin

from .models import *


admin.site.register(Direccion)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display = [
			'dni',
			'nombre', 
			'apellido', 
			'edad'
	]
	list_filter = ['dni', 'nombre', 'apellido']
	list_editable = ('edad',)