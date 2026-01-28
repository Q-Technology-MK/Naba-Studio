#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding_site.settings')
django.setup()

from core.models import BlogPost

print("=== Blog Posts Detaylı Kontrol ===\n")

posts = BlogPost.objects.all().order_by('-published_at')
for post in posts:
    print(f"📝 Başlık (MK): {post.title}")
    print(f"   Başlık (TR): {post.title_tr if post.title_tr else 'YOK'}")
    print(f"   Başlık (SQ): {post.title_sq if post.title_sq else 'YOK'}")
    print(f"   Slug: {post.slug}")
    print(f"   Hero Image URL: {post.hero_image[:50]}..." if post.hero_image else "   BOŞŞŞ")
    print()
