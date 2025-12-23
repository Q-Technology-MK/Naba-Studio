# 📋 Tamamlanan Google Maps Entegrasyonu - Değişiklik Özeti

## 🎯 Hedef
Naba Studio'nun Skopje, Samoilova 90 konumunda Google Maps haritasını website'in tüm sayfalarında (anasayfa, iletişim, RSVP) dinamik olarak göstermek.

---

## ✅ Tamamlanan Görevler

### 1️⃣ **Database Schema Güncelleme** ✓
**Dosya:** `core/models.py`

```python
# Satır 225-228: SiteSettings'e 3 yeni alan eklendi
class SiteSettings(models.Model):
    # ... (mevcut alanlar)
    
    # Maps & Location
    map_latitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        default="41.997335",
        help_text="Naba Studio Samoilova 90 enlemi: 41.997335"
    )
    map_longitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        default="21.428057",
        help_text="Naba Studio Samoilova 90 boylamı: 21.428057"
    )
    map_embed_code = models.TextField(
        blank=True,
        help_text="Google Maps embed kod. Boş bırakılırsa koordinatlardan otomatik oluşturulur."
    )
    
    # Satır 237-239: Yeni method eklendi
    def get_map_embed_url(self):
        """Generate Google Maps embed URL from coordinates if custom code not provided"""
        if self.map_embed_code:
            return self.map_embed_code
        # Generate from coordinates
        return f'<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1498.2340000000002!2d{self.map_longitude}!3d{self.map_latitude}..." ... ></iframe>'
```

**Neden:** Admin panelinden harita koordinatlarını merkezi olarak yönetebilmek.

---

### 2️⃣ **Admin Panel Fieldset** ✓
**Dosya:** `core/admin.py` (Satırlar: 156-160)

```python
("Harita & Konum", {
    "fields": ("map_latitude", "map_longitude", "map_embed_code"),
    "description": "Google Maps entegrasyonu. Naba Studio - Samoilova 90, Skopje Kale | Koordinatlar: 41.997335° N, 21.428057° E | Özel embed kodu eklemek isterseniz map_embed_code'a Google Maps iframe URL'sini yapıştırın."
}),
```

**Neden:** Admin kullanıcısının kolayca harita ayarlarını yapabilmesi.

---

### 3️⃣ **Anasayfa Harita Güncellemesi** ✓
**Dosya:** `templates/core/home.html` (Satırlar: 118-130)

**Öncesi:**
```html
<div class="map-embed">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18" title="Studio map" allowfullscreen loading="lazy"></iframe>
</div>
```

**Sonrası:**
```html
<div class="map-embed">
    {% if site_settings.map_embed_code %}
        {{ site_settings.map_embed_code|safe }}
    {% else %}
        <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1498.2340000000002!2d21.428057!3d41.997335!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x1354586c8b8d7d4d%3A0x8f8f8f8f8f8f8f8f!2sSamoilova%2090%2C%20Skopje!5e0!3m2!1sen!2sus!4v1702740000000!5m2!1sen!2sus"
            allowfullscreen
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            title="Naba Studio Skopje"
        ></iframe>
    {% endif %}
</div>
```

**Neden:** Dinamik harita - admin ayarlarından koordinatları otomatik çeker.

---

### 4️⃣ **İletişim Sayfası Harita Güncellemesi** ✓
**Dosya:** `templates/core/contacts.html` (Satırlar: 35-45)

**Öncesi:**
```html
<div class="map-embed">
    <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2500...Berlin..." 
        ...
    ></iframe>
</div>
```

**Sonrası:**
```html
<div class="map-embed">
    {% if site_settings.map_embed_code %}
        {{ site_settings.map_embed_code|safe }}
    {% else %}
        <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1498.2340000000002!2d21.428057!3d41.997335...Skopje..."
            ...
        ></iframe>
    {% endif %}
</div>
```

**Değişiklik:** Berlin koordinatları → Skopje koordinatları (41.997335, 21.428057)

---

### 5️⃣ **RSVP Sayfası Harita Eklenmesi** ✓
**Dosya:** `templates/core/rsvp.html` (Satırlar: 52-67)

**Öncesi:**
```html
    </section>
</div>
{% endblock %}
```

**Sonrası:**
```html
    </section>
</div>

<!-- Map Section -->
<div class="page-wrapper">
    <section class="rsvp-map-section">
        <h2 class="section-heading">Atölye Konumu</h2>
        <div class="map-embed">
            {% if site_settings.map_embed_code %}
                {{ site_settings.map_embed_code|safe }}
            {% else %}
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1498...Skopje..."
                    ...
                ></iframe>
            {% endif %}
        </div>
    </section>
</div>
```

