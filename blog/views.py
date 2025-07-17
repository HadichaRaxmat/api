from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Logo, Menu
from .serializers import LogoSerializer, MenuSerializer
from django.shortcuts import get_object_or_404



class LogoListView(APIView):
    def get(self, request):
        logos = Logo.objects.all()
        serializer = LogoSerializer(logos, many=True)
        return Response(serializer.data)


class LogoCreateView(APIView):
    def post(self, request):
        serializer = LogoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoDetailView(APIView):
    def get(self, request, pk):
        logo = get_object_or_404(Logo, pk=pk)
        serializer = LogoSerializer(logo)
        return Response(serializer.data)


class LogoUpdateView(APIView):
    def put(self, request, pk):
        logo = get_object_or_404(Logo, pk=pk)
        serializer = LogoSerializer(logo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoDeleteView(APIView):
    def delete(self, request, pk):
        logo = get_object_or_404(Logo, pk=pk)
        logo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MenuListView(APIView):
    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

class MenuCreateView(APIView):
    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MenuDetailView(APIView):
    def get(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

class MenuUpdateView(APIView):
    def put(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDeleteView(APIView):
    def delete(self, request, pk):
        menu = get_object_or_404(Menu, pk=pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
