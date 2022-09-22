from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    my_view = {}
    my_view['categories'] = Category.objects.all()
    my_view['brands'] = Brand.objects.all()

class HomeView(BaseView):
    def get(self,request):
        self.my_view['sliders'] = Slider.objects.all()
        self.my_view['ads'] = Ad.objects.all()
        self.my_view['hots'] = Product.objects.filter(labels = 'hot')
        self.my_view['sales'] = Product.objects.filter(labels='sale')
        self.my_view['news'] = Product.objects.filter(labels='new')
        return render(request,'index.html',self.my_view)