from django.db import models
from django.urls import reverse


class Service(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="✶")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(
        blank=True,
        default="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=1200&q=80",
        help_text="Önerilen boyut: 1200x800 piksel (yatay dikdörtgen)"
    )
    created_at = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    year = models.CharField(max_length=10, blank=True, default="2024", verbose_name="Yıl")
    designer = models.CharField(max_length=100, blank=True, verbose_name="Tasarımcı")
    features = models.TextField(blank=True, help_text="Her satıra bir özellik yazın", verbose_name="Özellikler")
    # SEO
    meta_title = models.CharField(max_length=70, blank=True, help_text="SEO başlığı (max 70 karakter, boş bırakılırsa title kullanılır)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO açıklaması (max 160 karakter)")

    class Meta:
        ordering = ["-featured", "-created_at", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio_detail", kwargs={"slug": self.slug})

    def get_features_list(self):
        return [f.strip() for f in self.features.split("\n") if f.strip()]


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('A Kesim', 'A Kesim'),
        ('Prenses', 'Prenses'),
        ('Balık', 'Balık'),
        ('Minimal', 'Minimal'),
        ('Klasik', 'Klasik'),
    )
    
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='A Kesim',
        verbose_name="Kategori"
    )
    summary = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=60, blank=True, default="Özel teklif")
    image_url = models.URLField(
        blank=True,
        default="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=900&q=80",
        help_text="Önerilen boyut: 600x800 piksel (dikey dikdörtgen)"
    )
    created_at = models.DateField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})


class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('Gelinlik Tasarımları', 'Gelinlik Tasarımları'),
        ('Kişisel Hikayeler', 'Kişisel Hikayeler'),
        ('Moda Trendleri', 'Moda Trendleri'),
        ('Bakım & Tavsiyeleri', 'Bakım & Tavsiyeleri'),
        ('Atelier Haberleri', 'Atelier Haberleri'),
    )
    
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField()
    body = models.TextField()
    published_at = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Atelier Haberleri', help_text="Blog yazısının kategorisini seçin")
    hero_image = models.URLField(
        blank=True,
        default="https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?auto=format&fit=crop&w=1200&q=80",
        help_text="Önerilen boyut: 1200x675 piksel (16:9 yatay dikdörtgen)"
    )
    tags = models.CharField(max_length=200, blank=True, help_text="Virgülle ayırarak etiketler girin")
    likes = models.PositiveIntegerField(default=0)
    # SEO
    meta_title = models.CharField(max_length=70, blank=True, help_text="SEO başlığı (max 70 karakter, boş bırakılırsa title kullanılır)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO açıklaması (max 160 karakter)")

    class Meta:
        ordering = ["-published_at", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]


class FAQItem(models.Model):
    CATEGORY_CHOICES = (
        ('Booking & Trials', 'Booking & Trials'),
        ('Design & Customization', 'Design & Customization'),
        ('Timeline & Pricing', 'Timeline & Pricing'),
        ('Delivery & Care', 'Delivery & Care'),
        ('Products & Materials', 'Products & Materials'),
        ('Contact & Information', 'Contact & Information'),
    )
    
    # Macedonian (default language)
    question_mk = models.CharField(max_length=200)
    answer_mk = models.TextField()
    
    # Turkish
    question_tr = models.CharField(max_length=200, blank=True, verbose_name="Soru (Türkçe)")
    answer_tr = models.TextField(blank=True, verbose_name="Cevap (Türkçe)")
    
    # Albanian
    question_sq = models.CharField(max_length=200, blank=True, verbose_name="Pyetja (Shqip)")
    answer_sq = models.TextField(blank=True, verbose_name="Përgjigja (Shqip)")
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Booking & Trials', help_text="Kategorija / Category / Kategori")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order"]

    def __str__(self):
        return self.question_mk

    def get_question(self, lang='mk'):
        """Get question in specified language"""
        field = f'question_{lang}'
        return getattr(self, field, self.question_mk)
    
    def get_answer(self, lang='mk'):
        """Get answer in specified language"""
        field = f'answer_{lang}'
        return getattr(self, field, self.answer_mk)


