from django.db import models
from django.urls import reverse


class BlogTag(models.Model):
    """Çok dilli blog etiketleri - Admin'den yönetilebilir"""
    name = models.CharField(max_length=50, verbose_name="Етикета (Македонски)")
    name_tr = models.CharField(max_length=50, blank=True, verbose_name="Etiket (Türkçe)")
    name_sq = models.CharField(max_length=50, blank=True, verbose_name="Etiketa (Shqip)")
    slug = models.SlugField(unique=True, help_text="URL için benzersiz tanımlayıcı")
    
    class Meta:
        ordering = ['name']
        verbose_name = "Blog Etiketi"
        verbose_name_plural = "Blog Etiketleri"
    
    def __str__(self):
        return self.name
    
    def get_name(self, lang='mk'):
        """Get tag name in specified language"""
        if lang == 'tr' and self.name_tr:
            return self.name_tr
        elif lang == 'sq' and self.name_sq:
            return self.name_sq
        return self.name


class Service(models.Model):
    # Macedonian (default)
    title = models.CharField(max_length=100, verbose_name="Наслов (Македонски)")
    subtitle = models.CharField(max_length=150, blank=True, verbose_name="Поднаслов (Македонски)")
    description = models.TextField(verbose_name="Опис (Македонски)")
    
    # Turkish
    title_tr = models.CharField(max_length=100, blank=True, verbose_name="Başlık (Türkçe)")
    subtitle_tr = models.CharField(max_length=150, blank=True, verbose_name="Alt Başlık (Türkçe)")
    description_tr = models.TextField(blank=True, verbose_name="Açıklama (Türkçe)")
    
    # Albanian
    title_sq = models.CharField(max_length=100, blank=True, verbose_name="Titulli (Shqip)")
    subtitle_sq = models.CharField(max_length=150, blank=True, verbose_name="Nëntitulli (Shqip)")
    description_sq = models.TextField(blank=True, verbose_name="Përshkrimi (Shqip)")
    
    icon = models.CharField(max_length=50, default="✶")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
    
    def get_title(self, lang='mk'):
        if lang == 'tr' and self.title_tr:
            return self.title_tr
        elif lang == 'sq' and self.title_sq:
            return self.title_sq
        return self.title
    
    def get_subtitle(self, lang='mk'):
        if lang == 'tr' and self.subtitle_tr:
            return self.subtitle_tr
        elif lang == 'sq' and self.subtitle_sq:
            return self.subtitle_sq
        return self.subtitle
    
    def get_description(self, lang='mk'):
        if lang == 'tr' and self.description_tr:
            return self.description_tr
        elif lang == 'sq' and self.description_sq:
            return self.description_sq
        return self.description


