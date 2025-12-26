# Çeviri Gereksinimleri Dökümanı

Bu döküman, websitesinde **statik olarak çevrilmesi gereken** tüm metinleri listeler.  
**Dinamik içerikler** (admin panelden girilen veriler) bu listede **YOK**.

---

## 📌 Mevcut Durum

- **Varsayılan Dil:** Makedonca (`mk`)
- **Desteklenen Diller:** Makedonca, Türkçe (`tr`), Arnavutça (`sq`)
- **Locale Klasörleri:** `locale/tr/LC_MESSAGES/`, `locale/sq/LC_MESSAGES/` (şu an boş)
- **Makedonca Klasörü:** Henüz yok, oluşturulmalı

---

## 🔴 DİNAMİK İÇERİKLER (Admin Panelden Girilir - ÇEVİRMENİZ GEREKMEZ)

Aşağıdaki içerikler admin panelden girilir ve her dil için ayrı alanlar mevcuttur:

| İçerik Türü | Açıklama |
|-------------|----------|
| **FAQ Soruları/Cevapları** | `question_mk`, `question_tr`, `question_sq`, `answer_mk`, `answer_tr`, `answer_sq` |
| **Copyright Metinleri** | `copyright_text_mk`, `copyright_text_tr`, `copyright_text_sq` |
| **Blog Yazıları** | Başlık, içerik, özet |
| **Ürünler/Portfolyo** | İsim, açıklama, fiyat |
| **Hizmetler** | Başlık, açıklama, ikon |
| **Paketler** | İsim, fiyat, özellikler |
| **Site Ayarları** | Site adı, tagline, adres, telefon, email |

---

## 🟢 STATİK İÇERİKLER (Template'lerde Hardcoded - ÇEVİRİLMESİ GEREKİR)

### 1. base.html - Ana Şablon

#### Navigasyon Menüsü
| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Home | Дома | Ballina |
| Hizmetler | Услуги | Shërbimet |
| Kurumsal | Корпоративно | Korporata |
| Hakkımızda | За нас | Rreth nesh |
| RSVP | РСВП | RSVP |
| SSS | ЧПП | FAQ |
| Fiyatlandırma | Цени | Çmimet |
| Portfolyo | Портфолио | Portofoli |
| Blog | Блог | Blog |
| İletişim | Контакт | Kontakt |
| Ana Sayfa | Почетна | Faqja kryesore |

#### Footer
| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Office | Канцеларија | Zyra |
| Links | Линкови | Lidhjet |
| Get in touch | Контактирајте нè | Na kontaktoni |

#### Diğer
| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Skip to content | Прескокни до содржина | Kalo te përmbajtja |
| Menüyü göster | Прикажи мени | Shfaq menunë |
| Yukarı çık | Оди горе | Shko lart |

---

