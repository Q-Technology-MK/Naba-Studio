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
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
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
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=220)
    body = models.TextField()
    published_at = models.DateField()
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
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.question


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
    
    # Logo
    logo_url = models.URLField(blank=True, help_text="Logo resmi URL'si (Önerilen boyut: 200x60 piksel)")
    favicon_url = models.URLField(blank=True, help_text="Favicon URL'si (Önerilen boyut: 32x32 piksel)")
    
    # Theme Colors
    color_primary = models.CharField(max_length=7, default="#fef1eb", help_text="Background color (hex)")
    color_secondary = models.CharField(max_length=7, default="#191919", help_text="Main text color (hex)")
    color_accent = models.CharField(max_length=7, default="#d86a5f", help_text="Accent/button color (hex)")
    color_accent_dark = models.CharField(max_length=7, default="#a84334", help_text="Accent hover color (hex)")
    color_text_soft = models.CharField(max_length=7, default="#6c6c6c", help_text="Secondary text color (hex)")
    
    # Contact Info
    address = models.TextField(blank=True, default="Pariser Platz 3, 10117 Berlin")
    email = models.EmailField(blank=True, default="atelier@ankora.com")
    phone = models.CharField(max_length=30, blank=True, default="+49 30 1234 5678")
    
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
