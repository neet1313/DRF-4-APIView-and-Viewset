from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Profiles_API import serializers


class HelloAPIView(APIView):
    """Testing API View"""

    serializer_class = serializers.HelloSerializer

    # Get Request
    def get(self, request, format=None):
        """Return a list of API features."""
        an_apiview = [
            'Uses HTTP methods (get, put, patch, post, delete)',
            'Is similar to a traditional Django View',
            'Gives you most control over Your application logic.',
            'Is mapped manually to URLs'
        ]

        # Response should consist of either list or dictionary.
        # So that it can be converted into JSON data.
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            # Retrieving validated name field from the serializer.
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)