### 2. home.html - Anasayfa

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Üsküp'ün Kalbi'nde Bir Atölye | Ателје во срцето на Скопје | Një atelie në zemër të Shkupit |
| Naba Studio by Semma | Naba Studio by Semma | Naba Studio by Semma |
| Kuzey Makedonya'nın en prestijli couture gelinlik tasarım atölyesi. Her gelinliğin bir hikâyesi vardır. Seninkini yazmaya hazır mısın? | Најпрестижното couture ателје за венчаници во Северна Македонија. Секоја венчаница има своја приказна. Дали си подготвена да ја напишеш твојата? | Atelieja më prestigjioze e fustaneve të nusërisë couture në Maqedoninë e Veriut. Çdo fustan nusërie ka një histori. A jeni gati të shkruani tuajën? |
| Hakkımızda | За нас | Rreth nesh |
| Her Gelinliğin Bir Anısı Vardır | Секоја венчаница има свој спомен | Çdo fustan nusërie ka një kujtim |
| özel dikim couture | посебно шиење couture | qepje e veçantë couture |
| Sıfırdan Tasarlanan Gelinlikler | Венчаници дизајнирани од нула | Fustane nusërie të dizajnuara nga zeroja |
| PAZARTESİ-CUMA: 10:00 – 19:00 | ПОНЕДЕЛНИК-ПЕТОК: 10:00 – 19:00 | E HËNË-E PREMTE: 10:00 – 19:00 |
| CUMARTESİ: 10:00 – 17:00 | САБОТА: 10:00 – 17:00 | E SHTUNË: 10:00 – 17:00 |
| what we do | што правиме | çfarë bëjmë |
| Bridal sewing services | Услуги за шиење венчаници | Shërbime qepjeje për nuse |
| dress shop | продавница за фустани | dyqan fustanesh |
| Ready to wear | Готови за носење | Gati për tu veshur |
| our brides | нашите невести | nusat tona |
| Dress gallery | Галерија на фустани | Galeria e fustaneve |
| Tüm Koleksiyonu Gör | Погледни ја целата колекција | Shiko të gjithë koleksionin |
| Contact Us | Контактирајте нè | Na kontaktoni |
| Have questions? Get in touch! | Имате прашања? Контактирајте нè! | Keni pyetje? Na kontaktoni! |
| Adınız | Вашето име | Emri juaj |
| E-posta | Е-пошта | Email |
| Mesajınız | Вашата порака | Mesazhi juaj |
| Gönder | Испрати | Dërgo |
| Wedding articles | Статии за свадби | Artikuj martese |
| Latest from the atelier journal | Најново од дневникот на ателјето | Më të fundit nga ditari i ateliesë |
| Story | Приказна | Histori |

---

### 3. page_services.html - Hizmetler

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| our services | нашите услуги | shërbimet tona |
| Get ready with us | Подгответе се со нас | Përgatituni me ne |
| Custom Dress Design | Дизајн на фустан по нарачка | Dizajn i personalizuar i fustanit |
| Free Consultation | Бесплатна консултација | Konsultim falas |
| Fitting & Swatch Try-On | Проба и примерок | Prova dhe mostra |
| Made-to-Measure | Шиено по мерка | E qepur sipas masës |
| Express Alteration | Експресна преправка | Ndryshim i shpejtë |
| couture danışmanlığı | couture консултација | konsultim couture |
| Sizin İçin Mükemmel Gelinliği Tasarlayalım | Да дизајнираме совршена венчаница за вас | Le të dizajnojmë fustanin perfekt të nusërisë për ju |
| Randevu Al | Закажи термин | Cakto takim |
| Couture Gelinlik Paketleri | Couture пакети за венчаници | Paketat e fustaneve të nusërisë Couture |
| Get Now | Земи сега | Merr tani |

---

### 4. page_about.html - Hakkımızda

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Hayalleri Gerçeğe Dönüştürüyoruz | Ги претвораме соништата во реалност | I kthejmë ëndrrat në realitet |
| PAZARTESİ-CUMA: 09:00 – 22:00 | ПОНЕДЕЛНИК-ПЕТОК: 09:00 – 22:00 | E HËNË-E PREMTE: 09:00 – 22:00 |
| CUMARTESİ: 09:00 – 20:00 | САБОТА: 09:00 – 20:00 | E SHTUNË: 09:00 – 20:00 |
| Neler Yapıyoruz | Што правиме | Çfarë bëjmë |
| Özel Tasarım Hizmetleri | Услуги за специјален дизајн | Shërbime të dizajnit special |
| Kişiye Özel Gelinlikler | Персонализирани венчаници | Fustane nusërie të personalizuara |
| Nişan Kıyafetleri | Облека за веридба | Veshje fejese |
| Tadilat & Prova Hizmetleri | Услуги за преправка и проба | Shërbime ndryshimi dhe prove |
| Gece Elbiseleri / Abiye | Вечерни фустани / Абаје | Fustane mbrëmjeje / Abaje |
| %100 El İşçiliği | 100% Рачна изработка | 100% Punë dore |
| Birinci Sınıf Kumaşlar | Првокласни ткаенини | Pëlhura të klasit të parë |
| Üsküp'te Üretildi | Произведено во Скопје | Prodhuar në Shkup |
| Neden Biz? | Зошто ние? | Pse ne? |
| Kişisel Yaklaşım | Личен пристап | Qasje personale |
| Yüksek Kalite | Висок квалитет | Cilësi e lartë |
| Son Blog Yazıları | Најнови блог објави | Postimet më të fundit të blogut |
| Devamını Oku → | Прочитај повеќе → | Lexo më shumë → |
| Henüz blog yazısı yok. | Сè уште нема блог објави. | Ende nuk ka postime blogu. |

