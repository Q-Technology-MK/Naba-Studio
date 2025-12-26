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
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    services = Service.objects.all()
    featured_portfolio = PortfolioItem.objects.filter(featured=True)[:4]
    latest_blog_raw = BlogPost.objects.order_by("-published_at")[:3]
    featured_products = Product.objects.filter(is_featured=True)[:3]
    # Fallback to latest products if no featured ones
    if not featured_products.exists():
        featured_products = Product.objects.order_by("-created_at")[:3]
    
    # Add translated fields to blog posts
    latest_blog = []
    for post in latest_blog_raw:
        post.translated_title = post.get_title(lang)
        post.translated_excerpt = post.get_excerpt(lang)
        latest_blog.append(post)
    
    # Bride Gallery Text Translations
    bride_gallery_text = {
        'mk': {
            'title': 'Вашата приказна, нашиот дизајн',
            'paragraph_1': 'Ние не продаваме само венчаници; ние создаваме атмосфера на самодоверба и грациозност. Нашата инспирација доаѓа од модерната жена – онаа која ја цени класиката, но не се плаши да покаже храброст во деталите. Без разлика дали станува збор за минималистички „A-cut" модел или раскошна балска тоалета со долг вел, секое парче е дизајнирано да ја нагласи внатрешната убавина. Во нашето атеље, секоја проба е посебен настан, консултација каде што заедно го дефинираме патот до совршениот изглед.',
            'title_2': 'Наследството на македонскиот „Couture"',
            'paragraph_2': 'Како водечко атеље во Северна Македонија, нашата мисија е да ја подигнеме границата на она што значи висока мода на овие простори. Горди сме на фактот што нашите креации се дел од најзначајните моменти на илјадници семејства. Кога ќе го погледнете вашиот фустан по десет години, сакаме да го почувствувате истото возбудување како и првиот пат кога го облековте. Тоа е моќта на вистинскиот дизајн – тој не старее, тој само добива на вредност низ емоциите и спомените што ги носи со себе.',
            'title_3': 'Започнете го вашето патување денес',
            'paragraph_3': 'Ве покануваме да го истражите светот каде што луксузот се среќава со емоцијата. Погледнете ја нашата галерија на фустани и дозволете вашата имагинација да ве води. Секој детал, од деликатните копчиња на грбот до воздушестите слоеви на здолништето, е тука за да ви каже дека заслужувате ништо помалку од совршенство. Вашиот сон чека да биде сошиен, а ние сме тука да ја држиме иглата што ќе ја напише вашата најубава приказна.',
        },
        'tr': {
            'title': 'Sizin Hikayeniz, Bizim Tasarımımız',
            'paragraph_1': 'Biz sadece gelinlik satmıyoruz; özgüven ve zarafet atmosferi yaratıyoruz. Bizim ilhamımız modern kadından geliyor – klasikleri takdir eden ama detaylarda cesaret göstermekten korkmayan kadın. İster minimalist bir "A-kesim" model ister uzun tüllü görkemli bir balo elbisesi olsun, her parça iç güzelliği vurgulamak için tasarlanmıştır. Atölyemizde, her deneme özel bir etkinlik, birlikte mükemmel görünüşe giden yolu tanımlayan bir danışmadır.',
            'title_2': 'Makedonya "Couture" Mirasının',
            'paragraph_2': 'Kuzey Makedonya\'nın öncü atölyesi olarak, misyonumuz bu bölgelerde yüksek modanın anlamını yükseltmektir. Yaratımlarımızın binlerce ailenin en önemli anlarının bir parçası olduğu gerçeğinden gurur duyuyoruz. On yıl sonra gelinliğinize baktığınızda, ilk kez giydiğiniz zaman hissettiğiniz heyecanı hissetmenizi istiyoruz. Bu, gerçek tasarımın gücüdür – asla yaşlanmaz, sadece taşıdığı duygular ve anılarla değer kazanır.',
            'title_3': 'Bugün Yolculuğunuzu Başlatın',
            'paragraph_3': 'Sizi lüksün duygularla buluştuğu dünyayı keşfetmeye davet ediyoruz. Gelinlik galerimizi görün ve hayal gücünüzün sizi rehber etmesine izin verin. Her detay, arkadaki hassas düğmelerden eteğin hava tabakalarına kadar, mükemmellikten daha azını hak etmediğinizi söylemek için burada. Sizin rüyanız dikilmeyi bekliyor ve biz sizin en güzel hikayesini yazacak iğneyi tutmak için buradayız.',
        },
        'sq': {
            'title': 'Historia Juaj, Dizajni Ynë',
            'paragraph_1': 'Ne nuk shitim vetëm fustan nuse; ne krijojmë një atmosferë të besimit në vete dhe elegancës. Frymëzimi ynë vjen nga gruaja moderne – ajo që vlerëson klasikën, por nuk ka frikë të tregojë guxim në detaje. Pavarësisht nëse bëhet fjalë për një model minimalist "A-line" ose një fustan balli të pasur me vel të gjatë, çdo copë është projektuar për të nënvizuar bukurinë e brendshme. Në atelierin tonë, çdo provë është një ngjarje e veçantë, një konsultim ku së bashku përcaktojmë rrugën drejt pamjes së përsosur.',
            'title_2': 'Trashëgimia e "Couture" Maqedonase',
            'paragraph_2': 'Si atelie udhëheqëse në Maqedoninë e Veriut, misioni ynë është të ngrejmë kufirin e asaj që do të thotë moda e lartë në këto hapësira. Jemi të nderuar me faktin se krijimet tona janë pjesë e momenteve më të rëndësishme të mijëra familjesh. Kur ta shikoni fustaninë tuaj pas dhjetë vitesh, duam të ndihni të njëjtën emocion si herën e parë kur e veshët. Kjo është fuqia e dizajnit të vërtetë – ai nuk plakët kurrë, ai vetëm fitim në vlerë përmes emocioneve dhe kujtimeve që mbart me vete.',
            'title_3': 'Filloni Udhëtimin Tuaj Sot',
            'paragraph_3': 'Ju ftojmë të eksploroni botën ku luksi takohet me emocionin. Shikoni galerin tonë të fustaneve dhe lejoni imagjinatën tuaj të ju udhëzojë. Çdo detaj, nga butonat delikat në shpinë deri në shtresat ajroze të poshtës, është këtu për t\'ju thënë se nuk meritoni asgjë më pak se përfeksion. Ëndrra juaj pret të qepet, dhe ne jemi këtu për të mbajtur gjilpërën që do të shkruajë historinë tuaj më të bukur.',
        }
    }
    
    # Get media from PageMedia
    hero_home_bg = get_media('hero_home').first()
    hero_home_2_bg = get_media('hero_home_2').first()
    hero_stack_1 = get_media('hero_home_stack_1').first()
    hero_stack_2 = get_media('hero_home_stack_2').first()
    hero_floral = get_media('hero_home_floral').first()
    
    # Dress Gallery Mini images (3 images)
    dress_mini_1 = get_media('dress_gallery_mini_1').first()
    dress_mini_2 = get_media('dress_gallery_mini_2').first()
    dress_mini_3 = get_media('dress_gallery_mini_3').first()
    
    # Bride Gallery images (5 images)
    bride_img_1 = get_media('bride_gallery_1').first()
    bride_img_2 = get_media('bride_gallery_2').first()
    bride_img_3 = get_media('bride_gallery_3').first()
    bride_img_4 = get_media('bride_gallery_4').first()
    bride_img_5 = get_media('bride_gallery_5').first()
    
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
        # Hero Media
        "hero_home_bg": hero_home_bg,
        "hero_home_2_bg": hero_home_2_bg,
        "hero_stack_1": hero_stack_1,
        "hero_stack_2": hero_stack_2,
        "hero_floral": hero_floral,
        # Dress Gallery Mini
        "dress_mini_1": dress_mini_1,
        "dress_mini_2": dress_mini_2,
        "dress_mini_3": dress_mini_3,
        # Bride Gallery
        "bride_img_1": bride_img_1,
        "bride_img_2": bride_img_2,
        "bride_img_3": bride_img_3,
        "bride_img_4": bride_img_4,
        "bride_img_5": bride_img_5,
        # Bride Gallery Text
        "bride_gallery_text": bride_gallery_text.get(lang, bride_gallery_text['mk']),
        "lang": lang,
    }
    return render(request, "core/home.html", context)


