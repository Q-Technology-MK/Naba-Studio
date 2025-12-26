from django.contrib import admin
from django.db import models

from .models import (
    AddOnService, BlogPost, BlogTag, FAQItem, PageMedia, PortfolioItem, PricingPackage, Product, ProductImage, ProductReview, Service, 
    SiteContent, SiteSettings, PageText, VideoEmbed,
    HomeHeroMedia, HomeBrideGalleryMedia, HomeDressGalleryMedia, AboutPageMedia,
    ServicesPageMedia, ContactsPageMedia, FAQPageMedia, RSVPPageMedia
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "order")
    ordering = ("order", "title")
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("title", "subtitle", "description", "icon", "order"),
            "description": "Основен јазик за веб-страницата"
        }),
        ("Türkçe", {
            "fields": ("title_tr", "subtitle_tr", "description_tr"),
            "classes": ("collapse",),
            "description": "Türkçe içerik (opsiyonel)"
        }),
        ("Shqip", {
            "fields": ("title_sq", "subtitle_sq", "description_sq"),
            "classes": ("collapse",),
            "description": "Përmbajtja në shqip (opsionale)"
        }),
    )


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "featured", "year", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("featured", "year")
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("title", "slug", "summary", "description", "featured"),
            "description": "Основен јазик за веб-страницата"
        }),
        ("Türkçe", {
            "fields": ("title_tr", "summary_tr", "description_tr"),
            "classes": ("collapse",),
            "description": "Türkçe içerik (opsiyonel)"
        }),
        ("Shqip", {
            "fields": ("title_sq", "summary_sq", "description_sq"),
            "classes": ("collapse",),
            "description": "Përmbajtja në shqip (opsionale)"
        }),
        ("🖼️ Горсел", {
            "fields": ("image_url",),
            "description": "⚠️ Препорачана големина: 1200x800 пиксели"
        }),
        ("Детали", {
            "fields": ("year", "designer", "features")
        }),
        ("SEO - Македонски", {
            "fields": ("meta_title", "meta_description"),
            "classes": ("collapse",),
            "description": "Ако е празно, автоматски се генерира"
        }),
        ("SEO - Türkçe", {
            "fields": ("meta_title_tr", "meta_description_tr"),
            "classes": ("collapse",),
        }),
        ("SEO - Shqip", {
            "fields": ("meta_title_sq", "meta_description_sq"),
            "classes": ("collapse",),
        }),
    )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 3
    fields = ('image', 'is_primary', 'order', 'alt_text')
    ordering = ['-is_primary', 'order']
    verbose_name = "Ürün Resmi"
    verbose_name_plural = "📸 Ürün Resimleri (Max 3 adet, Önerilen: 600x800px, JPG/PNG/WEBP)"


