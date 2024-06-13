from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('create/', DestinationCreateView.as_view(), name='create _destination'),
    path('detail/<int:pk>/', DestinationDetail.as_view(), name='detail'),
    path('update/<int:pk>/', DestinationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DestinationDelete.as_view(), name='delete'),
    path('search/<str:Name>/', DestinationSearch.as_view(), name='search'),

    path('create_dest/', views.create_dest, name='create_dest'),
    path('fetch_dest/<int:id>/', views.fetch_dest, name='fetch_dest'),
    path('update_destination/<int:id>/', views.update_dest, name='update_destination'),
    path('delete_dest/<int:id>/', views.delete_dest, name='delete_dest'),
    path('', views.Index, name='index'),
    path('update_detail/<int:id>/', views.update_detail, name='update_detail'),
    path('delete_confirm/<int:id>',views.delete_confirm,name='delete_confirm')



]