def about(request):
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    latest_blog_raw = BlogPost.objects.order_by("-published_at")[:3]
    # Add translated fields to blog posts
    latest_blog = []
    for post in latest_blog_raw:
        post.translated_title = post.get_title(lang)
        post.translated_excerpt = post.get_excerpt(lang)
        latest_blog.append(post)
    
    # Get video embed for about page
    try:
        video_embed = VideoEmbed.objects.get(section='about')
    except VideoEmbed.DoesNotExist:
        video_embed = None
    
    return render(request, "core/page_about.html", {
        "latest_blog": latest_blog, 
        "lang": lang,
        "video_embed": video_embed,
    })


def services_page(request):
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    services = Service.objects.all()
    packages_raw = PricingPackage.objects.all()
    
    # Add translated fields to packages
    packages = []
    for pkg in packages_raw:
        pkg.translated_name = pkg.get_name(lang)
        pkg.translated_period = pkg.get_period(lang)
        pkg.translated_features = pkg.get_features(lang)
        packages.append(pkg)
    
    # Get contact gallery images from PageMedia (same as contacts page Instagram gallery)
    contact_gallery_images = get_media('contact_gallery')
    return render(request, "core/page_services.html", {
        "services": services, 
        "packages": packages,
        "contact_gallery_images": contact_gallery_images,
        "lang": lang,
    })


