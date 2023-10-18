from django.urls import path,include
from . import  views
app_name='shop'
urlpatterns = [

    path('',views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatedetail')

]

#username: shop
#email: shop@gmail.com
#password:shop@123