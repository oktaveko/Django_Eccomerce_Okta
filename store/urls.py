from cgitb import lookup
from django.urls import path
#from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from . import views


#router = SimpleRouter() #ini menggunakan import rest_framework.routers
router = routers.DefaultRouter() #ini menggunakan rest_framework_nested
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')
products_router.register('images',views.ProductImageViewSet, basename='product-images')


carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = router.urls + products_router.urls + carts_router.urls


# URLConf

'''urlpatterns = [
    path('products/', views.ProductList.as_view()), #as_view akan mengubah menjadi function based view
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    #path('collections/', views.collection_list), # contoh penggunaan function based view
    path('collections/', views.CollectionList.as_view()),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
]'''
