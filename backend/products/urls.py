from django.urls import path, include
from . import views

urlpatterns = [
    
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    # path('', views.ProductCreateAPIView.as_view()),
    path('', views.ProductListCreateAPIView.as_view()),
    # path('', views.ProductListAPIView.as_view()),
    # path('', views.product_alt_view),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()), 
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()), 
]