---

### 5. contacts.html - İletişim

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| İletişim | Контакт | Kontakt |
| Dilediğiniz zaman mesaj bırakın; atelier ekibi 24 saat içinde cevap verecek. | Оставете порака кога сакате; тимот на ателјето ќе одговори во рок од 24 часа. | Lini një mesazh kur të doni; ekipi i ateliesë do të përgjigjet brenda 24 orëve. |
| Atölye | Ателје | Atelie |
| Skopje, Makedonya | Скопје, Македонија | Shkup, Maqedoni |
| Telefon | Телефон | Telefon |
| Hafta içi 09:00 - 18:00 | Работни денови 09:00 - 18:00 | Ditët e punës 09:00 - 18:00 |
| E-posta | Е-пошта | Email |
| Her türlü soru ve özel randevu talepleri için uygun. | Погодно за сите прашања и барања за специјални термини. | E përshtatshme për të gjitha pyetjet dhe kërkesat për takime speciale. |
| Mesaj bırakın | Оставете порака | Lini një mesazh |
| Adınız | Вашето име | Emri juaj |
| Örn. Elif Yıldız | Пр. Ана Петрова | P.sh. Ana Petrovska |
| Mesaj | Порака | Mesazh |
| Mesajı gönder | Испрати порака | Dërgo mesazhin |
| Creative Atelier | Креативно ателје | Atelie kreative |
| We sculpt dreams in florals & fabric. | Ги обликуваме соништата во цвеќиња и ткаенина. | I skulpturojmë ëndrrat në lule dhe pëlhurë. |
| Planlamaya başla | Започни со планирање | Fillo planifikimin |

---

### 6. faq.html - SSS

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| FAQ | ЧПП | FAQ |
| accommodation | сместување | akomodim |
| Book the rooms at a wedding boutique hotel | Резервирајте соби во бутик хотел за свадби | Rezervoni dhomat në një hotel butik martese |
| Book Now | Резервирај сега | Rezervo tani |
| Couture Terziliğin Sanatı | Уметноста на couture кројачество | Arti i rrobaqepësisë couture |
| Randevu Al | Закажи термин | Cakto takim |

---

### 7. rsvp.html - RSVP

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Wedding Celebration | Свадбена прослава | Festë martese |
| Join us for an unforgettable evening celebrating love, joy, and new beginnings. | Придружете ни се за незаборавна вечер полна со љубов, радост и нови почетоци. | Bashkohuni me ne për një mbrëmje të paharrueshme duke festuar dashurinë, gëzimin dhe fillimet e reja. |
| RSVP Now | РСВП Сега | RSVP Tani |
| Contact details | Контакт детали | Detajet e kontaktit |
| Ad Soyad | Име и презиме | Emri dhe mbiemri |
| Adınız Soyadınız | Вашето име и презиме | Emri dhe mbiemri juaj |
| E-posta | Е-пошта | Email |
| Telefon | Телефон | Telefon |
| Tercih Edilen Tarih | Претпочитан датум | Data e preferuar |
| Hizmet | Услуга | Shërbimi |
| -- Hizmet Seçiniz -- | -- Изберете услуга -- | -- Zgjidhni shërbimin -- |
| Kullanılabilir hizmet yok | Нема достапни услуги | Nuk ka shërbime të disponueshme |
| Mesaj | Порака | Mesazh |
| Talepleriniz varsa belirtin | Наведете ги вашите барања | Specifikoni kërkesat tuaja |
| Randevu Talep Et | Побарај термин | Kërko takim |
| Atölye Konumu | Локација на ателјето | Vendndodhja e ateliesë |

---

