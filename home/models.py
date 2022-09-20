from django.db import models

# Create your models here.
STATUS = (('active','Active'),('default','Default'))
class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=400)
    logo = models.CharField(blank=True,max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=400)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)
    url = models.URLField(max_length=500,blank = True)
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS,max_length=50)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500, blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=400)
    rank = models.IntegerField()
    def __str__(self):
        return self.name
STOCK = (('In stock','In stock'),('out of stock','out of stock'))
LABELS = (('new','new'),('hot','hot'),('sale','sale'),('','default'))
class Product(models.Model):
    name = models.CharField(max_length= 400)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.CharField(choices = STOCK,max_length=50)
    labels = models.CharField(choices=LABELS,blank = True,max_length=50)

    def __str__(self):
        return self.name