class PortfolioItem(models.Model):
    # Macedonian (default)
    title = models.CharField(max_length=120, verbose_name="Наслов (Македонски)")
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=200, verbose_name="Резиме (Македонски)")
    description = models.TextField(verbose_name="Опис (Македонски)")
    
    # Turkish
    title_tr = models.CharField(max_length=120, blank=True, verbose_name="Başlık (Türkçe)")
    summary_tr = models.CharField(max_length=200, blank=True, verbose_name="Özet (Türkçe)")
    description_tr = models.TextField(blank=True, verbose_name="Açıklama (Türkçe)")
    
    # Albanian
    title_sq = models.CharField(max_length=120, blank=True, verbose_name="Titulli (Shqip)")
    summary_sq = models.CharField(max_length=200, blank=True, verbose_name="Përmbledhja (Shqip)")
    description_sq = models.TextField(blank=True, verbose_name="Përshkrimi (Shqip)")
    
    image_url = models.URLField(
        blank=True,
        default="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=1200&q=80",
        help_text="Önerilen boyut: 1200x800 piksel (yatay dikdörtgen)"
    )
    created_at = models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    year = models.CharField(max_length=10, blank=True, default="2024", verbose_name="Година")
    designer = models.CharField(max_length=100, blank=True, verbose_name="Дизајнер")
    features = models.TextField(blank=True, help_text="Her satıra bir özellik yazın", verbose_name="Карактеристики")
    # SEO - Macedonian
    meta_title = models.CharField(max_length=70, blank=True, verbose_name="SEO Наслов (Македонски)", help_text="Max 70 карактери")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="SEO Опис (Македонски)", help_text="Max 160 карактери")
    # SEO - Turkish
    meta_title_tr = models.CharField(max_length=70, blank=True, verbose_name="SEO Başlık (Türkçe)", help_text="Max 70 karakter")
    meta_description_tr = models.CharField(max_length=160, blank=True, verbose_name="SEO Açıklama (Türkçe)", help_text="Max 160 karakter")
    # SEO - Albanian
    meta_title_sq = models.CharField(max_length=70, blank=True, verbose_name="SEO Titulli (Shqip)", help_text="Max 70 karaktere")
    meta_description_sq = models.CharField(max_length=160, blank=True, verbose_name="SEO Përshkrimi (Shqip)", help_text="Max 160 karaktere")

    class Meta:
        ordering = ["-featured", "-created_at", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio_detail", kwargs={"slug": self.slug})

    def get_features_list(self):
        return [f.strip() for f in self.features.split("\n") if f.strip()]
    
    def get_title(self, lang='mk'):
        if lang == 'tr' and self.title_tr:
            return self.title_tr
        elif lang == 'sq' and self.title_sq:
            return self.title_sq
        return self.title
    
    def get_summary(self, lang='mk'):
        if lang == 'tr' and self.summary_tr:
            return self.summary_tr
        elif lang == 'sq' and self.summary_sq:
            return self.summary_sq
        return self.summary
    
    def get_description(self, lang='mk'):
        if lang == 'tr' and self.description_tr:
            return self.description_tr
        elif lang == 'sq' and self.description_sq:
            return self.description_sq
        return self.description
    
    def get_meta_title(self, lang='mk'):
        if lang == 'tr' and self.meta_title_tr:
            return self.meta_title_tr
        elif lang == 'sq' and self.meta_title_sq:
            return self.meta_title_sq
        return self.meta_title or self.title
    
    def get_meta_description(self, lang='mk'):
        if lang == 'tr' and self.meta_description_tr:
            return self.meta_description_tr
        elif lang == 'sq' and self.meta_description_sq:
            return self.meta_description_sq
        return self.meta_description or self.summary


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('a_line', 'А-линија'),
        ('princess', 'Принцеза'),
        ('mermaid', 'Русалка'),
        ('minimal', 'Минимал'),
        ('classic', 'Класик'),
    )
    
    CATEGORY_TRANSLATIONS = {
        'a_line': {'mk': 'А-линија', 'tr': 'A Kesim', 'sq': 'A-linjë'},
        'princess': {'mk': 'Принцеза', 'tr': 'Prenses', 'sq': 'Princeshë'},
        'mermaid': {'mk': 'Русалка', 'tr': 'Balık', 'sq': 'Sirenë'},
        'minimal': {'mk': 'Минимал', 'tr': 'Minimal', 'sq': 'Minimale'},
        'classic': {'mk': 'Класик', 'tr': 'Klasik', 'sq': 'Klasike'},
    }
    
    @classmethod
    def get_category_name(cls, category_key, lang='mk'):
        """Get translated category name"""
        if category_key in cls.CATEGORY_TRANSLATIONS:
            return cls.CATEGORY_TRANSLATIONS[category_key].get(lang, cls.CATEGORY_TRANSLATIONS[category_key]['mk'])
        return category_key
    
    # Macedonian (default)
    name = models.CharField(max_length=120, verbose_name="Име (Македонски)")
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=200, verbose_name="Резиме (Македонски)")
    description = models.TextField(verbose_name="Опис (Македонски)")
    
    # Turkish
    name_tr = models.CharField(max_length=120, blank=True, verbose_name="Ad (Türkçe)")
    summary_tr = models.CharField(max_length=200, blank=True, verbose_name="Özet (Türkçe)")
    description_tr = models.TextField(blank=True, verbose_name="Açıklama (Türkçe)")
    
    # Albanian
    name_sq = models.CharField(max_length=120, blank=True, verbose_name="Emri (Shqip)")
    summary_sq = models.CharField(max_length=200, blank=True, verbose_name="Përmbledhja (Shqip)")
    description_sq = models.TextField(blank=True, verbose_name="Përshkrimi (Shqip)")
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='a_line',
        verbose_name="Категорија"
    )
    price = models.CharField(max_length=60, blank=True, default="По договор", verbose_name="Цена (Македонски)")
    price_tr = models.CharField(max_length=60, blank=True, default="Tafsiye Edilen Fiyat", verbose_name="Fiyat (Türkçe)")
    price_sq = models.CharField(max_length=60, blank=True, default="Me Marrëveshje", verbose_name="Çmimi (Shqip)")
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
        help_text="Önerilen boyut: 600x800 piksel (dikey dikdörtgen), maksimum 400KB"
    )
    created_at = models.DateField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False, verbose_name="Истакнат на почетна", help_text="Означете за да се прикаже на почетната страница (максимум 3)")

    class Meta:
        ordering = ["-is_featured", "-created_at", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})
    
    def get_name(self, lang='mk'):
        if lang == 'tr' and self.name_tr:
            return self.name_tr
        elif lang == 'sq' and self.name_sq:
            return self.name_sq
        return self.name
    
    def get_summary(self, lang='mk'):
        if lang == 'tr' and self.summary_tr:
            return self.summary_tr
        elif lang == 'sq' and self.summary_sq:
            return self.summary_sq
        return self.summary
    
    def get_description(self, lang='mk'):
        if lang == 'tr' and self.description_tr:
            return self.description_tr
        elif lang == 'sq' and self.description_sq:
            return self.description_sq
        return self.description
    
    def get_price(self, lang='mk'):
        """Get translated price"""
        if lang == 'tr' and self.price_tr:
            return self.price_tr
        elif lang == 'sq' and self.price_sq:
            return self.price_sq
        return self.price
    
    def get_primary_image(self):
        """Get the primary image for this product"""
        primary = self.images.filter(is_primary=True).first()
        if primary:
            return primary.image.url
        first_image = self.images.first()
        if first_image:
            return first_image.image.url
        if self.image:
            return self.image.url
        return "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=900&q=80"
    
    def get_all_images(self):
        """Get all images for this product"""
        return self.images.all().order_by('-is_primary', 'order')
    
    def get_average_rating(self):
        """Get average rating from approved reviews"""
        from django.db.models import Avg
        result = self.reviews.filter(is_approved=True).aggregate(avg=Avg('rating'))
        return result['avg'] or 0
    
    def get_review_count(self):
        """Get count of approved reviews"""
        return self.reviews.filter(is_approved=True).count()


