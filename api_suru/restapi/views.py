from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from restapi.models import Aritcle
from restapi.serializers import AritcleSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


#class based api

class Articlelist(APIView):
    def get(self,request):
        arti = Aritcle.objects.all()
        serializer = AritcleSerializer(arti, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AritcleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 class AritleDetails(APIView):
     def get_objects(self,id):
         try:
             return Aritcle.objects.get(id=id)
         except Aritcle.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)

     def get(self,request,id):
         arti =self.get_objects(id)
         serializer = AritcleSerializer(arti)
         return Response(serializer.data)
     def put(self,request,id):
         arti = self.get_objects(id)
         serializer = AritcleSerializer( arti,data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self,request,id):
         arti = self.get_objects(id)
         arti.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)










# #function based api
# @api_view(['GET', 'POST'])
# def articlelist(request):
#     if request.method=='GET':
#         arti=Aritcle.objects.all()
#         serializer=AritcleSerializer(arti,many=True)
#         return Response(serializer.data)
#
#     elif request.method=="POST":
#             serializer=AritcleSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def aritical_detail(request, pk):
#
#     try:
#         arti=Aritcle.objects.get(pk=pk)
#     except Aritcle.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method=='GET':
#         serializer = AritcleSerializer(arti)
#         return Response(serializer.data)
#
#     if request.method=='PUT':
#         serializer=AritcleSerializer(arti,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         arti.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

