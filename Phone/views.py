from django.http import JsonResponse
from .models import Phone
from .serializers import PhoneSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework  import status

@api_view(['GET','POST'])
def getAllPhones(request):
    if request.method=='GET':
        phones=Phone.objects.all()
        results=PhoneSerializer(phones,many=True)
        return JsonResponse(results.data,safe=False)
    elif request.method=='POST':
        is_many = isinstance(request.data, list)
        deserializer=PhoneSerializer(data=request.data,many=is_many)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'Error':'Not Valid'})













