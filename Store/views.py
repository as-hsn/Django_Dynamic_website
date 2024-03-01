from django.shortcuts import render, get_object_or_404
from Products.models import TopProduct
from Products.models  import AllProduct
from blog.models import Blog


def home(request):
    top_products = TopProduct.objects.all()
    blogs= Blog.objects.all()
    data = {'top_product':top_products, 'blogs':blogs}
    return render(request, "index.html", data)

def shop(request):
    top_products = TopProduct.objects.all()
    all_products = AllProduct.objects.all()
    data = {'top_product':top_products, 'all_product':all_products}
    return render(request, "product.html", data)

def blog(request):
    blogs= Blog.objects.all()
    data = {'blogs':blogs}
    return render(request, "blog.html", data)

def about(request):
    return render(request, "about-us.html")

def contact(request):
    return render(request, "contact.html")

def all_product_detail(request, product_slug):
    all_products = AllProduct.objects.get(product_slug=product_slug)
    bottom_products= TopProduct.objects.all() 
    print(all_products)
    data = {'product':all_products, 'bottom_product': bottom_products}
    return render(request, "product-detail.html", data)

def top_product_detail(request, product_slug):
    top_products = TopProduct.objects.get(product_slug=product_slug) 
    bottom_products= TopProduct.objects.all() 
    data = {'product':top_products, 'bottom_product': bottom_products}
    return render(request, "product-detail.html", data)


def blog_detail(request, blog_slug):
    blog = Blog.objects.get(blog_slug=blog_slug)
    data = {'blog_data':blog}
    return render(request, "blog-details.html", data)    

def product_cart(request):
    return render(request, "product-cart.html")

def product_checkout(request):
    return render(request, "product-checkout.html")

def user_login(request):
    return render(request, "account-login.html")