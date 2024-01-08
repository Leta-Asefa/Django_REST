from django.http import JsonResponse
from .models import Phone
from .serializers import PhoneSerializer

def getAllPhones(request):
    phones=Phone.objects.all()
    results=PhoneSerializer(phones,many=True)
    return JsonResponse(results.data,safe=False)











