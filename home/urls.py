from .views import *
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('details/<slug>', ProductDetailView.as_view(), name='details'),
    path('signup', signup, name='signup'),
    path('review', reviews, name='review'),
    path('search',SearchView.as_view(),name = 'search'),
]