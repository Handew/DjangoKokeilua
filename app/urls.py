from django.urls import path
from .views import landingview, supplierlistview, addsupplier, deletesupplier, productslistview, addproduct, deleteproduct

urlpatterns = [
    path('landing/', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('products/', productslistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>', deleteproduct),
]