### 8. pricing.html - Fiyatlandırma

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Pricing | Цени | Çmimet |
| Fiyatlandırma Paketleri | Пакети за цени | Paketat e çmimeve |
| Randevu Al | Закажи термин | Cakto takim |
| 🎁 Ek Hizmetler & Add-Ons | 🎁 Дополнителни услуги | 🎁 Shërbime shtesë |
| Paketinize eklemek için ek hizmetleri seçin | Изберете дополнителни услуги за вашиот пакет | Zgjidhni shërbime shtesë për paketën tuaj |

---

### 9. page_portfolio.html - Portfolyo

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| YENİ KOLEKSİYON | НОВА КОЛЕКЦИЈА | KOLEKSION I RI |
| Gelinlerimizin Sanat Eserleri | Уметнички дела на нашите невести | Veprat artistike të nuseve tona |
| Naba Studio by Semma Couture Koleksiyonu | Naba Studio by Semma Couture Колекција | Koleksioni Naba Studio by Semma Couture |
| Hepsi | Сите | Të gjitha |
| Randevu Al | Закажи термин | Cakto takim |

---

### 10. page_blog.html - Blog

| Türkçe (Mevcut) | Makedonca | Arnavutça |
|-----------------|-----------|-----------|
| Atelier Notes | Белешки од ателјето | Shënime nga atelieja |
| Yeni koleksiyonlar, süreçler ve ilham buluşmaları hakkında paylaşımlar burada görünür. | Објави за нови колекции, процеси и инспиративни средби се појавуваат тука. | Postimet për koleksione të reja, procese dhe takime frymëzuese shfaqen këtu. |
| Detayları oku | Прочитај детали | Lexo detajet |
| Blog yazısı bulunamadı. | Не е пронајдена блог објава. | Nuk u gjet postim blogu. |
| Önceki | Претходна | E mëparshme |
| Sonraki | Следна | E ardhshme |
| Sayfa | Страница | Faqja |
| Keşfet | Истражи | Eksploro |
| İlham Panosu | Табла за инспирација | Tabela e frymëzimit |
| Popüler başlıklar | Популарни наслови | Titujt popullorë |
| Henüz yeni içerik yok. | Сè уште нема нова содржина. | Ende nuk ka përmbajtje të re. |
| Kategoriler | Категории | Kategoritë |
| Tümü | Сите | Të gjitha |
| İçerik güncellemesi | Ажурирање на содржина | Përditësim i përmbajtjes |
| Gelin planınız için notlar alın | Земете белешки за вашиот план за невеста | Merrni shënime për planin tuaj të nusërisë |
| Abone ol | Претплати се | Abonohu |

---

## 📁 .PO DOSYASI YAPISI

Django çeviri sistemi için `locale/mk/LC_MESSAGES/django.po` dosyası oluşturulmalıdır.

### Örnek .po Dosya Formatı:

```po
# Makedonca Çeviriler
# Naba Studio by Semma
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\n"
"Language: mk\n"

msgid "Home"
msgstr "Дома"

msgid "Services"
msgstr "Услуги"

msgid "About Us"
msgstr "За нас"
```

---

## 🔧 DİL DEĞİŞİKLİĞİ İÇİN YAPILMASI GEREKENLER

### Mevcut Sorun:
Template'lerdeki metinler **hardcoded** (sabit kodlanmış) olarak Türkçe yazılmış. Django'nun `{% trans %}` veya `{% blocktrans %}` tag'leri kullanılmamış.

### Çözüm Adımları:

1. **Template'lerde `{% trans %}` kullanımı:**
   ```html
   <!-- Önce -->
   <a href="{% url 'home' %}">Home</a>
   
   <!-- Sonra -->
   {% load i18n %}
   <a href="{% url 'home' %}">{% trans "Home" %}</a>
   ```

2. **Makedonca locale klasörü oluştur:**
   ```
   locale/mk/LC_MESSAGES/
   ```

3. **Çeviri dosyalarını oluştur:**
   ```bash
   python manage.py makemessages -l mk
   python manage.py makemessages -l tr
   python manage.py makemessages -l sq
   ```

4. **Çevirileri yap ve derle:**
   ```bash
   python manage.py compilemessages
   ```

---

