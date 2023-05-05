# GET-> fetch data
# POST-> Post data to the DB
# PUT-> Update data from DB
# PATCH-> Partially update data from DB
# DELETE-> Data data from DB

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Profiles_API import serializers


class HelloAPIView(APIView):
    """Testing API View"""

    serializer_class = serializers.HelloSerializer

    # Creating a Get Request function
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

    # Creating a POST request function
    def post(self, request):
        """Create a hello message with our name."""

        # --> 1 Data Deserialized
        serializer = self.serializer_class(data=request.data)

        # --> 2 Form Data Validated
        if serializer.is_valid():
            # Retrieving validated name field from the serializer.
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

        # --> 3 Converted into complex data type and posted to the DB
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Creating a PUT, PATCH, DELETE methods

    def put(self, request, pk=None):
        """To Update an ENTIRE object in DB"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """To PARTIALLY update an object in DB"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """To delete an object in DB"""
        return Response({'message': 'DELETE'})
