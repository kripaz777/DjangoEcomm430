from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet,ProductListView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('product/', ProductListView.as_view(), name='product'),

]