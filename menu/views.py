from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer

class CategoryList(APIView):
  """
  List all categories or create a new category
  """
  def get(self,request,format=None):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many=True)
    return JsonResponse({'categories':serializer.data})
  
  def post(self,request,format=None):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse({
        'message':'category created',
        'category':serializer.data
      })
    return JsonResponse({
        'message':'failed to create category',
        'errors':serializer.errors
    })
