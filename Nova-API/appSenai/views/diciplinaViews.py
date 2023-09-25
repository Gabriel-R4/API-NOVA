from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appSenai.models.diciplinaModels import Diciplina
from appSenai.serializers.diciplinaSerializer import DiciplinaSerializer

class DisciplinaView(APIView):

    def get(self, request):
        try:
            disciplinas = Diciplina.objects.all()
            serializer = DiciplinaSerializer(disciplinas, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = DiciplinaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DetailDisciplinaView(APIView):

    def get_object(self, pk, entity):
        try:
            return entity.objects.get(pk=pk)
        except entity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            disciplina = self.get_object(pk, Diciplina)
            serializer = DiciplinaSerializer(disciplina)
            return Response(serializer.data)
        except Http404:
            return Response({'error': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk, format=None):
        try:
            disciplina = self.get_object(pk, Diciplina)
            serializer = DiciplinaSerializer(disciplina, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'error': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk, format=None):
        try:
            disciplina = self.get_object(pk, Diciplina)
            disciplina.delete()
            return Response({'status': 'Disciplina deletada'},status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({'error': 'Disciplina não encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)