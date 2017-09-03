# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Estacion(models.Model):

	latitud = models.CharField(max_length=100)
	longitud = models.CharField(max_length=100)
	estatura = models.IntegerField(default=0)