class ProductReviewInlineForProduct(admin.TabularInline):
    model = ProductReview
    extra = 0
    fields = ('rating', 'reviewer_name', 'is_approved', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ['-created_at']
    verbose_name = "Değerlendirme"
    verbose_name_plural = "⭐ Ürün Değerlendirmeleri"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "category", "price", "in_stock", "is_featured", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("category", "in_stock", "is_featured")
    list_editable = ("is_featured",)
    inlines = [ProductImageInline, ProductReviewInlineForProduct]
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("name", "slug", "summary", "description", "category", "price", "in_stock", "is_featured"),
            "description": "Основен јазик за веб-страницата"
        }),
        ("Türkçe", {
            "fields": ("name_tr", "summary_tr", "description_tr"),
            "classes": ("collapse",),
            "description": "Türkçe içerik (opsiyonel)"
        }),
        ("Shqip", {
            "fields": ("name_sq", "summary_sq", "description_sq"),
            "classes": ("collapse",),
            "description": "Përmbajtja në shqip (opsionale)"
        }),
        ("🖼️ URL Слика (Опционално)", {
            "fields": ("image_url",),
            "classes": ("collapse",),
            "description": "⚠️ Користете го ова само ако не качувате слики горе. Препорачана големина: 600x800 пиксели"
        }),
    )


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ("name", "name_tr", "name_sq", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "name_tr", "name_sq")
    fieldsets = (
        ("Етикета / Etiket / Etiketa", {
            "fields": ("name", "name_tr", "name_sq", "slug"),
            "description": "Her dilde etiket adını girin. Slug otomatik oluşturulur."
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at", "likes", "get_tags_display")
    list_filter = ("category", "published_at", "blog_tags")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("blog_tags",)
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("title", "slug", "excerpt", "body", "published_at", "category"),
            "description": "Основен јазик за веб-страницата"
        }),
        ("Türkçe", {
            "fields": ("title_tr", "excerpt_tr", "body_tr"),
            "classes": ("collapse",),
            "description": "Türkçe içerik (opsiyonel)"
        }),
        ("Shqip", {
            "fields": ("title_sq", "excerpt_sq", "body_sq"),
            "classes": ("collapse",),
            "description": "Përmbajtja në shqip (opsionale)"
        }),
        ("Görsel", {
            "fields": ("hero_image",),
            "description": "⚠️ Önerilen boyut: 1200x675 piksel (16:9 yatay dikdörtgen)"
        }),
        ("🏷️ Etiketler (Çok Dilli)", {
            "fields": ("blog_tags",),
            "description": "Etiketleri seçin. Yeni etiket eklemek için önce 'Blog Etiketleri' bölümünden oluşturun."
        }),
        ("Etkileşim", {
            "fields": ("likes",)
        }),
        ("SEO - Македонски", {
            "fields": ("meta_title", "meta_description"),
            "classes": ("collapse",),
            "description": "Ако е празно, автоматски се генерира"
        }),
        ("SEO - Türkçe", {
            "fields": ("meta_title_tr", "meta_description_tr"),
            "classes": ("collapse",),
        }),
        ("SEO - Shqip", {
            "fields": ("meta_title_sq", "meta_description_sq"),
            "classes": ("collapse",),
        }),
    )
    
    def get_tags_display(self, obj):
        return ", ".join([tag.name for tag in obj.blog_tags.all()])
    get_tags_display.short_description = "Etiketler"


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ("question_mk", "category", "order")
    list_filter = ("category",)
    ordering = ("category", "order")
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("question_mk", "answer_mk"),
            "description": "Основен јазик за веб-страницата"
        }),
        ("Türkçe", {
            "fields": ("question_tr", "answer_tr"),
            "classes": ("collapse",),
            "description": "Türkçe soru ve cevap"
        }),
        ("Shqip", {
            "fields": ("question_sq", "answer_sq"),
            "classes": ("collapse",),
            "description": "Pyetja dhe përgjigja në shqip"
        }),
        ("Организација", {
            "fields": ("category",),
            "description": "Категоријата автоматски се доделува редослед"
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # New object
            # Auto-assign order based on category
            max_order = FAQItem.objects.filter(category=obj.category).aggregate(
                max_order=models.Max('order')
            )['max_order']
            obj.order = (max_order or 0) + 1
        super().save_model(request, obj, form, change)


@admin.register(PricingPackage)
class PricingPackageAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "period", "order", "is_featured")
    ordering = ("order", "name")
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("name", "price", "period", "features", "order", "is_featured")
        }),
        ("Türkçe", {
            "fields": ("name_tr", "period_tr", "features_tr"),
            "classes": ("collapse",)
        }),
        ("Shqip", {
            "fields": ("name_sq", "period_sq", "features_sq"),
            "classes": ("collapse",)
        }),
    )


