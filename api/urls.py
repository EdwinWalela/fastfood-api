from django.contrib import admin
from django.urls import path
from menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories',views.CategoryList.as_view()),
    path('categories/<int:pk>',views.CategoryDetail.as_view()),
    path('menu',views.MenuItemList.as_view()),
    path('menu/<int:pk>',views.MenuItemDetail.as_view())
]
