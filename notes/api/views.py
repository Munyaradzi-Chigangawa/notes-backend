from django.http import JsonResponse

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
        }
        {
            'Endpoint' : '/notes/id/delete',
            'method' : 'DELETE',
            'body' : None,
            'description' : 'Deletes the note'
        }
    ]
    return JsonResponse(routes, safe = False)