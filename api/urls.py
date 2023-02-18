from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from menu import views
from authentication.views import RegisterUserAPIView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories',views.CategoryList.as_view()),
    path('categories/<int:pk>',views.CategoryDetail.as_view()),
    path('menu',views.MenuItemList.as_view()),
    path('menu/<int:pk>',views.MenuItemDetail.as_view()),
    path('auth/register',RegisterUserAPIView.as_view()),
    path('auth/login',TokenObtainPairView.as_view(),name='token_obtain_pai')
]
