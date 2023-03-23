from ..models import Persona, Direccion
from rest_framework import serializers



class DireccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Direccion
        fields = "__all__"



class PersonaSerializer(serializers.ModelSerializer):
    direcciones = DireccionSerializer(many=True, read_only=True)

    class Meta:
        model = Persona
        fields = "__all__"