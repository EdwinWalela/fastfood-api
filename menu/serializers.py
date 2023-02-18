from rest_framework import serializers
from .models import Category, MenuItem


class CategoryRelatedField(serializers.RelatedField):
  def to_representation(self, value):
    return str(value)
  def to_internal_value(self, data):
    return Category.objects.get(pk=data)

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id','title']
    
  
class MenuItemSerializer(serializers.ModelSerializer):
  category = CategoryRelatedField(
    queryset=Category.objects.all
  )
  class Meta:
    model = MenuItem
    fields = ['id','title','description','price','category']