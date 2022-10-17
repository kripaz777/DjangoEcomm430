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
    my_view['no_counts'] = NoCart.objects.all()



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

class SearchView(BaseView):
    def get(self,request):
        self.my_view
        query = request.GET.get('query')
        print(query)
        if query != "":
            self.my_view['search_product'] = Product.objects.filter(description__icontains = query)
        else:
            return redirect('/')
        return render(request,'product-list.html',self.my_view)

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

def add_cart(slug,user):
    price = Product.objects.get(slug=slug).price
    discounted_price = Product.objects.get(slug=slug).discounted_price
    if Cart.objects.filter(slug=slug,username = user).exists():
        quantity = Cart.objects.get(slug=slug,username = user).quantity
    else:
        quantity = 1
    if discounted_price > 0:
        original_price = discounted_price
    else:
        original_price = price
    return original_price,quantity
def cart(request,slug):
    user = request.user.username
    count = 0
    if Product.objects.filter(slug = slug).exists():
        if Cart.objects.filter(slug = slug,username = user).exists():
            original_price, quantity = add_cart(slug,user)
            quantity = quantity+1
            total =  original_price*quantity
            Cart.objects.filter(slug = slug,username = user).update(total = total,quantity = quantity)
            return redirect('/my_cart')
        else:
            original_price, quantity = add_cart(slug, user)
            data = Cart.objects.create(
                username = user,
                slug = slug,
                total = original_price,
                items = Product.objects.filter(slug = slug)[0]
            )
            data.save()
            if NoCart.objects.filter(user = request.user.username).exists():
                count = count+1
                NoCart.objects.filter(user = request.user.username).update(count = count)
            else:
                NoCart.objects.create(user = request.user.username, count = 1)
            return redirect('/my_cart')
    else:
        return redirect('/')

def delete_cart(request,slug):
    if Cart.objects.filter(slug = slug,username = request.user.username).exists():
        Cart.objects.filter(slug = slug,username = request.user.username).delete()
        return redirect('/my_cart')
    else:
        return redirect('/')

def remove_single_cart(request,slug):
    if Cart.objects.filter(slug=slug, username=request.user.username).exists():
        original_price, quantity = add_cart(slug, request.user.username)
        if quantity > 1:
            quantity = quantity - 1
            total = original_price * quantity
            Cart.objects.filter(slug=slug, username=request.user.username).update(total=total, quantity=quantity)
            return redirect('/my_cart')
        else:
            return redirect('/my_cart')
    else:
        return redirect('/my_cart')

class CartView(BaseView):
    def get(self,request):
        self.my_view
        total = 0
        self.my_view['my_carts'] = Cart.objects.filter(username = request.user.username,checkout = False)
        for i in Cart.objects.filter(username = request.user.username,checkout = False):
            total = total + i.total
        self.my_view['all_total'] = total
        self.my_view['shipping'] = 20
        self.my_view['grand_total'] = self.my_view['all_total']+ self.my_view['shipping']
        return render(request,'cart.html',self.my_view)