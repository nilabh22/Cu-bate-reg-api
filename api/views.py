from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer

# Create your views here.
@api_view(['POST','GET'])
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
    
    return JsonResponse({'status':'Success',
    'data': serializer.data
    })
