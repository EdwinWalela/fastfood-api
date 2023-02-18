from django.db import models

class Category(models.Model):
  class Meta:
    verbose_name_plural = 'categories'
    
  def __str__(self) -> str:
    return self.title
  
  title = models.CharField(max_length=200)  
