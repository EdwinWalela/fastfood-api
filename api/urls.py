from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories',views.CategoryList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)