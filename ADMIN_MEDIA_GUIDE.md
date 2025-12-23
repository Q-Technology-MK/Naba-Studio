# 🎯 ADMIN PANEL - GÖRSELLER (PageMedia) KULLANIM KILAVUZU

## 📍 Erişim
**Django Admin Panel** → **Sayfa Görselleri (PageMedia)** → Görselleri Yönet

---

## 📸 GÖRSELLER NEDIR?

PageMedia sistemi sayfalardaki **tüm görselleri merkezi bir yerden yönetmenizi** sağlar. Resim eklemek, değiştirmek ya da aktifleştirmek istediğinizde admin panelden yapabilirsiniz. Kod değişikliğine gerek yok.

---

## ➕ YENİ GÖRSEL EKLEME

### Adım 1: Admin Panele Gir
```
http://127.0.0.1:8000/admin/ → "Sayfa Görselleri" → "Yeni Görsel Ekle"
```

### Adım 2: Form Doldur

#### 🏷️ **Bölüm & Sıralama** Bölümü
- **Bölüm:** Açılır menüden görselin hangi sayfada ve bölümde kullanılacağını seçin
  - Örn: "Anasayfa - Hero 1 Arka Planı"
- **Sıra:** Aynı bölümde birden çok görsel varsa sırasını belirtin (0, 1, 2, vb.)
- **Aktif:** ✅ işaretlenirse görsel sayfada gösterilir

#### 🖼️ **Görsel Yükleme** Bölümü
- **Resmi Seç:** Bilgisayarınızdan görsel dosyasını seçin
- ⚠️ **ÖNEMLİ:** Bölümünüzün gerektirdiği ölçülerde yükleyiniz!

#### 📝 **SEO & Erişilebilirlik** Bölümü
- **Alt Text:** Görsel yüklenemediğinde gösterilecek metin (ör: "Naba Studio Hero Görseli")
- **Başlık:** SEO için görsel başlığı (ör: "Couture Gelinlik Dizaynı")

#### 📏 **Ölçüler & Format Bilgisi** Bölümü
- Örnek yazımlar:
  ```
  1920x1080px, JPG, max 800KB
  600x400px, PNG, max 300KB
  ```

### Adım 3: Kaydet
"Kaydet" düğmesine tıkla → Görsel sayfada otomatik gösterilir ✅

---

## ✏️ GÖRSEL DEĞIŞTIRME

1. Admin panelden ilgili görseli bul
2. Tıkla, form aç
3. **Resmi Seç** bölümünde yeni resmi yükle
4. Kaydet

> 💡 Eski resim otomatik silinir, yeni resim kontrol edilir

---

## 🚫 GÖRSEL PASIF YAPMA (Silmeden Gizleme)

1. Görseli aç
2. **Aktif** checkbox'ını kaldır ☐
3. Kaydet

> Görsel silinmez, sadece sayfada gösterilmez. Daha sonra tekrar aktifleştirebilirsin.

---

## 🗑️ GÖRSEL SİLME

1. Görseli aç
2. Sayfanın altında "Sil" butonuna tıkla
3. Onaylı

> ⚠️ Silinen görseller geri alınamaz!

---

## 📋 BÖLÜMLER VE ÖLÇÜLER

### 🏠 ANASAYFA (Home)
| Bölüm | Ölçüler | Format |
|-------|---------|--------|
| Hero 1 Arka Planı | 1920x1080 | JPG/WebP |
| Hero 2 Arka Planı | 1920x1080 | JPG/WebP |
| Hero 2 Stack Resim 1 | 800x1000 | JPG/PNG |
| Dress Gallery Mini (3 adet) | 400-420x300 | JPG |
| Gelin Galerisi (5 adet) | 400/600x500 | JPG |

*Detaylı tablo için → [IMAGE_SPECIFICATIONS.md](IMAGE_SPECIFICATIONS.md)*

---

## 🎨 GÖRSEL YÜKLEMEYİ İPUÇLARI

### ✅ DOĞRU YAPMA
- ✓ Belirtilen ölçülerde yükle
- ✓ JPG'i max 500KB'de tut
- ✓ Alt text yazı (SEO)
- ✓ Kaliteli, net görseller

### ❌ YANLIŞ YAPMA
- ✗ Çok büyük dosya (>1MB)
- ✗ Hatalı ölçüler
- ✗ Düşük kalite resim
- ✗ Yanlış format seçme

---

## 🔧 DOSYA BOYUTUNU KÜÇÜLTME

Eğer resim çok ağırsa:

1. **Online:** TinyPNG.com
   - Resimi sürükle-bırak
   - Otomatik sıkıştırır
   - İndir

2. **Photoshop/Canva:**
   - Resmi aç
   - "Export for Web" seçeneğini kullan
   - Quality: 70-80% ayarla

3. **Windows:**
   - Resim sağ tık → "Boyutu Değiştir"
   - Hedef boyutlara göre ayarla

---

## ❓ SORULAR

**S: Görsel yükleyemiyorum, hata veriyor**
A: 
- Dosya boyutunu kontrol et (max 5MB)
- Dosya formatını kontrol et (.jpg, .png)
- Tarayıcı cache'i temizle (Ctrl+Shift+Delete)

**S: Yüklediğim görsel yanlış yerde çıkıyor**
A: 
- Admin panelinden bölümü kontrol et
- Doğru bölümün seçildiğini onaylaya

**S: Resmi çok kaliteli yükledim, sayfa yavaş açılıyor**
A:
- Dosya boyutunu 500KB altında tutun
- TinyPNG ile sıkıştırın
- WebP formatına dönüştürün (daha hızlı)

**S: Eski resmi geri alabilirim?**
A:
- Eğer "Aktif"i kapatırsanız evet (Pasif yapın)
- Eğer silerseniz hayır (veritabanından silinir)

---

## 🚀 HIZLI REFERANS

```
Admin → Sayfa Görselleri → Yeni Ekle → Form Doldur → Kaydet ✅
```

---

**Sorularınız için:** admin@nabastudio.mk

*Son Güncelleme: 23 Aralık 2025*
