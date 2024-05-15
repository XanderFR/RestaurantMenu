from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # as_view() renders this class as a view
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item'),  # Takes user to specific food page
    path('about/', views.about, name='about')
]
