from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_current, name='list_current'),
    path('insert/<str:product_id>/<str:expiry_date>/', views.insert, name='insert'),
    path('readings/<str:product_id>/', views.readings, name='readings'),
]
