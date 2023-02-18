from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer

@api_view(['GET'])
def category_list(request):
  categories = Category.objects.all()
  serializer = CategorySerializer(categories,many=True)
  return JsonResponse({'categories':serializer.data})