def portfolio(request):
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    portfolio_items_raw = PortfolioItem.objects.all()
    # Add translated fields to portfolio items
    portfolio_items = []
    for item in portfolio_items_raw:
        item.translated_title = item.get_title(lang)
        item.translated_summary = item.get_summary(lang)
        portfolio_items.append(item)
    
    # Get translated categories based on current language
    categories = [(key, Product.get_category_name(key, lang)) for key, _ in Product.CATEGORY_CHOICES]
    
    # Add translated fields to products
    products_raw = Product.objects.all()
    products = []
    for product in products_raw:
        product.translated_name = product.get_name(lang)
        product.translated_summary = product.get_summary(lang)
        product.translated_category = Product.get_category_name(product.category, lang)
        products.append(product)
    
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
            "lang": lang,
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
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    item = get_object_or_404(PortfolioItem, slug=slug)
    # Add translated fields
    item.translated_title = item.get_title(lang)
    item.translated_summary = item.get_summary(lang)
    item.translated_description = item.get_description(lang)
    
    return render(request, "core/portfolio_detail.html", {"item": item, "lang": lang})


def blog_list(request):
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    posts_raw = BlogPost.objects.order_by("-published_at")
    
    # Filter by category if provided
    category = request.GET.get("category")
    if category:
        posts_raw = posts_raw.filter(category=category)
    
    # Add translated fields to posts
    posts = []
    for post in posts_raw:
        post.translated_title = post.get_title(lang)
        post.translated_excerpt = post.get_excerpt(lang)
        post.translated_category = BlogPost.get_category_name(post.category, lang)
        posts.append(post)
    
    # Get translated categories for sidebar
    categories = [(key, BlogPost.get_category_name(key, lang)) for key, _ in BlogPost.CATEGORY_CHOICES]
    
    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        "posts": posts,
        "page_obj": page_obj,
        "categories": categories,
        "selected_category": category,
        "lang": lang,
    }
    return render(request, "core/page_blog.html", context)