@admin.register(AddOnService)
class AddOnServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "icon", "order")
    ordering = ("order", "name")
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("name", "description", "price", "icon", "order"),
            "description": "Основен јазик за веб-страницата"
        }),
        ("Türkçe", {
            "fields": ("name_tr", "description_tr", "price_tr"),
            "classes": ("collapse",),
            "description": "Türkçe içerik (opsiyonel)"
        }),
        ("Shqip", {
            "fields": ("name_sq", "description_sq", "price_sq"),
            "classes": ("collapse",),
            "description": "Përmbajtja në shqip (opsionale)"
        }),
    )


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("key",)
    search_fields = ("key", "content_mk")
    fieldsets = (
        ("Identifier", {
            "fields": ("key",)
        }),
        ("Македонски (Default)", {
            "fields": ("content_mk",)
        }),
        ("Türkçe", {
            "fields": ("content_tr",),
            "classes": ("collapse",)
        }),
        ("Shqip", {
            "fields": ("content_sq",),
            "classes": ("collapse",)
        }),
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Site Bilgileri", {
            "fields": ("site_name", "tagline")
        }),
        ("Logo & Favicon - Dosya Yükleme", {
            "fields": ("logo_file", "favicon_file"),
            "description": "⚠️ Logo: 200x60 piksel PNG/JPG | Favicon: 32x32 piksel .ico"
        }),
        ("Logo & Favicon - URL (Eski Yöntem)", {
            "fields": ("logo_url", "favicon_url"),
            "classes": ("collapse",),
            "description": "Bu alanlar kullanılmıyorsa, yukarıdaki dosya yükleme seçeneğini kullanın"
        }),
        ("Tema Renkleri", {
            "fields": ("color_primary", "color_secondary", "color_accent", "color_accent_dark", "color_text_soft"),
            "description": "Renkleri hex formatında girin (örn: #d86a5f)"
        }),
        ("İletişim Bilgileri", {
            "fields": ("address", "email", "phone")
        }),
        ("Sosyal Medya", {
            "fields": ("facebook_url", "instagram_url", "twitter_url", "pinterest_url", "youtube_url", "tiktok_url", "google_business_url"),
            "description": "Sadece URL'si olan sosyal medya hesapları footer'da görünür"
        }),
        ("SEO", {
            "fields": ("meta_description", "meta_keywords"),
            "description": "Site geneli SEO ayarları"
        }),
        ("Footer - Copyright Yazısı", {
            "fields": ("copyright_text_mk", "copyright_text_tr", "copyright_text_sq"),
            "description": "3 dil için copyright yazısı. Site dili değiştiğinde otomatik güncellenir"
        }),
        ("Footer - Ek Metin", {
            "fields": ("footer_text",),
            "classes": ("collapse",)
        }),
        ("Harita & Konum", {
            "fields": ("map_latitude", "map_longitude", "map_embed_code"),
            "description": "Naba Studio - Samoilova 90, Skopje Kale | 📍 Harita: https://maps.app.goo.gl/TnBQbTKjQFpx3DFN7"
        }),
        ("📧 Email / SMTP Ayarları (Google)", {
            "fields": ("email_enabled", "smtp_host", "smtp_port", "smtp_user", "smtp_password", "smtp_use_tls", "smtp_from_email"),
            "description": "Gmail SMTP için: Host: smtp.gmail.com | Port: 587 | TLS: True | Şifre: App Password kullanın (normal Gmail şifresi değil). App Password almak için: Google Account > Security > 2-Step Verification > App Passwords"
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class BaseSectionMediaAdmin(admin.ModelAdmin):
    """Base admin for section-specific media"""
    list_display = ("get_section_display", "image_preview", "size_guideline_display", "alt_text", "is_active", "order")
    list_editable = ("is_active", "order")
    ordering = ("order",)
    search_fields = ("alt_text", "title")
    
    # Subclasses should define these
    section_filter = []  # List of section keys to filter
    section_size_info = ""  # Size info for this section
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.section_filter:
            qs = qs.filter(section__in=self.section_filter)
        return qs
    
    def get_fieldsets(self, request, obj=None):
        return (
            ("📍 Görsel Konumu", {
                "fields": ("section", "order", "is_active"),
                "description": f"Bu bölüm için görsel yükleyin. Sıra numarası ile görüntülenme sırasını belirleyin."
            }),
            ("🖼️ Görsel Yükleme", {
                "fields": ("image",),
                "description": f"⚠️ ÖNERİLEN BOYUTLAR:\n{self.section_size_info}"
            }),
            ("📝 SEO & Erişilebilirlik", {
                "fields": ("alt_text", "title"),
                "classes": ("wide",),
                "description": "Alt text görsel yüklenemediğinde gösterilir."
            }),
        )
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 80px;" />'
        return '-'
    image_preview.short_description = "Önizleme"
    image_preview.allow_tags = True
    
    def size_guideline_display(self, obj):
        from .models import PageMedia
        guideline = PageMedia.SECTION_SIZE_GUIDELINES.get(obj.section, '')
        if guideline:
            return guideline.split(',')[0] if ',' in guideline else guideline[:30]
        return '-'
    size_guideline_display.short_description = "Önerilen Boyut"
    
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'section' and self.section_filter:
            kwargs['choices'] = [(k, v) for k, v in PageMedia.SECTION_CHOICES if k in self.section_filter]
        return super().formfield_for_choice_field(db_field, request, **kwargs)


@admin.register(HomeHeroMedia)
class HomeHeroMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['hero_home', 'hero_home_2', 'hero_home_stack_1', 'hero_home_stack_2', 'hero_home_floral']
    section_size_info = """• Hero 1 Arka Planı: 1920x1080px (Full HD), JPG/WebP, max 500KB
• Hero 2 Arka Planı: 1920x1080px (Full HD), JPG/WebP, max 500KB
• Stack Resim 1 (Sol): 400x500px (Dikey), JPG/WebP, max 200KB
• Stack Resim 2 (Sağ): 400x500px (Dikey), JPG/WebP, max 200KB
• Çiçek Dekorasyon: 300x300px (Kare), PNG şeffaf arka plan, max 150KB"""


@admin.register(HomeBrideGalleryMedia)
class HomeBrideGalleryMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['bride_gallery_1', 'bride_gallery_2', 'bride_gallery_3', 'bride_gallery_4', 'bride_gallery_5']
    section_size_info = """• Gelin Galerisi 1: 400x500px (Dikey), JPG/WebP, max 200KB
• Gelin Galerisi 2: 600x500px (Yatay/Geniş), JPG/WebP, max 250KB
• Gelin Galerisi 3: 400x500px (Dikey), JPG/WebP, max 200KB
• Gelin Galerisi 4: 400x500px (Dikey), JPG/WebP, max 200KB
• Gelin Galerisi 5: 600x500px (Yatay/Geniş), JPG/WebP, max 250KB"""


@admin.register(HomeDressGalleryMedia)
class HomeDressGalleryMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['dress_gallery_mini_1', 'dress_gallery_mini_2', 'dress_gallery_mini_3']
    section_size_info = """• Mini Resim 1: 400x400px (Kare), JPG/WebP, max 150KB
• Mini Resim 2: 420x420px (Kare), JPG/WebP, max 150KB
• Mini Resim 3: 380x380px (Kare), JPG/WebP, max 150KB"""


@admin.register(AboutPageMedia)
class AboutPageMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['about_hero']
    section_size_info = """• Hero Arka Planı: 1920x800px (Geniş Banner), JPG/WebP, max 400KB"""


@admin.register(ServicesPageMedia)
class ServicesPageMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['services_banner', 'services_gallery']
    section_size_info = """• Banner Arka Planı: 1920x600px (Banner), JPG/WebP, max 400KB
• Galeri Resimleri: 400x500px (Dikey), JPG/WebP, max 200KB - Birden fazla yükleyebilirsiniz"""


@admin.register(ContactsPageMedia)
class ContactsPageMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['contact_gallery', 'contact_cta_left', 'contact_cta_right']
    section_size_info = """• Galeri Resimleri: 400x500px (Dikey), JPG/WebP, max 200KB - Birden fazla yükleyebilirsiniz
• CTA Sol Resim: 400x500px (Dikey), JPG/WebP, max 200KB - Showcase bölümü sol resim
• CTA Sağ Resim: 400x500px (Dikey), JPG/WebP, max 200KB - Showcase bölümü sağ resim"""


@admin.register(FAQPageMedia)
class FAQPageMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['faq_accommodation', 'faq_cta_left', 'faq_cta_right']
    section_size_info = """• Konaklama Görselleri: 800x600px (Yatay), JPG/WebP, max 300KB
• CTA Sol Resim: 400x500px (Dikey), JPG/WebP, max 200KB - Alt showcase bölümü sol resim
• CTA Sağ Resim: 400x500px (Dikey), JPG/WebP, max 200KB - Alt showcase bölümü sağ resim"""


@admin.register(RSVPPageMedia)
class RSVPPageMediaAdmin(BaseSectionMediaAdmin):
    section_filter = ['rsvp_hero']
    section_size_info = """• Hero Arka Planı: 1920x800px (Geniş Banner), JPG/WebP, max 400KB"""


@admin.register(PageText)
class PageTextAdmin(admin.ModelAdmin):
    list_display = ("get_section_display",)
    fieldsets = (
        ("Bölüm Seçimi", {
            "fields": ("section",)
        }),
        ("Македонски (Default)", {
            "fields": ("content_mk",)
        }),
        ("Türkçe", {
            "fields": ("content_tr",),
            "classes": ("collapse",)
        }),
        ("Shqip", {
            "fields": ("content_sq",),
            "classes": ("collapse",)
        }),
    )


@admin.register(VideoEmbed)
class VideoEmbedAdmin(admin.ModelAdmin):
    list_display = ("get_section_display", "title", "youtube_id")
    fieldsets = (
        ("Video Bilgileri", {
            "fields": ("section", "title")
        }),
        ("YouTube ID", {
            "fields": ("youtube_id",),
            "description": "YouTube URL'sinin ?v= sonrası yazın. Örn: dQw4w9WgXcQ"
        }),
    )


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 0
    fields = ('rating', 'reviewer_name', 'reviewer_email', 'comment', 'is_approved', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ['-created_at']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "rating", "reviewer_name", "is_approved", "created_at")
    list_filter = ("is_approved", "rating", "product")
    list_editable = ("is_approved",)
    search_fields = ("reviewer_name", "reviewer_email", "comment")
    ordering = ["-created_at"]
    actions = ["approve_reviews", "reject_reviews"]
    
    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} değerlendirme onaylandı.")
    approve_reviews.short_description = "Seçili değerlendirmeleri onayla"
    
    def reject_reviews(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f"{queryset.count()} değerlendirme reddedildi.")
    reject_reviews.short_description = "Seçili değerlendirmeleri reddet"

