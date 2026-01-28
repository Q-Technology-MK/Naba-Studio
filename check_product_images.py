#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding_site.settings')
django.setup()

from core.models import Product, ProductImage

print("=== Product Images Kontrol ===\n")

products = Product.objects.all()[:5]  # İlk 5 ürünü kontrol et

for product in products:
    print(f"📦 Product: {product.name}")
    print(f"   Slug: {product.slug}")
    print(f"   product.image (ImageField): {product.image if product.image else 'BOŞŞ'}")
    
    # ProductImage ilişkisi
    product_images = product.images.all()
    print(f"   ProductImage Count: {product_images.count()}")
    
    if product_images.exists():
        for idx, img in enumerate(product_images, 1):
            print(f"      [{idx}] {img.image.url if img.image else 'BOŞŞ'} (Primary: {img.is_primary})")
    
    # get_all_images() method
    all_images = product.get_all_images()
    print(f"   get_all_images() Count: {all_images.count()}")
    
    # get_primary_image() method
    primary = product.get_primary_image()
    print(f"   get_primary_image(): {primary[:50]}..." if len(primary) > 50 else f"   get_primary_image(): {primary}")
    
    print()
