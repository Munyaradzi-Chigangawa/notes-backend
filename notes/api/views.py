from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : '/notes/',
            'method' : 'GET',
            'body' : None,
            'description' : 'Return Array of notes'
        },
        {
            'Endpoint' : '/notes/id',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns single note with specified id',
        },
        {
            'Endpoint' : '/notes/create',
            'method' : 'POST',
            'body' : {'body': ""},
            'description' : 'Creates a new post with specified info'
        },
        {
            'Endpoint' : '/notes/id/update',
            'method' : 'PUT',
            'body' : {'body': ""},
            'description' : 'Updates a note with text input'
        },
        {
            'Endpoint' : '/notes/id/delete',
            'method' : 'DELETE',
            'body' : None,
            'description' : 'Deletes the note',
        },
    ]
    return Response(routes)