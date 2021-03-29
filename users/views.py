from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
# Serializers
from users.serializers import SignupSerializer
# Create your views here


class SignupView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            response = serializer.save()
            return Response(
                response,
                status=status.HTTP_201_CREATED
            )
        else:
            response = serializer.errors
            return Response(
                {'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

