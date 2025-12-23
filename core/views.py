# Note: we intentionally avoid default "Shortcut" to keep clarity.
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import EmailMessage
from django.contrib import messages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .models import AddOnService, BlogPost, FAQItem, PageMedia, PortfolioItem, PricingPackage, Product, Service, VideoEmbed, SiteSettings
from django.core.paginator import Paginator


def send_email_with_settings(subject, body, to_email):
    """Send email using SMTP settings from SiteSettings"""
    try:
        settings = SiteSettings.get_settings()
        
        if not settings.email_enabled:
            return False, "Email gönderimi devre dışı"
        
        if not settings.smtp_user or not settings.smtp_password:
            return False, "SMTP ayarları eksik"
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = settings.smtp_from_email or settings.smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))
        
        # Send email
        server = smtplib.SMTP(settings.smtp_host, settings.smtp_port)
        if settings.smtp_use_tls:
            server.starttls()
        server.login(settings.smtp_user, settings.smtp_password)
        server.send_message(msg)
        server.quit()
        
        return True, "Email gönderildi"
    except Exception as e:
        return False, str(e)


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
    print(f"DEBUG blog_list: Total posts = {posts.count()}")
    print(f"DEBUG blog_list: Posts queryset = {list(posts)}")
    
    # Filter by category if provided
    category = request.GET.get("category")
    if category:
        posts = posts.filter(category=category)
    
    # Get all distinct categories for sidebar
    categories = BlogPost.CATEGORY_CHOICES
    
    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    print(f"DEBUG blog_list: page_obj.object_list = {page_obj.object_list}")
    
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
    success = False
    error = None
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        
        if name and email and message:
            settings = SiteSettings.get_settings()
            
            # Email to site owner
            subject = f"Yeni İletişim Formu: {name}"
            body = f"""
            <h2>Yeni İletişim Mesajı</h2>
            <p><strong>Gönderen:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Mesaj:</strong></p>
            <p>{message}</p>
            """
            
            success, error = send_email_with_settings(
                subject=subject,
                body=body,
                to_email=settings.email
            )
            
            if success:
                messages.success(request, 'Mesajınız başarıyla gönderildi!')
            else:
                messages.error(request, f'Mesaj gönderilemedi: {error}')
        else:
            messages.error(request, 'Lütfen tüm alanları doldurun.')
    
    return render(request, "core/contacts.html", {'success': success})


def pricing(request):
    packages = PricingPackage.objects.all()
    add_ons = AddOnService.objects.all()
    return render(request, "core/pricing.html", {"packages": packages, "add_ons": add_ons})


def rsvp(request):
    success = False
    error = None
    addons = AddOnService.objects.all().order_by('order')
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        date = request.POST.get('date', '')
        service = request.POST.get('service', '')
        message = request.POST.get('message', '')
        
        if name and email:
            settings = SiteSettings.get_settings()
            
            # Email to site owner
            subject = f"Yeni Randevu Talebi: {name}"
            body = f"""
            <h2>Yeni Randevu Talebi</h2>
            <p><strong>Ad Soyad:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Telefon:</strong> {phone}</p>
            <p><strong>Tercih Edilen Tarih:</strong> {date}</p>
            <p><strong>Hizmet:</strong> {service}</p>
            <p><strong>Ek Notlar:</strong></p>
            <p>{message}</p>
            """
            
            success, error = send_email_with_settings(
                subject=subject,
                body=body,
                to_email=settings.email
            )
            
            if success:
                messages.success(request, 'Randevu talebiniz alındı! En kısa sürede size dönüş yapacağız.')
            else:
                messages.error(request, f'Randevu talebi gönderilemedi: {error}')
        else:
            messages.error(request, 'Lütfen ad ve email alanlarını doldurun.')
    
    return render(request, "core/rsvp.html", {'success': success, 'addons': addons})


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


@require_POST
def like_post(request, post_id):
    """Like a blog post via AJAX"""
    post = get_object_or_404(BlogPost, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})

# Create your views here.
