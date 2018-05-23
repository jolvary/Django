from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
	nombre = models.CharField(max_length=100, blank=True) #Al tener puesto el null como True daba un error y no me permitía dejar el nombre en blanco.
	email = models.EmailField()
	timestamp =  models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.nombre