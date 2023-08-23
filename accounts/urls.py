from django.urls import path
from accounts import views
# from Store.views import home
app_name = "accounts"

urlpatterns = [
    path('',views.userhome),

]