from django.urls import path
from .views import landingview, supplierlistview, addsupplier

urlpatterns = [
    path('landing/', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),

]
