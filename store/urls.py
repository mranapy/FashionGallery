from django.urls import path
from store import views
# from Store.views import home
app_name = "store"

urlpatterns = [
    path('',views.home, name='home'),
    path('store/',views.store, name='store'),
    path('store/<slug:category_slug>/',views.store, name='products_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>/',views.productDetails, name='product_details'),
    # path('store/product-details/',views.productDetails, name='product-details'),
]