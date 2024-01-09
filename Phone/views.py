from django.http import JsonResponse
from .models import Phone
from .serializers import PhoneSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework  import status

@api_view(['GET'])
def getPhones(request):
        phones=Phone.objects.all()
        results=PhoneSerializer(phones,many=True)
        return JsonResponse(results.data,safe=False)
   
@api_view(['GET'])
def getPhoneById(request,id):
    try:
        phone=Phone.objects.get(pk=id)
    except Phone.DoesNotExist:
      return JsonResponse({'Error':"Doesn't Exist in the Database"})

    phone=PhoneSerializer(phone)
    return JsonResponse(phone.data,safe=False)

@api_view(['GET'])
def getPhoneByBrand(request,brandName):
    try:
        phone=Phone.objects.filter(brand=brandName)
    except Phone.DoesNotExist:
      return JsonResponse({'Error':"Doesn't Exist in the Database"})

    phone=PhoneSerializer(phone,many=True)
    return JsonResponse(phone.data,safe=False)


@api_view(['GET'])
def getPhoneByPrice(request,amount):
    try:
        phone=Phone.objects.filter(price=amount)
    except Phone.DoesNotExist:
      return JsonResponse({'Error':"Doesn't Exist in the Database"})

    phone=PhoneSerializer(phone,many=True)
    return JsonResponse(phone.data,safe=False)


@api_view(['POST'])
def addPhone(request):
        is_many = isinstance(request.data, list)
        deserializer=PhoneSerializer(data=request.data,many=is_many)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'Error':'Not Valid'})
        
@api_view(['PUT'])
def updatePhone(request,id):
    try:
        phone=Phone.objects.get(pk=id)
    except Phone.DoesNotExist:
        return Response({'Error':"Doesn't Exist in the Database"},status=status.HTTP_404_NOT_FOUND)
    
    deserializer=PhoneSerializer(data=request.data)
    if deserializer.is_valid():
        deserializer.save()
        return Response(deserializer.data,status=status.HTTP_200_OK)
    
    return Response({'Error':'Not valid'},status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['DELETE'])
def deletePhone(request,id):
     try:
        phone=Phone.objects.get(pk=id)
     except Phone.DoesNotExist:
        return Response({'Error':"Doesn't Exist in the Database"},status=status.HTTP_404_NOT_FOUND)
     
     phone.delete()
     return Response({'Result':"Deleted !"},status=status.HTTP_204_NO_CONTENT)
    





























