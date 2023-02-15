from django.urls import path

from .views import product_create_api_view, product_detail_api_view, product_update_api_view, product_delete_api_view

urlpatterns = [
    path('', product_create_api_view),
    path('<int:pk>/', product_detail_api_view),
    path('<int:pk>/update/', product_update_api_view),
    path('<int:pk>/delete/', product_delete_api_view),
]
