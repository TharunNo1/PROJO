from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView 
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer

class ProjectCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['created_by'] = request.user.id  
        serializer = ProjectSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
