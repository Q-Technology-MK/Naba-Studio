# Google Maps Entegrasyonu

## Skopje, Samoilova 90 Harita Ayarlaması

### 📍 Varsayılan Konum
- **Adres:** Samoilova 90, Skopje Kale, Makedonya
- **Enlem (Latitude):** 41.997335
- **Boylam (Longitude):** 21.428057
- **Google Maps Link:** https://maps.app.goo.gl/TnBQbTKjQFpx3DFN7

### 🎯 Harita Ayarlaması Yöntemleri

#### Yöntem 1: Otomatik (Koordinatlardan)
Admin panelinde (`Site Settings > Harita & Konum`):
1. `map_latitude` = 41.997335
2. `map_longitude` = 21.428057
3. `map_embed_code` = Boş bırak

Sistem otomatik olarak bu koordinatlardan Google Maps haritası oluşturacak.

#### Yöntem 2: Özel Embed Kodu (İleri Düzey)

Kendi özel embed kodunu kullanmak için:

1. **Google Maps'te aç:** https://maps.google.com
2. **Samoilova 90 konumunu ara** (veya başka bir konum)
3. **"Share" butonuna tıkla** → "Embed a map" seçeneğini seç
4. **Embed kodu kopyala:**
   ```html
   <iframe src="https://www.google.com/maps/embed?pb=..." width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
   ```
5. **Admin panelinde `map_embed_code` alanına yapıştır**

### 📱 Harita Gösterilen Sayfalar

1. **Anasayfa** (`home.html`) - Contact Split Bölümü
2. **İletişim** (`contacts.html`) - İletişim Formu Altında
3. **RSVP** (`rsvp.html`) - Atölye Konumu Bölümü

Tüm haritalar dinamik olarak `site_settings` verilerinden çekilir.

### ⚙️ Teknik Detaylar

**Model Field'ları:**
- `map_latitude` (DecimalField): Harita enlem koordinatı
- `map_longitude` (DecimalField): Harita boylam koordinatı
- `map_embed_code` (TextField): Özel Google Maps iframe kodu

**Template Mantığı:**
```django
{% if site_settings.map_embed_code %}
    {{ site_settings.map_embed_code|safe }}
{% else %}
    <!-- Koordinatlardan otomatik iframe oluşturulur -->
{% endif %}
```

**Python Method:**
```python
SiteSettings.get_map_embed_url()  # Harita embed kodu döndürür
```

### 🔗 İlgili Dosyalar
- Model: [core/models.py](core/models.py#L225-L228)
- Admin: [core/admin.py](core/admin.py#L156-L160)
- Templates:
  - [templates/core/home.html](templates/core/home.html#L118)
  - [templates/core/contacts.html](templates/core/contacts.html#L35)
  - [templates/core/rsvp.html](templates/core/rsvp.html#L52)
- CSS: [static/css/main.css](static/css/main.css#L2170-L2200)

### ✅ Kontrol Listesi

- [ ] Admin panel'de Site Settings açıldı
- [ ] "Harita & Konum" bölümü görüntülendi
- [ ] Koordinatlar (41.997335, 21.428057) doğrulandı
- [ ] Tüm sayfalar haritayı doğru gösteriyor (home, contacts, rsvp)
- [ ] Harita interaktif ve kaydırılabiliyor
- [ ] Mobil cihazlarda düzgün gösteriliyor

### 🎨 Harita Stil Ayarlaması (CSS)

`.map-embed` sınıfı ile harita stillemesi yapılabilir:
- **Masaüstü:** 360px yükseklik
- **Tablet:** 280px yükseklik
- **Mobil:** 240px yükseklik

CSS düzenlemeleri: [static/css/main.css#L2170](static/css/main.css#L2170)
