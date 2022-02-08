from django.http import JsonResponse

def get(Routes, request):
    return JsonResponse({
        'status': 'success',
        'message': 'Hello, World!'
    })