class PricingPackage(models.Model):
    name = models.CharField(max_length=100)
    name_tr = models.CharField(max_length=100, blank=True, verbose_name="Ad (Türkçe)")
    name_sq = models.CharField(max_length=100, blank=True, verbose_name="Emri (Shqip)")
    price = models.CharField(max_length=50)
    period = models.CharField(max_length=50, default="Per/Month")
    period_tr = models.CharField(max_length=50, blank=True, verbose_name="Periyot (Türkçe)")
    period_sq = models.CharField(max_length=50, blank=True, verbose_name="Periudha (Shqip)")
    features = models.TextField(help_text="Her satıra bir özellik yazın")
    features_tr = models.TextField(blank=True, verbose_name="Özellikler (Türkçe)")
    features_sq = models.TextField(blank=True, verbose_name="Veçoritë (Shqip)")
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    def get_features_list(self):
        return [f.strip() for f in self.features.split("\n") if f.strip()]


class AddOnService(models.Model):
    """Add-on hizmetler ve opsiyonel paketler"""
    name = models.CharField(max_length=100)
    name_tr = models.CharField(max_length=100, blank=True, verbose_name="Ad (Türkçe)")
    name_sq = models.CharField(max_length=100, blank=True, verbose_name="Emri (Shqip)")
    description = models.TextField(blank=True, verbose_name="Açıklama")
    description_tr = models.TextField(blank=True, verbose_name="Açıklama (Türkçe)")
    description_sq = models.TextField(blank=True, verbose_name="Përshkrimi (Shqip)")
    price = models.CharField(max_length=50, blank=True, verbose_name="Fiyat (Opsiyonel)")
    icon = models.CharField(max_length=10, default="✨", help_text="Emoji ikon (ör: ✨, 🎨, 📏, 👗, ⚡, 🎁, ✂️, 🧵, ♨️, 📦, 💻)")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.icon} {self.name}"


class SiteContent(models.Model):
    """Admin-manageable translatable content for static pages."""
    key = models.CharField(max_length=100, unique=True, help_text="Unique identifier for this content")
    content_mk = models.TextField(verbose_name="Содржина (Македонски)")
    content_tr = models.TextField(blank=True, verbose_name="İçerik (Türkçe)")
    content_sq = models.TextField(blank=True, verbose_name="Përmbajtja (Shqip)")

    class Meta:
        verbose_name = "Site Content"
        verbose_name_plural = "Site Contents"

    def __str__(self):
        return self.key

    def get_content(self, lang='mk'):
        if lang == 'tr' and self.content_tr:
            return self.content_tr
        elif lang == 'sq' and self.content_sq:
            return self.content_sq
        return self.content_mk