class ProductImage(models.Model):
    """Multiple images for a product (up to 3)"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(
        upload_to='products/',
        help_text="Препорачана големина: 600x800 пиксели (вертикален правоаголник)"
    )
    is_primary = models.BooleanField(default=False, verbose_name="Примарна слика", help_text="Оваа слика ќе се прикаже како главна")
    order = models.PositiveIntegerField(default=0, verbose_name="Редослед")
    alt_text = models.CharField(max_length=200, blank=True, verbose_name="Alt текст")
    
    class Meta:
        ordering = ['-is_primary', 'order']
        verbose_name = "Слика на производ"
        verbose_name_plural = "Слики на производи"
    
    def __str__(self):
        return f"{self.product.name} - Слика {self.order + 1}"
    
    def save(self, *args, **kwargs):
        # If this is set as primary, unset other primaries for this product
        if self.is_primary:
            ProductImage.objects.filter(product=self.product, is_primary=True).exclude(pk=self.pk).update(is_primary=False)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    CATEGORY_CHOICES = (
        ('bridal_designs', 'Дизајни за невести'),
        ('personal_stories', 'Лични приказни'),
        ('fashion_trends', 'Модни трендови'),
        ('care_tips', 'Совети за нега'),
        ('atelier_news', 'Вести од атељето'),
    )
    
    CATEGORY_TRANSLATIONS = {
        'bridal_designs': {'mk': 'Дизајни за невести', 'tr': 'Gelinlik Tasarımları', 'sq': 'Dizajne për nuse'},
        'personal_stories': {'mk': 'Лични приказни', 'tr': 'Kişisel Hikayeler', 'sq': 'Histori personale'},
        'fashion_trends': {'mk': 'Модни трендови', 'tr': 'Moda Trendleri', 'sq': 'Trendet e modës'},
        'care_tips': {'mk': 'Совети за нега', 'tr': 'Bakım Tavsiyeleri', 'sq': 'Këshilla për kujdes'},
        'atelier_news': {'mk': 'Вести од атељето', 'tr': 'Atelier Haberleri', 'sq': 'Lajme nga atelieja'},
    }
    
    @classmethod
    def get_category_name(cls, category_key, lang='mk'):
        """Get translated category name"""
        if category_key in cls.CATEGORY_TRANSLATIONS:
            return cls.CATEGORY_TRANSLATIONS[category_key].get(lang, cls.CATEGORY_TRANSLATIONS[category_key]['mk'])
        return category_key
    
    # Macedonian (default)
    title = models.CharField(max_length=160, verbose_name="Наслов (Македонски)")
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(verbose_name="Извадок (Македонски)")
    body = models.TextField(verbose_name="Содржина (Македонски)")
    
    # Turkish
    title_tr = models.CharField(max_length=160, blank=True, verbose_name="Başlık (Türkçe)")
    excerpt_tr = models.TextField(blank=True, verbose_name="Özet (Türkçe)")
    body_tr = models.TextField(blank=True, verbose_name="İçerik (Türkçe)")
    
    # Albanian
    title_sq = models.CharField(max_length=160, blank=True, verbose_name="Titulli (Shqip)")
    excerpt_sq = models.TextField(blank=True, verbose_name="Përmbledhja (Shqip)")
    body_sq = models.TextField(blank=True, verbose_name="Përmbajtja (Shqip)")
    
    published_at = models.DateField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='atelier_news', help_text="Blog yazısının kategorisini seçin")
    hero_image = models.ImageField(
        upload_to='blog/',
        blank=True,
        null=True,
        help_text="Önerilen boyut: 800x450 piksel (16:9 yatay dikdörtgen), maksimum 400KB"
    )
    # Old text-based tags (deprecated, kept for migration)
    tags = models.CharField(max_length=200, blank=True, verbose_name="Етикети (Македонски)", help_text="Eski alan - artık kullanılmıyor")
    tags_tr = models.CharField(max_length=200, blank=True, verbose_name="Etiketler (Türkçe)", help_text="Eski alan - artık kullanılmıyor")
    tags_sq = models.CharField(max_length=200, blank=True, verbose_name="Etiketat (Shqip)", help_text="Eski alan - artık kullanılmıyor")
    # New ManyToMany tags
    blog_tags = models.ManyToManyField(BlogTag, blank=True, related_name='blog_posts', verbose_name="Etiketler")
    likes = models.PositiveIntegerField(default=0)
    # SEO - Macedonian
    meta_title = models.CharField(max_length=70, blank=True, verbose_name="SEO Наслов (Македонски)", help_text="Max 70 карактери")
    meta_description = models.CharField(max_length=160, blank=True, verbose_name="SEO Опис (Македонски)", help_text="Max 160 карактери")
    # SEO - Turkish
    meta_title_tr = models.CharField(max_length=70, blank=True, verbose_name="SEO Başlık (Türkçe)", help_text="Max 70 karakter")
    meta_description_tr = models.CharField(max_length=160, blank=True, verbose_name="SEO Açıklama (Türkçe)", help_text="Max 160 karakter")
    # SEO - Albanian
    meta_title_sq = models.CharField(max_length=70, blank=True, verbose_name="SEO Titulli (Shqip)", help_text="Max 70 karaktere")
    meta_description_sq = models.CharField(max_length=160, blank=True, verbose_name="SEO Përshkrimi (Shqip)", help_text="Max 160 karaktere")
    
    def get_title(self, lang='mk'):
        if lang == 'tr' and self.title_tr:
            return self.title_tr
        elif lang == 'sq' and self.title_sq:
            return self.title_sq
        return self.title
    
    def get_excerpt(self, lang='mk'):
        if lang == 'tr' and self.excerpt_tr:
            return self.excerpt_tr
        elif lang == 'sq' and self.excerpt_sq:
            return self.excerpt_sq
        return self.excerpt
    
    def get_body(self, lang='mk'):
        if lang == 'tr' and self.body_tr:
            return self.body_tr
        elif lang == 'sq' and self.body_sq:
            return self.body_sq
        return self.body
    
    def get_meta_title(self, lang='mk'):
        if lang == 'tr' and self.meta_title_tr:
            return self.meta_title_tr
        elif lang == 'sq' and self.meta_title_sq:
            return self.meta_title_sq
        return self.meta_title or self.title
    
    def get_meta_description(self, lang='mk'):
        if lang == 'tr' and self.meta_description_tr:
            return self.meta_description_tr
        elif lang == 'sq' and self.meta_description_sq:
            return self.meta_description_sq
        return self.meta_description or self.excerpt[:160]

    class Meta:
        ordering = ["-published_at", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def get_tags_list(self, lang='mk'):
        """Get tags list in the specified language from ManyToMany relationship"""
        return [tag.get_name(lang) for tag in self.blog_tags.all()]


class FAQItem(models.Model):
    CATEGORY_CHOICES = (
        ('booking_trials', 'Резервации и проби'),
        ('design_customization', 'Дизајн и прилагодување'),
        ('timeline_pricing', 'Рокови и цени'),
        ('delivery_care', 'Достава и нега'),
        ('products_materials', 'Производи и материјали'),
        ('contact_info', 'Контакт и информации'),
    )
    
    CATEGORY_TRANSLATIONS = {
        'booking_trials': {'mk': 'Резервации и проби', 'tr': 'Rezervasyon ve Deneme', 'sq': 'Rezervime dhe prova'},
        'design_customization': {'mk': 'Дизајн и прилагодување', 'tr': 'Tasarım ve Özelleştirme', 'sq': 'Dizajn dhe personalizim'},
        'timeline_pricing': {'mk': 'Рокови и цени', 'tr': 'Süre ve Fiyatlandırma', 'sq': 'Afatet dhe çmimet'},
        'delivery_care': {'mk': 'Достава и нега', 'tr': 'Teslimat ve Bakım', 'sq': 'Dorëzimi dhe kujdesi'},
        'products_materials': {'mk': 'Производи и материјали', 'tr': 'Ürünler ve Malzemeler', 'sq': 'Produkte dhe materiale'},
        'contact_info': {'mk': 'Контакт и информации', 'tr': 'İletişim ve Bilgi', 'sq': 'Kontakt dhe informacion'},
    }
    
    @classmethod
    def get_category_name(cls, category_key, lang='mk'):
        """Get translated category name"""
        if category_key in cls.CATEGORY_TRANSLATIONS:
            return cls.CATEGORY_TRANSLATIONS[category_key].get(lang, cls.CATEGORY_TRANSLATIONS[category_key]['mk'])
        return category_key
    
    # Macedonian (default language)
    question_mk = models.CharField(max_length=200, verbose_name="Прашање (Македонски)")
    answer_mk = models.TextField(verbose_name="Одговор (Македонски)")
    
    # Turkish
    question_tr = models.CharField(max_length=200, blank=True, verbose_name="Soru (Türkçe)")
    answer_tr = models.TextField(blank=True, verbose_name="Cevap (Türkçe)")
    
    # Albanian
    question_sq = models.CharField(max_length=200, blank=True, verbose_name="Pyetja (Shqip)")
    answer_sq = models.TextField(blank=True, verbose_name="Përgjigja (Shqip)")
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='booking_trials', help_text="Категорија / Kategori / Kategoria")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "order"]

    def __str__(self):
        return self.question_mk

    def get_question(self, lang='mk'):
        """Get question in specified language"""
        field = f'question_{lang}'
        return getattr(self, field, self.question_mk) or self.question_mk
    
    def get_answer(self, lang='mk'):
        """Get answer in specified language"""
        field = f'answer_{lang}'
        return getattr(self, field, self.answer_mk) or self.answer_mk


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
    
    def get_name(self, lang='mk'):
        if lang == 'tr' and self.name_tr:
            return self.name_tr
        elif lang == 'sq' and self.name_sq:
            return self.name_sq
        return self.name
    
    def get_price(self, lang='mk'):
        return self.price
    
    def get_period(self, lang='mk'):
        if lang == 'tr' and self.period_tr:
            return self.period_tr
        elif lang == 'sq' and self.period_sq:
            return self.period_sq
        return self.period
    
    def get_features(self, lang='mk'):
        if lang == 'tr' and self.features_tr:
            return [f.strip() for f in self.features_tr.split("\n") if f.strip()]
        elif lang == 'sq' and self.features_sq:
            return [f.strip() for f in self.features_sq.split("\n") if f.strip()]
        return [f.strip() for f in self.features.split("\n") if f.strip()]


class AddOnService(models.Model):
    """Add-on hizmetler ve opsiyonel paketler"""
    name = models.CharField(max_length=100, verbose_name="Име (Македонски)")
    name_tr = models.CharField(max_length=100, blank=True, verbose_name="Ad (Türkçe)")
    name_sq = models.CharField(max_length=100, blank=True, verbose_name="Emri (Shqip)")
    description = models.TextField(blank=True, verbose_name="Опис (Македонски)")
    description_tr = models.TextField(blank=True, verbose_name="Açıklama (Türkçe)")
    description_sq = models.TextField(blank=True, verbose_name="Përshkrimi (Shqip)")
    price = models.CharField(max_length=50, blank=True, verbose_name="Цена (Македонски)", help_text="Пр: БЕСПЛАТНО, 500 ден, По договор")
    price_tr = models.CharField(max_length=50, blank=True, verbose_name="Fiyat (Türkçe)", help_text="Ör: ÜCRETSİZ, 500 TL, Fiyat sorunuz")
    price_sq = models.CharField(max_length=50, blank=True, verbose_name="Çmimi (Shqip)", help_text="P.sh: FALAS, 500 den, Me marrëveshje")
    icon = models.CharField(max_length=10, default="✨", help_text="Emoji ikon (ör: ✨, 🎨, 📏, 👗, ⚡, 🎁, ✂️, 🧵, ♨️, 📦, 💻)")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.icon} {self.name}"
    
    def get_name(self, lang='mk'):
        if lang == 'tr' and self.name_tr:
            return self.name_tr
        elif lang == 'sq' and self.name_sq:
            return self.name_sq
        return self.name
    
    def get_description(self, lang='mk'):
        if lang == 'tr' and self.description_tr:
            return self.description_tr
        elif lang == 'sq' and self.description_sq:
            return self.description_sq
        return self.description
    
    def get_price(self, lang='mk'):
        if lang == 'tr' and self.price_tr:
            return self.price_tr
        elif lang == 'sq' and self.price_sq:
            return self.price_sq
        return self.price


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
    site_name = models.CharField(max_length=100, default="Ankora Atelier", blank=True)
    tagline = models.CharField(max_length=200, default="Bridal & Couture Studio", blank=True)
    
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
    whatsapp_number = models.CharField(max_length=20, blank=True, default="38970666567", help_text="WhatsApp numarası (ülke kodu ile, boşluksuz: örn. 38970666567)")
    
    # Header Settings
    show_header_branding = models.BooleanField(default=True, help_text="Header'da site adı ve slogan göster")
    
    # Social Links
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    pinterest_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)
    google_business_url = models.URLField(blank=True, help_text="Google My Business profil linki")
    
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
        ('services_gallery', 'Hizmetler - Galeri Resimleri'),
        
        # CONTACTS PAGE
        ('contact_gallery', 'İletişim - Galeri Resimleri'),
        ('contact_cta_left', 'İletişim - CTA Sol Resim'),
        ('contact_cta_right', 'İletişim - CTA Sağ Resim'),
        
        # FAQ PAGE
        ('faq_accommodation', 'SSS - Konaklama Resimleri'),
        ('faq_cta_left', 'SSS - CTA Sol Resim'),
        ('faq_cta_right', 'SSS - CTA Sağ Resim'),
        
        # PORTFOLIO PAGE
        ('portfolio_hero', 'Portfolio - Hero Arka Planı (Уметнички дела)'),
        ('portfolio_showcase', 'Portfolio - Galerideki Resimler'),
        
        # RSVP PAGE
        ('rsvp_hero', 'RSVP - Hero Arka Planı'),
    ]
    
    # Image size guidelines for each section
    SECTION_SIZE_GUIDELINES = {
        'hero_home': '1920x1080px (Full HD), JPG/WebP, max 500KB - Tam ekran hero arka planı',
        'hero_home_2': '1920x1080px (Full HD), JPG/WebP, max 500KB - İkinci hero arka planı',
        'hero_home_stack_1': '400x500px (Dikey), JPG/WebP, max 200KB - Stack resim sol',
        'hero_home_stack_2': '400x500px (Dikey), JPG/WebP, max 200KB - Stack resim sağ',
        'hero_home_floral': '300x300px (Kare), PNG (şeffaf arka plan), max 150KB - Dekoratif çiçek',
        'dress_gallery_mini_1': '400x400px (Kare), JPG/WebP, max 150KB - Mini galeri resmi',
        'dress_gallery_mini_2': '420x420px (Kare), JPG/WebP, max 150KB - Mini galeri resmi',
        'dress_gallery_mini_3': '380x380px (Kare), JPG/WebP, max 150KB - Mini galeri resmi',
        'bride_gallery_1': '400x500px (Dikey), JPG/WebP, max 200KB - Gelin galerisi',
        'bride_gallery_2': '600x500px (Yatay), JPG/WebP, max 250KB - Gelin galerisi (geniş)',
        'bride_gallery_3': '400x500px (Dikey), JPG/WebP, max 200KB - Gelin galerisi',
        'bride_gallery_4': '400x500px (Dikey), JPG/WebP, max 200KB - Gelin galerisi',
        'bride_gallery_5': '600x500px (Yatay), JPG/WebP, max 250KB - Gelin galerisi (geniş)',
        'about_hero': '1920x800px (Geniş banner), JPG/WebP, max 400KB - Hakkımızda hero',
        'services_banner': '1920x600px (Banner), JPG/WebP, max 400KB - Hizmetler banner',
        'services_gallery': '400x500px (Dikey), JPG/WebP, max 200KB - Hizmetler sayfası galeri',
        'contact_gallery': '400x500px (Dikey), JPG/WebP, max 200KB - İletişim sayfası galeri',
        'contact_cta_left': '400x500px (Dikey), JPG/WebP, max 200KB - İletişim CTA sol resim',
        'contact_cta_right': '400x500px (Dikey), JPG/WebP, max 200KB - İletişim CTA sağ resim',
        'faq_accommodation': '800x600px (Yatay), JPG/WebP, max 300KB - SSS konaklama görseli',
        'faq_cta_left': '400x500px (Dikey), JPG/WebP, max 200KB - SSS CTA sol resim',
        'faq_cta_right': '400x500px (Dikey), JPG/WebP, max 200KB - SSS CTA sağ resim',
        'portfolio_hero': '1920x1080px (Full HD), JPG/WebP, max 500KB - Portfolio hero arka planı',
        'portfolio_showcase': '800x1000px (Dikey), JPG/WebP, max 350KB - Portfolio vitrin',
        'rsvp_hero': '1920x800px (Geniş banner), JPG/WebP, max 400KB - RSVP hero arka planı',
    }
    
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
    
    def get_size_guideline(self):
        """Get the recommended image size for this section"""
        return self.SECTION_SIZE_GUIDELINES.get(self.section, 'Önerilen boyut belirtilmemiş')


# Proxy models for section-based admin organization
class HomeHeroMedia(PageMedia):
    """Anasayfa Hero Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "Anasayfa Hero Görseli"
        verbose_name_plural = "🏠 Anasayfa - Hero Görselleri"