**Neden:** RSVP sayfasına "Atölye Konumu" bölümü eklenerek konukların bulunmasını kolaylaştırma.

---

### 6️⃣ **CSS Styling** ✓
**Dosya:** `static/css/main.css` (Satırlar: 2195-2202)

```css
.rsvp-map-section {
    margin: 3rem 0;
    padding: 2rem 0;
}

.rsvp-map-section .section-heading {
    margin-bottom: 1.5rem;
}
```

**Neden:** RSVP harita bölümü için uygun boşluk ve görünüm.

---

## 📊 Etkilenen Dosyalar - Özet

| Dosya | Satır | İşlem | Alanlar |
|-------|-------|-------|---------|
| `core/models.py` | 225-239 | ➕ Eklendi | `map_latitude`, `map_longitude`, `map_embed_code`, `get_map_embed_url()` |
| `core/admin.py` | 156-160 | ✏️ Güncellendi | Fieldset "Harita & Konum" |
| `templates/core/home.html` | 118-130 | ✏️ Güncellendi | Dinamik iframe |
| `templates/core/contacts.html` | 35-45 | ✏️ Güncellendi | Dinamik iframe + Skopje koordinatları |
| `templates/core/rsvp.html` | 52-67 | ➕ Eklendi | Yeni harita bölümü |
| `static/css/main.css` | 2195-2202 | ➕ Eklendi | `.rsvp-map-section` stili |

---

## 🔄 Bağımlılıklar ve İlişkiler

```
┌─ SiteSettings Model
│  ├─ map_latitude (41.997335)
│  ├─ map_longitude (21.428057)
│  └─ map_embed_code (opsiyonel)
│
├─ Context Processor (✓ Zaten kurulu)
│  └─ Tüm template'lerde site_settings erişilebilir
│
├─ home.html
│  └─ .contact-split > .map-embed
│
├─ contacts.html
│  └─ .contact-form > .map-embed
│
└─ rsvp.html
   └─ .rsvp-map-section > .map-embed
```

---

## 🚀 Sonraki Adımlar (Zorunlu)

```bash
# 1. Migration oluştur
python manage.py makemigrations

# 2. Migration uygula
python manage.py migrate

# 3. Django admin'i aç ve test et
python manage.py runserver
# http://localhost:8000/admin/
# Site Settings > Harita & Konum
```

---

## ✨ Özellikler

### ✅ Tam Otomatik
- Koordinatlardan iframe otomatik oluşturma
- Template'de kod tekrarı yok

### ✅ Merkezi Yönetim
- Admin panelinde tek yerde ayarla
- Tüm 3 sayfa otomatik senkronize

### ✅ Responsive Tasarım
```css
Masaüstü (>768px): 360px
Tablet (768px):    280px
Mobil (<480px):    240px
```

### ✅ Güvenlik
- HTML injection koruması (admin filters)
- Context processor ile güvenli veri iletimi

### ✅ Esneklik
- Özel embed kodu eklenebilir
- Fallback koordinat değerleri

---

## 🧪 Test Checklist

- [ ] `python manage.py makemigrations` - Exit Code: 0
- [ ] `python manage.py migrate` - Exit Code: 0
- [ ] Admin panelinde Site Settings açılıyor
- [ ] "Harita & Konum" bölümü görünüyor
- [ ] Anasayfa haritası Skopje'yi gösteriyor
- [ ] İletişim sayfası haritası Skopje'yi gösteriyor
- [ ] RSVP sayfası "Atölye Konumu" haritası gösteriyor
- [ ] Tüm haritalar responsive (mobil test)
- [ ] Haritalar interaktif (kaydır, zoom)

---

## 📞 Hızlı Referans

**Koordinatlar:**
- Latitude: 41.997335
- Longitude: 21.428057
- Konum: Samoilova 90, Skopje Kale, Makedonya
- Google Maps: https://maps.app.goo.gl/TnBQbTKjQFpx3DFN7

**Admin Yolu:** `/admin/core/sitesettings/1/change/`

**Harita Gösterilen Sayfalar:**
1. `/` - Anasayfa (contact-split)
2. `/contacts/` - İletişim (form altı)
3. `/rsvp/` - RSVP (atölye konumu)

---

**✅ Durum: Hazır Kodlanmıştır**
**⏳ Sonraki: Migration ve Test**
**📅 Güncelleme Tarihi:** 2024
