from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
    my_view = {}

class HomeView(BaseView):
    def get(self,request):

        return render(request,'index.html',self.my_view)