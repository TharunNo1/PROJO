from django.shortcuts import render
from rest_framework import status 
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import SignUpSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!", "user": {"email": user.email}}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HelloUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "message": f"Hello, {user.username}! Welcome to PROJO"
        })
    