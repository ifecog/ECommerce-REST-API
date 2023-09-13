from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from shop.models import Product, Category, Brand
from shop.serializers.product_serializers import ProductSerializer

# create your views here.


class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request):
        category_id = request.query_params.get('category')
        brand_id = request.query_params.get('brand')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        
        query = request.query_params.get('keyword', '')
        
        products = Product.objects.filter(name__icontains=query).order_by('-created_time')
        
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            products = products.filter(category=category)
        if brand_id:
            brand = get_object_or_404(Brand, id=brand_id)
            products = products.filter(brand=brand)
        if min_price and max_price:
            products = products.filter(Q(price__gte=min_price) & Q(price__lte=max_price))
        
        page = request.query_params.get('page')
        paginator = Paginator(products, 8)
        
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
            
        if page == None:
            page = 1
        page = int(page)
        
        serializer = ProductSerializer(products, many=True)
        
        return Response({
            'products': serializer.data,
            'page': page,
            'pages': paginator.num_pages
        })
        
