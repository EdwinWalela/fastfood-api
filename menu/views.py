from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from .models import Category,MenuItem
from .serializers import CategorySerializer,MenuItemSerializer

class CategoryList(
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  generics.GenericAPIView):
  """
  List all categories or create a new category
  """
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  def get(self,request,*args,**kwargs):
    return self.list(request,*args,**kwargs)
  
  def post(self,request,*args, **kwargs):
    return self.create(request,*args,**kwargs)

class CategoryDetail(
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  generics.GenericAPIView
):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
  
class MenuItemList(
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  generics.GenericAPIView):
  
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  
  def get(self,request,*args,**kwargs):
    categories = Category.objects.all()
    category_serializer = CategorySerializer(categories,many=True)
    
    menu = {}
    
    for category in category_serializer.data:
      menuItems = list(MenuItem.objects.filter(category=category['id']))
      serializer = MenuItemSerializer(menuItems,many=True)
      menu[category['title']] = serializer.data
    
    return Response(menu)
    
  
  def post(self,request,*args,**kwargs):
    return self.create(request,*args,**kwargs)
  
class MenuItemDetail(
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  generics.GenericAPIView):
  
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer
  
  def get(self,request,*args,**kwargs):
    return self.retrieve(request,*args,**kwargs)

  def put(self,request,*args,**kwargs):
    return self.update(request,*args,**kwargs)
  
  def delete(self,request,*args,**kwargs):
    return self.destroy(request,*args,**kwargs)