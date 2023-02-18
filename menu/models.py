from django.db import models

class Category(models.Model):
  class Meta:
    verbose_name_plural = 'categories'
    
  def __str__(self) -> str:
    return self.title
  
  title = models.CharField(max_length=200)  

class MenuItem(models.Model):
  def __str__(self) -> str:
    return self.title
  
  category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  price = models.FloatField()                      