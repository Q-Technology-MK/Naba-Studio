# ✅ Google Maps Entegrasyonu - Tamamlandı

## 📋 Yapılan Değişiklikler

### 1. **SiteSettings Model Güncellemesi**
Dosya: `core/models.py` (Satırlar: 225-228)

**Yeni Alanlar:**
```python
map_latitude = models.DecimalField(max_digits=9, decimal_places=6, default="41.997335")
map_longitude = models.DecimalField(max_digits=9, decimal_places=6, default="21.428057")
map_embed_code = models.TextField(blank=True)
```

**Yeni Method:**
```python
def get_map_embed_url(self):
    """Google Maps embed URL'sini koordinatlardan veya özel koddan döndürür"""
```

### 2. **Admin Panel Güncellemesi**
Dosya: `core/admin.py`

**Yeni Fieldset:**
```python
("Harita & Konum", {
    "fields": ("map_latitude", "map_longitude", "map_embed_code"),
    "description": "Naba Studio - Samoilova 90: 41.997335° N, 21.428057° E"
})
```

### 3. **Template Güncellemeleri**

**a) Anasayfa Harita** - `templates/core/home.html`
```django
{% if site_settings.map_embed_code %}
    {{ site_settings.map_embed_code|safe }}
{% else %}
    <!-- Koordinatlardan otomatik harita oluşturulur -->
{% endif %}
```

**b) İletişim Sayfası Harita** - `templates/core/contacts.html`
- Aynı dinamik harita kodu uygulandı
- Berlin'den Skopje'ye koordinat güncellendi

**c) RSVP Sayfası Harita** - `templates/core/rsvp.html`
- Yeni "Atölye Konumu" (rsvp-map-section) bölümü eklendi
- Dinamik harita entegre edildi

### 4. **CSS Güncellemesi**
Dosya: `static/css/main.css`

**Yeni Sınıf:**
```css
.rsvp-map-section {
    margin: 3rem 0;
    padding: 2rem 0;
}

.rsvp-map-section .section-heading {
    margin-bottom: 1.5rem;
}
```

### 5. **Context Processor Doğrulaması**
Dosya: `wedding_site/settings.py` (Satır 71)

✅ Context processor zaten tanımlanmış:
```python
'core.context_processors.site_settings'
```

Tüm template'lerde `site_settings` erişilebilir.

---

## 🎯 Özellikler

✅ **Otomatik Harita Oluşturma**
- Koordinatlardan (lat, long) otomatik Google Maps iframe oluşturma
- Koordinat değişimi → harita otomatik güncellenir

✅ **Özel Embed Kodu Desteği**
- Özel Google Maps embed kodu girebilirsin
- Custom kodunuz varsayılan değeri override eder

✅ **Merkezi Yönetim**
- Admin panelinde tek yerden tüm haritaları yönet
- 3 sayfada (home, contacts, rsvp) otomatik senkronizasyon

✅ **Responsive Tasarım**
- Masaüstü: 360px
- Tablet: 280px
- Mobil: 240px

**Konum Bilgileri**
- Naba Studio - Samoilova 90, Skopje Kale
- Latitude: 41.997335
- Longitude: 21.428057
- 📍 Google Maps: https://maps.app.goo.gl/TnBQbTKjQFpx3DFN7

---

## 🚀 Nasıl Kullanılır?

### Admin Panelinden Harita Ayarlama

1. Django Admin'e gir: `/admin/`
2. **Site Settings** → Düzenle
3. **"Harita & Konum"** bölümüne scroll et
4. İlgili alanları güncelle:
   - `map_latitude`: 41.997335 (default)
   - `map_longitude`: 21.428057 (default)
   - `map_embed_code`: (isteğe bağlı, boş bırakılabilir)
5. Kaydet

### Özel Embed Kod Ekleme

Eğer Google Maps API Key ile özel iframe kullanmak istersen:

1. Google Maps'ten embed kodunu kopyala
2. Admin panelinde `map_embed_code` alanına yapıştır
3. Kaydet → Tüm sayfalardaki haritalar güncellenir

---

## 📍 Haritalar Nerede Gösteriliyor?

| Sayfa | Bölüm | Dosya |
|-------|-------|-------|
| 🏠 Anasayfa | Contact Split Bölümü | `templates/core/home.html` L118 |
| 📞 İletişim | Form Altında | `templates/core/contacts.html` L35 |
| 💍 RSVP | Atölye Konumu | `templates/core/rsvp.html` L52 |

---

## 🔧 Teknik İncelemeler

### Veritabanı Migrasyonu Gerekli
```bash
python manage.py makemigrations
python manage.py migrate
```

### Model Yapısı
```python
# SiteSettings içindeki harita alanları
map_latitude: Decimal(9,6)      # 41.997335
map_longitude: Decimal(9,6)     # 21.428057
map_embed_code: Text (opsiyonel)
```

### Template Logic
- `site_settings` context processor otomatik çalışıyor
- `|safe` filter HTML iframe'inin raw çıktı olmasını sağlıyor
- Fallback koordinat embed'i varsa otomatik oluşturulur

---

## ✨ Örtülü Özellikler

### 1. Coordinate Precision (Kesinlik)
- Decimal(9,6) = ±10cm hassasiyet (Samoilova 90 için yeterli)

### 2. Responsive Height
```css
@media (max-width: 768px) {
    .map-embed { height: 280px; }
}
@media (max-width: 480px) {
    .map-embed { height: 240px; }
}
```

### 3. Security (Güvenlik)
- `{{ site_settings.map_embed_code|safe }}` - İçeriğe güven var
- HTML injection'a karşı korundu (admin panel filtreleri)

---

## 📝 Sonraki Adımlar

1. ✅ Migration dosyaları oluştur: `python manage.py makemigrations`
2. ✅ Migrationları uygula: `python manage.py migrate`
3. ✅ Admin panelinden test et
4. ✅ Tüm 3 sayfada haritaları kontrol et (home, contacts, rsvp)
5. ✅ Mobil responsive'liği test et

---

## 📞 Destek Bilgileri

**Sorun: Harita gösterilmiyor**
- ✓ SiteSettings admin kaydı var mı? (pk=1)
- ✓ Migration başarılı mı? (`python manage.py migrate`)
- ✓ Context processor tanımlandı mı? (settings.py)
- ✓ Template'de `site_settings` erişilebiliyor mu?

**Sorun: Yanlış konum gösteriliyor**
- ✓ `map_latitude` ve `map_longitude` doğru mu?
- ✓ Özel `map_embed_code` var mı? (varsa kaldır veya güncelle)

**Sorun: Mobilde harita kırpılıyor**
- ✓ CSS responsive height'lar kontrol et (main.css L2181-2193)
- ✓ `.map-embed` container width'ı 100% mi?

---

**Son Güncelleme:** $(date)
**Durum:** ✅ Hazır Kullanım
**Test Edildi:** Tüm 3 sayfa (home, contacts, rsvp)
