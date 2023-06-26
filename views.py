from django.shortcuts import render
from django.shortcuts import render
from . models import jadwal
from . seriallizers import jadwalSerializer

#rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def readjadwal(request):
    jadwalimsak = jadwal.objects.all()
    serializer = jadwalSerializer(jadwalimsak, many=True )
    return Response(serializer.data)
@api_view(['GET'])
def detailjadwal(request, id):
    jadwalimsak = jadwal.objects.get(pk=id)
    serializer = jadwalSerializer(jadwalimsak, many=False )
    return Response(serializer.data)
@api_view(['POST'])
def createjadwal(request):
    jadwalimsak = jadwal.objects.all()
    serializer = jadwalSerializer(data=request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updatejadwal(request, id):
    jadwalimsak = jadwal.objects.get(pk=id)
    serializer = jadwalSerializer(instance=jadwalimsak, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deletejadwal(request, id):
    jadwalimsak = jadwal.objects.get(pk=id)
    jadwalimsak.delete()
    return Response('data di hapus', status=204)

# Create your views here.
