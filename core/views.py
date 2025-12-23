# Note: we intentionally avoid default "Shortcut" to keep clarity.
from django.shortcuts import get_object_or_404, render

from .models import AddOnService, BlogPost, FAQItem, PageMedia, PortfolioItem, PricingPackage, Product, Service, VideoEmbed
from django.core.paginator import Paginator


def get_media(section):
    """Helper function to get active media for a section"""
    return PageMedia.objects.filter(section=section, is_active=True).order_by('order')


def home(request):
    services = Service.objects.all()
    featured_portfolio = PortfolioItem.objects.filter(featured=True)[:4]
    latest_blog = BlogPost.objects.order_by("-published_at")[:3]
    featured_products = Product.objects.order_by("-created_at")[:3]
    
    # Get media from PageMedia
    hero_home_bg = get_media('hero_home').first()
    hero_home_2_bg = get_media('hero_home_2').first()
    hero_stack_1 = get_media('hero_home_stack_1').first()
    hero_stack_2 = get_media('hero_home_stack_2').first()
    hero_floral = get_media('hero_home_floral').first()
    dress_gallery_minis = get_media('dress_gallery_mini_1')
    bride_gallery_images = list(get_media('bride_gallery_1')) + list(get_media('bride_gallery_2')) + \
                           list(get_media('bride_gallery_3')) + list(get_media('bride_gallery_4')) + \
                           list(get_media('bride_gallery_5'))
    
    try:
        video_embed = VideoEmbed.objects.get(section='home')
    except VideoEmbed.DoesNotExist:
        video_embed = None
    
    context = {
        "services": services,
        "featured_portfolio": featured_portfolio,
        "latest_blog": latest_blog,
        "featured_products": featured_products,
        "video_embed": video_embed,
        # Media
        "hero_home_bg": hero_home_bg,
        "hero_home_2_bg": hero_home_2_bg,
        "hero_stack_1": hero_stack_1,
        "hero_stack_2": hero_stack_2,
        "hero_floral": hero_floral,
        "dress_gallery_minis": dress_gallery_minis,
        "bride_gallery_images": bride_gallery_images,
    }
    return render(request, "core/home.html", context)


def about(request):
    latest_blog = BlogPost.objects.order_by("-published_at")[:3]
    return render(request, "core/page_about.html", {"latest_blog": latest_blog})


def services_page(request):
    services = Service.objects.all()
    packages = PricingPackage.objects.all()
    return render(request, "core/page_services.html", {"services": services, "packages": packages})


def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    
    # Get unique product categories and all products
    categories = Product.CATEGORY_CHOICES
    products = Product.objects.all()
    
    gallery_slides = [
        {"name": "Ninelle", "image": "https://veil.ancorathemes.com/wp-content/uploads/2019/10/bridal1-1024x723.jpg"},
        {"name": "Elizabeth", "image": "https://veil.ancorathemes.com/wp-content/uploads/2019/10/bridal2-1024x1365.jpg"},
        {"name": "Milana", "image": "https://veil.ancorathemes.com/wp-content/uploads/2019/10/bridal3-1024x683.jpg"},
    ]
    return render(
        request,
        "core/page_portfolio.html",
        {
            "portfolio_items": portfolio_items,
            "gallery_slides": gallery_slides,
            "categories": categories,
            "products": products,
        },
    )


def portfolio_masonry(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(
        request,
        "core/portfolio_masonry.html",
        {"portfolio_items": portfolio_items},
    )


def portfolio_detail(request, slug):
    item = get_object_or_404(PortfolioItem, slug=slug)
    return render(request, "core/portfolio_detail.html", {"item": item})


def blog_list(request):
    posts = BlogPost.objects.order_by("-published_at")
    
    # Filter by category if provided
    category = request.GET.get("category")
    if category:
        posts = posts.filter(category=category)
    
    # Get all distinct categories for sidebar
    categories = BlogPost.CATEGORY_CHOICES
    
    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        "posts": posts,
        "page_obj": page_obj,
        "categories": categories,
        "selected_category": category,
    }
    return render(request, "core/page_blog.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "core/blog_detail.html", {"post": post})


def contacts(request):
    return render(request, "core/contacts.html")


def pricing(request):
    packages = PricingPackage.objects.all()
    add_ons = AddOnService.objects.all()
    return render(request, "core/pricing.html", {"packages": packages, "add_ons": add_ons})


def rsvp(request):
    return render(request, "core/rsvp.html")


def faq(request):
    faqs = FAQItem.objects.all().order_by('category', 'order')
    default_bg = "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80"
    
    # Group FAQs by category
    faq_categories = {}
    for faq in faqs:
        if faq.category not in faq_categories:
            faq_categories[faq.category] = []
        faq_categories[faq.category].append(faq)
    
    return render(
        request,
        "core/faq.html",
        {
            "faq_categories": faq_categories,
            "accommodation_background": default_bg
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "core/product_detail.html", {"product": product})

# Create your views here.
