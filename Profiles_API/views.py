# APIViews allow us to write logic for our endpoints

# GET-> fetch data
# POST-> Post data to the DB
# PUT-> Update data from DB
# PATCH-> Partially update data from DB
# DELETE-> Data data from DB

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from Profiles_API import serializers


# ---------------- API View ---------------------
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


# ---------------- VIEWSET ------------------
class HelloViewset(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Get all records."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create/insert a record"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Get single record"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating a part of an object"""
        return Response({'message': 'PATCH'})

    def destroy(self, request, pk=None):
        """Removing an object."""
        return Response({'http_method': 'DELETE'})