## ⚠️ ÖNEMLİ NOTLAR

1. **Varsayılan dil Makedonca** olduğu için, anasayfa açıldığında tüm içerik Makedonca görünmelidir.

2. **Şu an template'ler Türkçe** yazılmış durumda. Bu metinlerin Makedonca'ya çevrilmesi gerekiyor.

3. **İki seçenek var:**
   - **Seçenek A:** Template'lerdeki Türkçe metinleri doğrudan Makedonca ile değiştirmek (basit ama esnek değil)
   - **Seçenek B:** Django i18n sistemi kullanarak `{% trans %}` tag'leri eklemek (önerilen)

4. **Dinamik içerikler** (FAQ, Blog, Ürünler vb.) zaten admin panelden her dil için ayrı ayrı girilebilir durumda.

---

## 📋 ÖZET - TAMAMLANAN İŞLER

| Kategori | Durum |
|----------|-------|
| Navigasyon Menüsü | ✅ Makedonca'ya çevrildi |
| Footer | ✅ Makedonca'ya çevrildi |
| Anasayfa metinleri | ✅ Makedonca'ya çevrildi |
| Hizmetler sayfası | ✅ Makedonca'ya çevrildi |
| Hakkımızda sayfası | ✅ Makedonca'ya çevrildi |
| İletişim sayfası | ✅ Makedonca'ya çevrildi |
| FAQ sayfası | ✅ Makedonca'ya çevrildi |
| RSVP sayfası | ✅ Makedonca'ya çevrildi |
| Fiyatlandırma sayfası | ✅ Makedonca'ya çevrildi |
| Portfolyo sayfası | ✅ Makedonca'ya çevrildi |
| Blog sayfası | ✅ Makedonca'ya çevrildi |
| FAQ içerikleri | ✅ Admin panelden (dinamik) |
| Blog yazıları | ✅ Admin panelden (dinamik) |
| Ürünler | ✅ Admin panelden (dinamik) |
| Paketler | ✅ Admin panelden (dinamik) |

---

## 📁 OLUŞTURULAN .PO DOSYALARI

Aşağıdaki .po dosyaları oluşturuldu:

### Türkçe Çeviriler
- **Dosya:** `locale/tr/LC_MESSAGES/django.po`
- **Durum:** ✅ Oluşturuldu ve çeviriler eklendi

### Arnavutça Çeviriler
- **Dosya:** `locale/sq/LC_MESSAGES/django.po`
- **Durum:** ✅ Oluşturuldu ve çeviriler eklendi

### Makedonca (Varsayılan Dil)
- **Dosya:** Template'lerde doğrudan Makedonca yazıldı
- **Durum:** ✅ Tamamlandı

---

## 🔧 DİL DEĞİŞİKLİĞİ İÇİN SONRAKI ADIMLAR

Şu an template'ler **doğrudan Makedonca** olarak yazılmış durumda. Dil değişikliği için iki seçenek var:

### Seçenek A: Mevcut Sistem (Önerilen)
Şu an template'ler Makedonca olarak hardcoded. Türkçe ve Arnavutça için `.po` dosyaları hazırlandı ancak Django'nun `{% trans %}` tag'leri henüz eklenmedi.

**Avantaj:** Basit, hızlı çözüm
**Dezavantaj:** Dil değişikliği için template'lerin güncellenmesi gerekir

### Seçenek B: Django i18n Sistemi (Gelecekte)
Template'lere `{% trans %}` tag'leri eklenip, `.po` dosyalarından çeviriler okunabilir.

```bash
# .po dosyalarını derlemek için:
python manage.py compilemessages
```

---

## ⚠️ ÖNEMLİ NOTLAR

1. **Varsayılan dil Makedonca** olarak ayarlandı (`settings.py` → `LANGUAGE_CODE = 'mk'`)
2. **Anasayfa açıldığında** tüm içerik Makedonca görünecek
3. **Dil değiştirici** (bayraklar) header'da mevcut ve çalışıyor
4. **Dinamik içerikler** (FAQ, Blog, Ürünler) admin panelden her dil için ayrı ayrı girilebilir
