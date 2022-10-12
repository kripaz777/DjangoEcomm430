from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from django.contrib import messages
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
        self.my_view['brandproducts'] = Product.objects.filter(brand_id = ids)
        return render(request, 'brand.html', self.my_view)

class ProductDetailView(BaseView):
    def get(self,request,slug):
        self.my_view
        self.my_view['products'] = Product.objects.filter(slug = slug)
        self.my_view['reviews'] = Review.objects.filter(slug=slug)
        return render(request,'product-detail.html',self.my_view)
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'The username is already taken')
                return redirect('/signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password
                )
                user.save()
                return redirect('/signup')
        else:
            messages.error(request, 'Password does not match')
            return redirect('/signup')

    return render(request,'signup.html')

def reviews(request):
    if request.method == 'POST':
        review = request.POST['review']
        star = request.POST['star']
        slug = request.POST['slug']
        username = request.user.username
        email = request.user.email
        data = Review.objects.create(
            name = username,
            email = email,
            review = review,
            star = star,
            slug = slug
        )
        data.save()
    return redirect(f'/details/{slug}')

