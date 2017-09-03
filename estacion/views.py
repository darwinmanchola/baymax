# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Estacion
from rest_framework import viewsets
from .serializers import EstacionSerializer


class EstacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer
