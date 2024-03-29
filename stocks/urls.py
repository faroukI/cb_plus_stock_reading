from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_current, name='list_current'),
    path('insert/<str:product_id>/<str:expiry_date>/', views.insert, name='insert'),
    path('readings/<str:product_id>/', views.readings, name='readings'),
    path('first/<str:product_id>/', views.read_closest_to_expire, name='read_closest_to_expire'),
    path('get_latest_insert/', views.synchro_get_ts, name='synchro_get_ts'),
    path('get_insert_since_ts/<int:ts>/', views.synchro_stocks_since_ts, name='synchro_stocks_since_ts'),
]
