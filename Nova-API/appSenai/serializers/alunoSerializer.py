from rest_framework import serializers
from appSenai.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aluno
        fields='__all__'