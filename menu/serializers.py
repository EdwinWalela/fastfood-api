from rest_framework import serializers
from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id','title']
    
class MenuItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = MenuItem
    fields = ['id','title','description','price','category']
  category = CategorySerializer()