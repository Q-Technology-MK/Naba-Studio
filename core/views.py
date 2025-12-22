# Note: we intentionally avoid default "Shortcut" to keep clarity.
from django.shortcuts import get_object_or_404, render

from .models import BlogPost, FAQItem, PortfolioItem, PricingPackage, Product, Service
from django.core.paginator import Paginator


def home(request):
    services = Service.objects.all()
    featured_portfolio = PortfolioItem.objects.filter(featured=True)[:4]
    latest_blog = BlogPost.objects.order_by("-published_at")[:3]
    featured_products = Product.objects.order_by("-created_at")[:3]
    context = {
        "services": services,
        "featured_portfolio": featured_portfolio,
        "latest_blog": latest_blog,
        "featured_products": featured_products,
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
    gallery_slides = [
        {"name": "Ninelle", "image": "https://veil.ancorathemes.com/wp-content/uploads/2019/10/bridal1-1024x723.jpg"},
        {"name": "Elizabeth", "image": "https://veil.ancorathemes.com/wp-content/uploads/2019/10/bridal2-1024x1365.jpg"},
        {"name": "Milana", "image": "https://veil.ancorathemes.com/wp-content/uploads/2019/10/bridal3-1024x683.jpg"},
    ]
    return render(
        request,
        "core/page_portfolio.html",
        {"portfolio_items": portfolio_items, "gallery_slides": gallery_slides},
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
    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "page_obj": page_obj,
    }
    return render(request, "core/page_blog.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "core/blog_detail.html", {"post": post})


def contacts(request):
    return render(request, "core/contacts.html")


def pricing(request):
    packages = PricingPackage.objects.all()
    return render(request, "core/pricing.html", {"packages": packages})


def rsvp(request):
    return render(request, "core/rsvp.html")


def faq(request):
    faqs = FAQItem.objects.all()
    default_bg = "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80"
    accommodation_bg_item = faqs.filter(question__icontains="accommodation background").first()
    accommodation_background = accommodation_bg_item.answer if accommodation_bg_item else default_bg
    return render(
        request,
        "core/faq.html",
        {"faqs": faqs, "accommodation_background": accommodation_background},
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "core/product_detail.html", {"product": product})

# Create your views here.
