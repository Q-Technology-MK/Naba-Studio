from django.contrib import admin

from .models import BlogPost, FAQItem, PortfolioItem, PricingPackage, Product, Service, SiteContent, SiteSettings


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "order")
    ordering = ("order", "title")


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "featured", "year", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("featured", "year")
    fieldsets = (
        ("Temel Bilgiler", {
            "fields": ("title", "slug", "summary", "description", "featured")
        }),
        ("Görsel", {
            "fields": ("image_url",),
            "description": "⚠️ Önerilen boyut: 1200x800 piksel (yatay dikdörtgen)"
        }),
        ("Detaylar", {
            "fields": ("year", "designer", "features")
        }),
        ("SEO", {
            "fields": ("meta_title", "meta_description"),
            "classes": ("collapse",),
            "description": "Boş bırakılırsa otomatik oluşturulur"
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "in_stock", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        ("Temel Bilgiler", {
            "fields": ("name", "slug", "summary", "description", "price", "in_stock")
        }),
        ("Görsel", {
            "fields": ("image_url",),
            "description": "⚠️ Önerilen boyut: 600x800 piksel (dikey dikdörtgen)"
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at", "likes")
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Temel Bilgiler", {
            "fields": ("title", "slug", "excerpt", "body", "published_at")
        }),
        ("Görsel", {
            "fields": ("hero_image",),
            "description": "⚠️ Önerilen boyut: 1200x675 piksel (16:9 yatay dikdörtgen)"
        }),
        ("Etiketler & Etkileşim", {
            "fields": ("tags", "likes")
        }),
        ("SEO", {
            "fields": ("meta_title", "meta_description"),
            "classes": ("collapse",),
            "description": "Boş bırakılırsa otomatik oluşturulur"
        }),
    )


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ("question", "order")


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
        ("Logo & Favicon", {
            "fields": ("logo_url", "favicon_url"),
            "description": "⚠️ Logo: 200x60 piksel | Favicon: 32x32 piksel"
        }),
        ("Tema Renkleri", {
            "fields": ("color_primary", "color_secondary", "color_accent", "color_accent_dark", "color_text_soft"),
            "description": "Renkleri hex formatında girin (örn: #d86a5f)"
        }),
        ("İletişim Bilgileri", {
            "fields": ("address", "email", "phone")
        }),
        ("Sosyal Medya", {
            "fields": ("facebook_url", "instagram_url", "twitter_url", "pinterest_url", "youtube_url", "tiktok_url"),
            "description": "Sadece URL'si olan sosyal medya hesapları footer'da görünür"
        }),
        ("SEO", {
            "fields": ("meta_description", "meta_keywords"),
            "description": "Site geneli SEO ayarları"
        }),
        ("Footer", {
            "fields": ("footer_text",),
            "classes": ("collapse",)
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