class HomeBrideGalleryMedia(PageMedia):
    """Anasayfa Gelin Galerisi Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "Gelin Galerisi Görseli"
        verbose_name_plural = "🏠 Anasayfa - Gelin Galerisi"


class HomeDressGalleryMedia(PageMedia):
    """Anasayfa Dress Gallery Mini Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "Dress Gallery Görseli"
        verbose_name_plural = "🏠 Anasayfa - Dress Gallery"


class AboutPageMedia(PageMedia):
    """Hakkımızda Sayfası Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "Hakkımızda Görseli"
        verbose_name_plural = "📄 Hakkımızda - Görseller"


class ServicesPageMedia(PageMedia):
    """Hizmetler Sayfası Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "Hizmetler Görseli"
        verbose_name_plural = "🛠️ Hizmetler - Görseller"


class ContactsPageMedia(PageMedia):
    """İletişim Sayfası Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "İletişim Görseli"
        verbose_name_plural = "📞 İletişim - Görseller"


class FAQPageMedia(PageMedia):
    """SSS Sayfası Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "SSS Görseli"
        verbose_name_plural = "❓ SSS - Görseller"


class RSVPPageMedia(PageMedia):
    """RSVP Sayfası Görselleri"""
    class Meta:
        proxy = True
        verbose_name = "RSVP Görseli"
        verbose_name_plural = "📋 RSVP - Görseller"


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
        return f"https://www.youtube.com/embed/{self.youtube_id}"


class ProductReview(models.Model):
    """Product reviews with star ratings (1-5 with half stars)"""
    RATING_CHOICES = [
        (0.5, '0.5 ⭐'),
        (1.0, '1 ⭐'),
        (1.5, '1.5 ⭐'),
        (2.0, '2 ⭐'),
        (2.5, '2.5 ⭐'),
        (3.0, '3 ⭐'),
        (3.5, '3.5 ⭐'),
        (4.0, '4 ⭐'),
        (4.5, '4.5 ⭐'),
        (5.0, '5 ⭐'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(max_digits=2, decimal_places=1, choices=RATING_CHOICES, verbose_name="Değerlendirme")
    reviewer_name = models.CharField(max_length=100, verbose_name="İsim")
    reviewer_email = models.EmailField(verbose_name="E-posta")
    comment = models.TextField(blank=True, verbose_name="Yorum")
    is_approved = models.BooleanField(default=False, verbose_name="Onaylandı", help_text="Onaylanmadan sayfada görünmez")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Ürün Değerlendirmesi"
        verbose_name_plural = "Ürün Değerlendirmeleri"
    
    def __str__(self):
        return f"{self.product.name} - {self.rating}⭐ by {self.reviewer_name}"

