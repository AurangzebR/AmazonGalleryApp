from django.urls import path,include
from django.urls.resolvers import URLPattern
from .views import CategoryViewSet, ProductList, SellerViewSet,ProductListAPIView
from rest_framework.routers import DefaultRouter    


category_list= CategoryViewSet.as_view({
    'get':'list',
    'post':'create'
})

category_detail= CategoryViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
})

router= DefaultRouter(trailing_slash=False)
router.register('sellers',SellerViewSet)
urlpatterns=[
    path('',include(router.urls)),
    path('products',ProductList.as_view()),
    path('product-filter/',ProductListAPIView.as_view()),
    path('categories',category_list,name='category_list'),
    path('categories/<int:pk>',category_detail,name="category_detal"),
    #path('categories', CategoryViewSet.as_view()),
    #path('seller', SellerViewSet.as_view())
    ]