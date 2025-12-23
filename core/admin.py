from django.contrib import admin

from .models import (
    AddOnService, BlogPost, FAQItem, PageMedia, PortfolioItem, PricingPackage, Product, Service, 
    SiteContent, SiteSettings, PageText, VideoEmbed
)


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
    list_display = ("title", "category", "published_at", "likes")
    list_filter = ("category", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        ("Temel Bilgiler", {
            "fields": ("title", "slug", "excerpt", "body", "published_at", "category")
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
            "description": "Сорула и одговорот на турски јазик"
        }),
        ("Shqip", {
            "fields": ("question_sq", "answer_sq"),
            "classes": ("collapse",),
            "description": "Pyetja dhe përgjigja në shqip"
        }),
        ("Organizacija", {
            "fields": ("category", "order"),
            "description": "Категорија и редослед"
        }),
    )


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
        ("🎁 Premium Features", {
            "fields": (
                "free_consultation", "design_sketch", "measurements", "trials",
                "express_delivery", "gift_accessories", "design_modifications",
                "fabric_consultation", "final_steaming", "storage_bag", "online_meeting"
            ),
            "description": "Paket ile birlikte sunulacak hizmetleri seçin. Bu özellikler otomatik olarak pricing sayfasında gösterilecektir."
        }),
    )


@admin.register(AddOnService)
class AddOnServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "icon", "order")
    ordering = ("order", "name")
    fieldsets = (
        ("Македонски (Default)", {
            "fields": ("name", "description", "price", "icon", "order")
        }),
        ("Türkçe", {
            "fields": ("name_tr", "description_tr"),
            "classes": ("collapse",)
        }),
        ("Shqip", {
            "fields": ("name_sq", "description_sq"),
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
            "fields": ("facebook_url", "instagram_url", "twitter_url", "pinterest_url", "youtube_url", "tiktok_url"),
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
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PageMedia)
class PageMediaAdmin(admin.ModelAdmin):
    list_display = ("get_section_display", "alt_text", "is_active", "order")
    list_filter = ("section", "is_active")
    list_editable = ("is_active",)
    ordering = ("section", "order")
    search_fields = ("alt_text", "title")
    
    fieldsets = (
        ("📍 Bölüm & Sıralama", {
            "fields": ("section", "order", "is_active"),
            "description": "Görselin hangi sayfada ve hangi sırada gösterileceğini belirtin"
        }),
        ("🖼️ Görsel Yükleme", {
            "fields": ("image",),
            "description": "⚠️ Çok önemli: Bölümünüzün gerektirdiği ölçülerde yükleyiniz (aşağıda belirtilmiştir)"
        }),
        ("📝 SEO & Erişilebilirlik", {
            "fields": ("alt_text", "title"),
            "classes": ("wide",),
            "description": "Alt text görsel yüklenemediğinde gösterilir. Title SEO için önemlidir."
        }),
        ("📏 Ölçüler & Format Bilgisi", {
            "fields": ("description",),
            "classes": ("wide",),
            "description": "Bu alana görselin gerekli ölçülerini ve formatını yazınız. Örn: 1200x800px, JPG, max 500KB"
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        # section'u seçtikten sonra değiştirilemesin diye
        if obj:
            return ['section']
        return []


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

