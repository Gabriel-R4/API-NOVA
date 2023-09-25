from rest_framework import serializers
from appSenai.models import Diciplina

class DiciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Diciplina
        fields='__all__'