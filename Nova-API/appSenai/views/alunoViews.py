from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appSenai.models import Aluno
from appSenai.models import Tarefa
from appSenai.serializers.alunoSerializer import AlunoSerializer
from appSenai.serializers.tarefaSerializer import TarefaSerializer


class AlunoView(APIView):
    def get(self,request):
        try:
            alunos = Aluno.objects.all()
            serializer = AlunoSerializer(alunos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'erro':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = AlunoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DetailAlunoViews(APIView):
    def get_object(self, pk, entity):
        try:
            return entity.objects.get(pk=pk)
        except entity.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, format=None):
        try:
            aluno = self.get_object(pk, Aluno)
            serializer = AlunoSerializer(aluno)
            return Response(serializer.data)
        except Http404:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def put(self, request, pk, format=None):
        try:
            aluno = self.get_object(pk, Aluno)
            serializer = AlunoSerializer(aluno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def delete(self, request, pk, format=None):
        try:
            aluno = self.get_object(pk, Aluno)
            aluno.delete()
            return Response({'status': 'Aluno deletado'},status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({'error': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AlunoTarefaView(APIView):
    def get(self, request, aluno_id, format=None):
        try:
            tasks = Tarefa.objects.filter(aluno_id=aluno_id)
            serializer = TarefaSerializer(tasks, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)