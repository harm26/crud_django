from rest_framework import serializers
from .models import Familiares

class FamiliaresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Familiares
        fields = ('id', 'nombre', 'parentesco', 'vive')