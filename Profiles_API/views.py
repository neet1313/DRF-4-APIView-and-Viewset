from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Testing API View"""

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
