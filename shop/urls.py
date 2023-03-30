from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .import views
from .views import Home, Product, Category
from django.views.generic import ListView 


urlpatterns = [

   path('', Home.as_view() , name="Home"),
   path('base' , views.base , name="Base"),
   path('category/', Category.as_view() , name="Category"),
   path('product/' , Product.as_view() , name="Product"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


