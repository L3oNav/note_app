from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from notes.serializers import (
    NotesCreateSerializer,
    ReadNotesSerializer,
    ReadNoteByIdSerializer,
    UpdateNoteSerializer,
    DeleteNoteSerializer,
)
# Create your views here.


class NotesCreateView(APIView):

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = NotesCreateSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializer.errors
            return Response({
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class ReadNotesView(APIView):

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = ReadNotesSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializer.errors
            return Response({
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class ReadNoteByIdView(APIView):

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = ReadNoteByIdSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializer.errors
            return Response({
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class UpdateNoteView(APIView):

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = UpdateNoteSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializer.errors
            return Response({
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteNoteView(APIView):

    def post(self, request):
        data = request.data
        data['user'] = request.user.email
        serializer = DeleteNoteSerializer(data=data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = serializer.errors
            return Response({
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

