from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from . import views
app_name='zanism'


urlpatterns = [
    path('',views.allproducts,name='allproducts'),
    path('<slug:c_slug>/',views.allproducts,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.PRODUCTDETAILS, name='productdetail')
]