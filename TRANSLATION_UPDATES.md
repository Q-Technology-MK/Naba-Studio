# Tekrar Eden Metinler - Güncelleme Bilgisi

## Özet
Tekrar eden "Najprestižoto couture атеље..." metni ve ilgili seçenekler 3 dilde güncellendi.

## Eklenen Yeni Metinler

### 1. **home_hero_subtitle** (Mevcut - Korunmuş)
**Konuma göre göründüğü yerler:**
- Anasayfa Hero bölümü
- Services sayfası (4 yerde)
- About sayfası (8 yerde)
- Blog sayfası (2 yerde)
- Contacts sayfası (1 yerde)
**Toplam: 16 yerde kullanılıyor**

**Metinler:**
- **Makedonca (mk):** "Најпрестижното couture атеље за венчаници во Северна Македонија. Секоја венчаница има своја приказна. Дали си подготвена да ја напишеш твојата?"
- **Türkçe (tr):** "Kuzey Makedonya'nın en prestijli couture gelinlik tasarım atölyesi. Her gelinliğin bir hikâyesi vardır. Seninkini yazmaya hazır mısın?"
- **Arnavutça (sq):** "Atelieja më prestigjioze e fustaneve të nusërisë couture në Maqedoninë e Veriut. Çdo fustan nusërie ka një histori. A jeni gati të shkruani tuajën?"

---

### 2. **studio_prestige** (YENİ - Alternatif Metin)
**Kullanım Alanı:** Studio hakkında ek açıklama
**Metinler:**
- **Makedonca (mk):** "Нашиот атеље е позната во целиот регион за совршенство и внимание на детали."
- **Türkçe (tr):** "Atölye, bölge genelinde mükemmellik ve detaylara dikkat etmesiyle tanınmaktadır."
- **Arnavutça (sq):** "Atelieja njohet në të gjithë rajonin për përsosmëri dhe vëmendje ndaj detajeve."

---

### 3. **experience_message** (YENİ)
**Kullanım Alanı:** Deneyim ve tarih hakkında
**Metinler:**
- **Makedonca (mk):** "Со деценија искуство, создаваме венчаници кои го означуваат најспецијалниот ден во вашиот живот."
- **Türkçe (tr):** "Onlarca yıllık deneyimle, hayatınızın en özel gününü işaretleyen gelinlikler yaratıyoruz."
- **Arnavutça (sq):** "Me dhjetëra vjet përvojë, ne krijojmë fustan nusërie që shënjestrojnë ditën më të veçantë të jetës tuaj."

---

### 4. **quality_commitment** (YENİ)
**Kullanım Alanı:** Kalite taahhütü
**Metinler:**
- **Makedonca (mk):** "Секоја венчаница е создана со височок квалитет и внимание на деталите."
- **Türkçe (tr):** "Her gelinlik yüksek kalite ve detaylara dikkat ile yapılır."
- **Arnavutça (sq):** "Çdo fustan nusërie është krijuar me cilësi të lartë dhe vëmendje ndaj detajeve."

---

### 5. **custom_design_msg** (YENİ)
**Kullanım Alanı:** Kişiselleştirme ve tasarım
**Metinler:**
- **Makedonca (mk):** "Персонализирани дизајни кои го одразуваат вашиот уникален стил и личност."
- **Türkçe (tr):** "Benzersiz tarzınızı ve kişiliğinizi yansıtan kişiselleştirilmiş tasarımlar."
- **Arnavutça (sq):** "Dizajne të personalizuara që pasqyrojnë stilin tuaj unik dhe personalitetin."

---

## Dil Ayarı Nasıl Çalışıyor?

Sayfa dili değiştiğinde metinler otomatik olarak doğru dile göre görünür:
- `/mk/` URL'de → Makedonca metinler
- `/tr/` URL'de → Türkçe metinler
- `/sq/` URL'de → Arnavutça metinler

## Yeni Metinleri Templatelerde Kullanma

Şablonlarda şu şekilde kullanabilirsiniz:
```html
{% t 'studio_prestige' %}
{% t 'experience_message' %}
{% t 'quality_commitment' %}
{% t 'custom_design_msg' %}
```

## Örnek Kullanımlar

**About sayfasında:**
```html
<p>{% t 'studio_prestige' %}</p>
<p>{% t 'experience_message' %}</p>
<p>{% t 'quality_commitment' %}</p>
```

**Services sayfasında:**
```html
<section>
    <h2>{% t 'home_hero_subtitle' %}</h2>
    <p>{% t 'custom_design_msg' %}</p>
</section>
```

---

## Dosya Konumları

- **Metinlerin tanımlı olduğu dosya:** `core/templatetags/multilang.py`
- **Management command:** `core/management/commands/update_translations.py` (İleride kullanmak için)

## Nasıl Çalıştırılır?

Eğer future'da otomatik güncelleme yapmak istersen:
```bash
python manage.py update_translations
```

---

**Son Güncelleme:** 27 Ocak 2026
**Durum:** ✅ Tamamlandı