class SiteSettings(models.Model):
    """Admin-manageable site settings including theme colors."""
    site_name = models.CharField(max_length=100, default="Ankora Atelier")
    tagline = models.CharField(max_length=200, default="Bridal & Couture Studio")
    
    # Logo & Favicon - File uploads
    logo_file = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Logo resmi (Önerilen boyut: 200x60 piksel)")
    favicon_file = models.FileField(upload_to='favicons/', blank=True, null=True, help_text="Favicon dosyası (Önerilen boyut: 32x32 piksel, .ico formatında)")
    
    # Legacy URL fields (backward compatibility)
    logo_url = models.URLField(blank=True, help_text="Logo resmi URL'si (Önerilen boyut: 200x60 piksel)")
    favicon_url = models.URLField(blank=True, help_text="Favicon URL'si (Önerilen boyut: 32x32 piksel)")
    
    # Theme Colors
    color_primary = models.CharField(max_length=7, default="#fef1eb", help_text="Background color (hex)")
    color_secondary = models.CharField(max_length=7, default="#191919", help_text="Main text color (hex)")
    color_accent = models.CharField(max_length=7, default="#d86a5f", help_text="Accent/button color (hex)")
    color_accent_dark = models.CharField(max_length=7, default="#a84334", help_text="Accent hover color (hex)")
    color_text_soft = models.CharField(max_length=7, default="#6c6c6c", help_text="Secondary text color (hex)")
    
    # Contact Info
    address = models.TextField(blank=True, default="Samoilova 90, Skopje Kale")
    email = models.EmailField(blank=True, default="nabastudio25@gmail.com")
    phone = models.CharField(max_length=30, blank=True, default="070 666 567")
    
    # Social Links
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    pinterest_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    
    # SEO
    meta_description = models.TextField(blank=True, max_length=160, help_text="Site açıklaması (SEO için, max 160 karakter)")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Anahtar kelimeler, virgülle ayırın")
    
    # Footer
    footer_text = models.TextField(blank=True, default="", help_text="Footer'da görünecek ek metin")
    copyright_text_mk = models.CharField(max_length=255, blank=True, default="© 2025 Naba Studio by Semma. Сите права се задржаа.", help_text="Copyright text (Macedonian)")
    copyright_text_tr = models.CharField(max_length=255, blank=True, default="© 2025 Naba Studio by Semma. Tüm Hakları Saklıdır.", help_text="Copyright text (Turkish)")
    copyright_text_sq = models.CharField(max_length=255, blank=True, default="© 2025 Naba Studio by Semma. Të gjitha të drejtat e rezervuara.", help_text="Copyright text (Albanian)")
    
    # Maps & Location
    map_latitude = models.DecimalField(max_digits=9, decimal_places=6, default="41.997335", help_text="Naba Studio Samoilova 90 enlemi: 41.997335")
    map_longitude = models.DecimalField(max_digits=9, decimal_places=6, default="21.428057", help_text="Naba Studio Samoilova 90 boylamı: 21.428057")
    map_embed_code = models.TextField(blank=True, help_text="Google Maps embed kod: https://maps.app.goo.gl/TnBQbTKjQFpx3DFN7")
    
    # SMTP / Email Settings (Google SMTP)
    smtp_host = models.CharField(max_length=255, default="smtp.gmail.com", help_text="SMTP sunucu adresi (Gmail: smtp.gmail.com)")
    smtp_port = models.PositiveIntegerField(default=587, help_text="SMTP port numarası (Gmail TLS: 587)")
    smtp_user = models.EmailField(blank=True, help_text="SMTP kullanıcı adı (Gmail adresi)")
    smtp_password = models.CharField(max_length=255, blank=True, help_text="SMTP şifresi (Gmail App Password)")
    smtp_use_tls = models.BooleanField(default=True, help_text="TLS kullan (Gmail için True)")
    smtp_from_email = models.EmailField(blank=True, help_text="Gönderen email adresi (genellikle SMTP kullanıcısı ile aynı)")
    email_enabled = models.BooleanField(default=False, help_text="Email gönderimini aktif et")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
    
    def get_logo_url(self):
        """Get logo URL from file or legacy URL field"""
        if self.logo_file:
            return self.logo_file.url
        return self.logo_url
    
    def get_favicon_url(self):
        """Get favicon URL from file or legacy URL field"""
        if self.favicon_file:
            return self.favicon_file.url
        return self.favicon_url
    
    def get_map_embed_url(self):
        """Generate Google Maps embed URL from coordinates if custom code not provided"""
        if self.map_embed_code:
            return self.map_embed_code
        # Generate from coordinates - proper Google Maps embed URL
        return f'<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2976.1498234!2d{self.map_longitude}!3d{self.map_latitude}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1354586c8b8d7d4d%3A0x8f8f8f8f8f8f8f8f!2sSamoilova%2090%2C%20Skopje!5e0!3m2!1sen!2sus!4v1702740000000" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'