def blog_detail(request, slug):
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    post = get_object_or_404(BlogPost, slug=slug)
    # Add translated fields
    post.translated_title = post.get_title(lang)
    post.translated_excerpt = post.get_excerpt(lang)
    post.translated_body = post.get_body(lang)
    post.translated_category = BlogPost.get_category_name(post.category, lang)
    post.translated_meta_title = post.get_meta_title(lang)
    post.translated_meta_description = post.get_meta_description(lang)
    post.translated_tags = post.get_tags_list(lang)
    
    return render(request, "core/blog_detail.html", {"post": post, "lang": lang})


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
    
    # Get contact gallery images from PageMedia
    contact_gallery_images = get_media('contact_gallery')
    contact_cta_left = get_media('contact_cta_left').first()
    contact_cta_right = get_media('contact_cta_right').first()
    
    return render(request, "core/contacts.html", {
        'success': success,
        'contact_gallery_images': contact_gallery_images,
        'contact_cta_left': contact_cta_left,
        'contact_cta_right': contact_cta_right,
    })


def pricing(request):
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    packages_raw = PricingPackage.objects.all()
    packages = []
    for pkg in packages_raw:
        pkg.translated_name = pkg.get_name(lang)
        pkg.translated_features = pkg.get_features(lang)
        pkg.translated_price = pkg.get_price(lang)
        pkg.translated_period = pkg.get_period(lang)
        packages.append(pkg)
    
    add_ons_raw = AddOnService.objects.all()
    add_ons = []
    for addon in add_ons_raw:
        addon.translated_name = addon.get_name(lang)
        addon.translated_description = addon.get_description(lang)
        addon.translated_price = addon.get_price(lang)
        add_ons.append(addon)
    
    return render(request, "core/pricing.html", {"packages": packages, "add_ons": add_ons, "lang": lang})


def rsvp(request):
    from django.utils.translation import get_language
    success = False
    error = None
    lang = get_language() or 'mk'
    addons_raw = AddOnService.objects.all().order_by('order')
    # Add translated name to each addon
    addons = []
    for addon in addons_raw:
        addon.translated_name = addon.get_name(lang)
        addons.append(addon)
    
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
    from django.utils.translation import get_language
    lang = get_language() or 'mk'
    
    faqs = FAQItem.objects.all().order_by('category', 'order')
    default_bg = "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80"
    
    # Get accommodation background from PageMedia
    faq_accommodation_media = get_media('faq_accommodation').first()
    accommodation_bg = faq_accommodation_media.image.url if faq_accommodation_media else default_bg
    
    # Get CTA images
    faq_cta_left = get_media('faq_cta_left').first()
    faq_cta_right = get_media('faq_cta_right').first()
    
    # Group FAQs by category with both key and translated name
    faq_categories = {}
    for faq in faqs:
        # Get translated category name
        translated_category = FAQItem.get_category_name(faq.category, lang)
        if translated_category not in faq_categories:
            faq_categories[translated_category] = {
                'key': faq.category,
                'faqs': []
            }
        faq_categories[translated_category]['faqs'].append(faq)
    
    return render(
        request,
        "core/faq.html",
        {
            "faq_categories": faq_categories,
            "accommodation_background": accommodation_bg,
            "faq_cta_left": faq_cta_left,
            "faq_cta_right": faq_cta_right,
            "lang": lang,
        },
    )


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    settings = SiteSettings.get_settings()
    return render(request, "core/product_detail.html", {"product": product, "site_settings": settings})


@require_POST
def like_post(request, post_id):
    """Like a blog post via AJAX"""
    post = get_object_or_404(BlogPost, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({'likes': post.likes})

# Create your views here.
