from django.urls import path
from .views import landingview, supplierlistview, addsupplier, deletesupplier, productslistview, addproduct, deleteproduct, edit_supplier_get, edit_supplier_post, edit_product_get, edit_product_post

urlpatterns = [
    # SUPPLIERS
    path('landing/', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('delete-supplier/<int:id>/', deletesupplier),

    # PRODUCTS
    path('products/', productslistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    
]