class PageMedia(models.Model):
    """Yönetilebilir görseller - Sayfadaki tüm resimler buradan kontrol edilir"""
    SECTION_CHOICES = [
        # HOME PAGE
        ('hero_home', 'Anasayfa - Hero 1 Arka Planı'),
        ('hero_home_2', 'Anasayfa - Hero 2 Arka Planı'),
        ('hero_home_stack_1', 'Anasayfa - Hero 2 Stack Resim 1'),
        ('hero_home_stack_2', 'Anasayfa - Hero 2 Stack Resim 2'),
        ('hero_home_floral', 'Anasayfa - Hero 2 Çiçek Dekorasyon'),
        ('dress_gallery_mini_1', 'Anasayfa - Dress Gallery Mini Resim 1'),
        ('dress_gallery_mini_2', 'Anasayfa - Dress Gallery Mini Resim 2'),
        ('dress_gallery_mini_3', 'Anasayfa - Dress Gallery Mini Resim 3'),
        ('bride_gallery_1', 'Anasayfa - Gelin Galerisi Resim 1'),
        ('bride_gallery_2', 'Anasayfa - Gelin Galerisi Resim 2'),
        ('bride_gallery_3', 'Anasayfa - Gelin Galerisi Resim 3'),
        ('bride_gallery_4', 'Anasayfa - Gelin Galerisi Resim 4'),
        ('bride_gallery_5', 'Anasayfa - Gelin Galerisi Resim 5'),
        
        # ABOUT PAGE
        ('about_hero', 'Hakkımızda - Hero Arka Planı'),
        
        # SERVICES PAGE
        ('services_banner', 'Hizmetler - Banner Arka Planı'),
        
        # CONTACTS PAGE
        ('contact_gallery', 'İletişim - Galeri Resimleri'),
        
        # FAQ PAGE
        ('faq_accommodation', 'SSS - Konaklama Resimleri'),
        
        # PORTFOLIO PAGE
        ('portfolio_showcase', 'Portfolio - Galerideki Resimler'),
        
        # RSVP PAGE
        ('rsvp_hero', 'RSVP - Hero Arka Planı'),
    ]
    
    section = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES,
        verbose_name="Bölüm"
    )
    image = models.ImageField(
        upload_to='page_media/',
        help_text="Görsel dosyasını yükleyin (.jpg, .png, .webp)"
    )
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Alt Text (SEO & Erişilebilirlik)",
        help_text="Görselin açıklaması (görsel yüklenemediğinde gösterilir)"
    )
    title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Başlık",
        help_text="Bu görsele ait açıklayıcı başlık (opsiyonel)"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Ölçüler & Format Bilgisi",
        help_text="Bu görsel için gerekli boyut ve formatı belirtin. Örn: 1200x800px, JPG, max 500KB"
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Sıra",
        help_text="Aynı bölümde birden çok görsel varsa görüntülenme sırası"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Aktif",
        help_text="Pasif görseller sayfada gösterilmez"
    )
    
    class Meta:
        ordering = ['section', 'order']
        verbose_name = "Sayfa Görseli"
        verbose_name_plural = "Sayfa Görselleri"
        unique_together = [['section', 'order']]
    
    def __str__(self):
        return f"{self.get_section_display()} - #{self.order}"


class PageText(models.Model):
    """Manageable text content for static sections"""
    SECTION_CHOICES = [
        ('hero_home_title', 'Anasayfa Hero Başlık'),
        ('hero_home_subtitle', 'Anasayfa Hero Alt Başlık'),
        ('hero_home_desc', 'Anasayfa Hero Açıklama'),
        ('hero_home_hours', 'Anasayfa Çalışma Saatleri'),
        ('hero2_title', 'Hero 2 Başlık'),
        ('hero2_desc', 'Hero 2 Açıklama'),
        ('about_title', 'Hakkımızda Başlık'),
        ('about_desc', 'Hakkımızda Açıklama'),
        ('about_hours', 'Hakkımızda Çalışma Saatleri'),
        ('faq_questions', 'SSS Soruları'),
        ('rsvp_title', 'RSVP Başlık'),
        ('rsvp_desc', 'RSVP Açıklama'),
    ]
    
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, unique=True)
    content_mk = models.TextField(verbose_name="İçerik (Македонски)")
    content_tr = models.TextField(blank=True, verbose_name="İçerik (Türkçe)")
    content_sq = models.TextField(blank=True, verbose_name="Përmbajtja (Shqip)")
    
    class Meta:
        verbose_name = "Page Text"
        verbose_name_plural = "Page Texts"
    
    def __str__(self):
        return self.get_section_display()
    
    def get_content(self, lang='mk'):
        if lang == 'tr' and self.content_tr:
            return self.content_tr
        elif lang == 'sq' and self.content_sq:
            return self.content_sq
        return self.content_mk


class VideoEmbed(models.Model):
    """Manageable video embeds for different pages"""
    SECTION_CHOICES = [
        ('home', 'Anasayfa'),
        ('about', 'Hakkımızda'),
        ('services', 'Hizmetler'),
    ]
    
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, unique=True)
    youtube_id = models.CharField(max_length=20, help_text="YouTube video ID (url'nin ?v= sonrası)")
    title = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = "Video Embed"
        verbose_name_plural = "Video Embeds"
    
    def __str__(self):
        return f"{self.get_section_display()} - {self.title}"
    
    def get_embed_url(self):
        return f"https://www.youtube.com/embed/{self.youtube_id}?rel=0&autoplay=0&modestbranding=1"

