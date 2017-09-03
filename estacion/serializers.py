from rest_framework import serializers
from .models import Estacion

class EstacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Estacion
		fields = ('id','latitud','logitud','estatura')
