from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer

# Create your views here.
@api_view(['POST'])
def api(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    if request.method == "POST":
        name = request.data['name']
        email = request.data['email']
        rollNo = request.data['rollNo']
        phone = request.data['phone']
        branch = request.data['branch']
        team = request.data['team']
        year = request.data['year']
        link = request.data['link']
    
    return JsonResponse({'status':'Success',
    'data': serializer.data
    })
