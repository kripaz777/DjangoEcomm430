from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    my_view = {}
    my_view['categories'] = Category.objects.all()
    my_view['brands'] = Brand.objects.all()
    my_view['sales'] = Product.objects.filter(labels='sale')

class HomeView(BaseView):
    def get(self,request):
        self.my_view
        self.my_view['sliders'] = Slider.objects.all()
        self.my_view['ads'] = Ad.objects.all()
        self.my_view['hots'] = Product.objects.filter(labels = 'hot')
        self.my_view['news'] = Product.objects.filter(labels='new')
        return render(request,'index.html',self.my_view)

class CategoryView(BaseView):
    def get(self,request,slug):
        self.my_view
        ids = Category.objects.get(slug = slug).id
        self.my_view['catproducts'] = Product.objects.filter(category_id = ids)
        return render(request, 'category.html', self.my_view)


class BrandView(BaseView):
    def get(self,request,slug):
        self.my_view
        ids = Brand.objects.get(slug = slug).id
        self.my_view['brandroducts'] = Product.objects.filter(brand_id = ids)
        return render(request, 'brand.html', self.my_view)