"""
Custom template tags for multilingual content display.
"""
from django import template
from django.utils.translation import get_language

register = template.Library()

# Static text translations dictionary
STATIC_TEXTS = {
    # Navigation
    'nav_home': {'mk': 'Дома', 'tr': 'Ana Sayfa', 'sq': 'Ballina'},
    'nav_services': {'mk': 'Услуги', 'tr': 'Hizmetler', 'sq': 'Shërbimet'},
    'nav_corporate': {'mk': 'Корпоративно', 'tr': 'Kurumsal', 'sq': 'Korporata'},
    'nav_about': {'mk': 'За нас', 'tr': 'Hakkımızda', 'sq': 'Rreth nesh'},
    'nav_rsvp': {'mk': 'РСВП', 'tr': 'RSVP', 'sq': 'RSVP'},
    'nav_faq': {'mk': 'ЧПП', 'tr': 'SSS', 'sq': 'Pyetjet e Shpeshta'},
    'nav_pricing': {'mk': 'Цени', 'tr': 'Fiyatlandırma', 'sq': 'Çmimet'},
    'nav_portfolio': {'mk': 'Портфолио', 'tr': 'Portfolyo', 'sq': 'Portofoli'},
    'nav_blog': {'mk': 'Блог', 'tr': 'Blog', 'sq': 'Blog'},
    'nav_contact': {'mk': 'Контакт', 'tr': 'İletişim', 'sq': 'Kontakt'},
    
    # Footer
    'footer_office': {'mk': 'Канцеларија', 'tr': 'Ofis', 'sq': 'Zyra'},
    'footer_links': {'mk': 'Линкови', 'tr': 'Linkler', 'sq': 'Lidhjet'},
    'footer_contact_us': {'mk': 'Контактирајте нè', 'tr': 'İletişime Geçin', 'sq': 'Na kontaktoni'},
    
    # Home Page
    'home_hero_title': {'mk': 'Атеље во срцето на Скопје', 'tr': "Üsküp'ün Kalbinde Bir Atölye", 'sq': 'Një atelie në zemër të Shkupit'},
    'home_hero_subtitle': {'mk': 'Најпрестижното couture атеље за венчаници во Северна Македонија. Секоја венчаница има своја приказна. Дали си подготвена да ја напишеш твојата?', 'tr': "Kuzey Makedonya'nın en prestijli couture gelinlik tasarım atölyesi. Her gelinliğin bir hikâyesi vardır. Seninkini yazmaya hazır mısın?", 'sq': 'Atelieja më prestigjioze e fustaneve të nusërisë couture në Maqedoninë e Veriut. Çdo fustan nusërie ka një histori. A jeni gati të shkruani tuajën?'},
    'home_memory': {'mk': 'Секоја венчаница има свој спомен', 'tr': 'Her Gelinliğin Bir Anısı Vardır', 'sq': 'Çdo fustan nusërie ka një kujtim'},
    'home_couture': {'mk': 'посебно шиење couture', 'tr': 'özel dikim couture', 'sq': 'qepje e veçantë couture'},
    'home_designed': {'mk': 'Венчаници дизајнирани од нула', 'tr': 'Sıfırdan Tasarlanan Gelinlikler', 'sq': 'Fustane nusërie të dizajnuara nga zeroja'},
    'home_weekdays': {'mk': 'ПОНЕДЕЛНИК-ПЕТОК', 'tr': 'PAZARTESİ-CUMA', 'sq': 'E HËNË-E PREMTE'},
    'home_saturday': {'mk': 'САБОТА', 'tr': 'CUMARTESİ', 'sq': 'E SHTUNË'},
    'home_what_we_do': {'mk': 'што правиме', 'tr': 'ne yapıyoruz', 'sq': 'çfarë bëjmë'},
    'home_sewing_services': {'mk': 'Услуги за шиење венчаници', 'tr': 'Gelinlik Dikim Hizmetleri', 'sq': 'Shërbime qepjeje për nuse'},
    'home_alterations': {'mk': 'Преправки', 'tr': 'Tadilat', 'sq': 'Ndryshime'},
    'home_dress_sewing': {'mk': 'Шиење фустани', 'tr': 'Elbise Dikimi', 'sq': 'Qepje fustanesh'},
    'home_tailoring': {'mk': 'Кројачество', 'tr': 'Terzilik', 'sq': 'Rrobaqepësi'},
    'home_dress_shop': {'mk': 'продавница за фустани', 'tr': 'elbise mağazası', 'sq': 'dyqan fustanesh'},
    'home_ready_to_wear': {'mk': 'Готови за носење', 'tr': 'Hazır Giyim', 'sq': 'Gati për tu veshur'},
    'home_our_brides': {'mk': 'нашите невести', 'tr': 'gelinlerimiz', 'sq': 'nusat tona'},
    'home_dress_gallery': {'mk': 'Галерија на фустани', 'tr': 'Elbise Galerisi', 'sq': 'Galeria e fustaneve'},
    'home_view_collection': {'mk': 'Погледни ја целата колекција', 'tr': 'Tüm Koleksiyonu Gör', 'sq': 'Shiko të gjithë koleksionin'},
    'home_questions': {'mk': 'Имате прашања?', 'tr': 'Sorularınız mı var?', 'sq': 'Keni pyetje?'},
    'home_your_name': {'mk': 'Вашето име', 'tr': 'Adınız', 'sq': 'Emri juaj'},
    'home_email': {'mk': 'Е-пошта', 'tr': 'E-posta', 'sq': 'Email'},
    'home_your_message': {'mk': 'Вашата порака', 'tr': 'Mesajınız', 'sq': 'Mesazhi juaj'},
    'home_send': {'mk': 'Испрати', 'tr': 'Gönder', 'sq': 'Dërgo'},
    'home_wedding_articles': {'mk': 'Статии за свадби', 'tr': 'Düğün Makaleleri', 'sq': 'Artikuj martese'},
    'home_latest_from_diary': {'mk': 'Најново од дневникот на атељето', 'tr': 'Atölye Günlüğünden En Yeniler', 'sq': 'Më të fundit nga ditari i ateliesë'},
    'home_story': {'mk': 'Приказна', 'tr': 'Hikaye', 'sq': 'Histori'},
    
    # Services Page
    'services_our_services': {'mk': 'нашите услуги', 'tr': 'hizmetlerimiz', 'sq': 'shërbimet tona'},
    'services_prepare_with_us': {'mk': 'Подгответе се со нас', 'tr': 'Bizimle Hazırlanın', 'sq': 'Përgatituni me ne'},
    'services_custom_design': {'mk': 'Дизајн на фустан по нарачка', 'tr': 'Özel Elbise Tasarımı', 'sq': 'Dizajn i personalizuar i fustanit'},
    'services_free_consultation': {'mk': 'Бесплатна консултација', 'tr': 'Ücretsiz Danışmanlık', 'sq': 'Konsultim falas'},
    'services_fitting_samples': {'mk': 'Проба и примероци', 'tr': 'Prova ve Numune', 'sq': 'Prova dhe mostra'},
    'services_custom_tailoring': {'mk': 'Шиено по мерка', 'tr': 'Ölçüye Göre Dikim', 'sq': 'E qepur sipas masës'},
    'services_express_alterations': {'mk': 'Експресна преправка', 'tr': 'Ekspres Tadilat', 'sq': 'Ndryshim i shpejtë'},
    'services_couture_consultation': {'mk': 'couture консултација', 'tr': 'couture danışmanlığı', 'sq': 'konsultim couture'},
    'services_design_perfect': {'mk': 'Да дизајнираме совршена венчаница за вас', 'tr': 'Sizin İçin Mükemmel Gelinliği Tasarlayalım', 'sq': 'Le të dizajnojmë fustanin perfekt të nusërisë për ju'},
    'services_book_appointment': {'mk': 'Закажи термин', 'tr': 'Randevu Al', 'sq': 'Cakto takim'},
    'services_couture_packages': {'mk': 'Couture пакети за венчаници', 'tr': 'Couture Gelinlik Paketleri', 'sq': 'Paketat e fustaneve të nusërisë Couture'},
    'services_get_now': {'mk': 'Земи сега', 'tr': 'Şimdi Al', 'sq': 'Merr tani'},
    
    # About Page
    'about_dreams_reality': {'mk': 'Ги претвораме соништата во реалност', 'tr': 'Hayalleri Gerçeğe Dönüştürüyoruz', 'sq': 'I kthejmë ëndrrat në realitet'},
    'about_what_we_do': {'mk': 'Што правиме', 'tr': 'Neler Yapıyoruz', 'sq': 'Çfarë bëjmë'},
    'about_special_design': {'mk': 'Услуги за специјален дизајн', 'tr': 'Özel Tasarım Hizmetleri', 'sq': 'Shërbime të dizajnit special'},
    'about_personalized': {'mk': 'Персонализирани венчаници', 'tr': 'Kişiye Özel Gelinlikler', 'sq': 'Fustane nusërie të personalizuara'},
    'about_engagement': {'mk': 'Облека за веридба', 'tr': 'Nişan Kıyafetleri', 'sq': 'Veshje fejese'},
    'about_alteration_fitting': {'mk': 'Услуги за преправка и проба', 'tr': 'Tadilat ve Prova Hizmetleri', 'sq': 'Shërbime ndryshimi dhe prove'},
    'about_evening_dresses': {'mk': 'Вечерни фустани / Абаје', 'tr': 'Gece Elbiseleri / Abiye', 'sq': 'Fustane mbrëmjeje / Abaje'},
    'about_handmade': {'mk': '100% Рачна изработка', 'tr': '%100 El İşçiliği', 'sq': '100% Punë dore'},
    'about_first_class': {'mk': 'Првокласни ткаенини', 'tr': 'Birinci Sınıf Kumaşlar', 'sq': 'Pëlhura të klasit të parë'},
    'about_made_in_skopje': {'mk': 'Произведено во Скопје', 'tr': "Üsküp'te Üretildi", 'sq': 'Prodhuar në Shkup'},
    'about_why_us': {'mk': 'Зошто ние?', 'tr': 'Neden Biz?', 'sq': 'Pse ne?'},
    'about_personal_approach': {'mk': 'Личен пристап', 'tr': 'Kişisel Yaklaşım', 'sq': 'Qasje personale'},
    'about_high_quality': {'mk': 'Висок квалитет', 'tr': 'Yüksek Kalite', 'sq': 'Cilësi e lartë'},
    'about_latest_blog': {'mk': 'Најнови блог објави', 'tr': 'Son Blog Yazıları', 'sq': 'Postimet më të fundit të blogut'},
    'about_read_more': {'mk': 'Прочитај повеќе →', 'tr': 'Devamını Oku →', 'sq': 'Lexo më shumë →'},
    'about_no_blog': {'mk': 'Сè уште нема блог објави.', 'tr': 'Henüz blog yazısı yok.', 'sq': 'Ende nuk ka postime blogu.'},
    
    # Contact Page
    'contact_leave_message': {'mk': 'Оставете порака кога сакате; тимот на атељето ќе одговори во рок од 24 часа.', 'tr': 'Dilediğiniz zaman mesaj bırakın; atölye ekibi 24 saat içinde cevap verecek.', 'sq': 'Lini një mesazh kur të doni; ekipi i ateliesë do të përgjigjet brenda 24 orëve.'},
    'contact_atelier': {'mk': 'Атеље', 'tr': 'Atölye', 'sq': 'Atelie'},
    'contact_skopje': {'mk': 'Скопје, Македонија', 'tr': 'Üsküp, Makedonya', 'sq': 'Shkup, Maqedoni'},
    'contact_phone': {'mk': 'Телефон', 'tr': 'Telefon', 'sq': 'Telefon'},
    'contact_working_days': {'mk': 'Работни денови 09:00 - 18:00', 'tr': 'Hafta içi 09:00 - 18:00', 'sq': 'Ditët e punës 09:00 - 18:00'},
    'contact_suitable': {'mk': 'Погодно за сите прашања и барања за специјални термини.', 'tr': 'Her türlü soru ve özel randevu talepleri için uygun.', 'sq': 'E përshtatshme për të gjitha pyetjet dhe kërkesat për takime speciale.'},
    'contact_leave_msg': {'mk': 'Оставете порака', 'tr': 'Mesaj Bırakın', 'sq': 'Lini një mesazh'},
    'contact_message': {'mk': 'Порака', 'tr': 'Mesaj', 'sq': 'Mesazh'},
    'contact_send_message': {'mk': 'Испрати порака', 'tr': 'Mesajı Gönder', 'sq': 'Dërgo mesazhin'},
    'contact_creative_atelier': {'mk': 'Креативно атеље', 'tr': 'Yaratıcı Atölye', 'sq': 'Atelie kreative'},
    'contact_shaping_dreams': {'mk': 'Ги обликуваме соништата во цвеќиња и ткаенина.', 'tr': 'Hayalleri çiçekler ve kumaşlarla şekillendiriyoruz.', 'sq': 'I skulpturojmë ëndrrat në lule dhe pëlhurë.'},
    'contact_start_planning': {'mk': 'Започни со планирање', 'tr': 'Planlamaya Başla', 'sq': 'Fillo planifikimin'},
    
    # FAQ Page
    'faq_title': {'mk': 'ЧПП', 'tr': 'SSS', 'sq': 'FAQ'},
    'faq_accommodation': {'mk': 'Закажете термин', 'tr': 'Randevu Alın', 'sq': 'Caktoni një takim'},
    'faq_book_rooms': {'mk': 'Посетете го нашиот атеље за персонализирана консултација за вашиот совршен венчален фустан', 'tr': 'Mükemmel gelinliğiniz için kişiselleştirilmiş danışmanlık almak üzere atölyemizi ziyaret edin', 'sq': 'Vizitoni ateljen tonë për konsultim të personalizuar për fustanin tuaj të përsosur të nusërisë'},
    'faq_book_now': {'mk': 'Закажи термин', 'tr': 'Randevu Al', 'sq': 'Cakto takim'},
    'faq_couture_art': {'mk': 'Уметноста на couture кројачество', 'tr': 'Couture Terziliğin Sanatı', 'sq': 'Arti i rrobaqepësisë couture'},
    'faq_couture_desc': {'mk': 'Во нашето атеље во Северна Македонија, секоја венчаница е дизајнирана како уметничко дело. Создаваме венчаници по мерка според вашите мерки, стил и соништа. Направете консултација, започнете да ја дизајнирате вашата венчаница.', 'tr': "Kuzey Makedonya'daki atölyemizde her gelinlik bir sanat eseri olarak tasarlanır. Ölçülerinize, tarzınıza ve hayallerinize göre özel gelinlikler yaratıyoruz. Danışmanlık alın, gelinliğinizi tasarlamaya başlayın.", 'sq': 'Në ateljen tonë në Maqedoninë e Veriut, çdo fustan nusërie është dizajnuar si vepër arti. Krijojmë fustane nusërie sipas masave, stilit dhe ëndrrave tuaja. Bëni një konsultim, filloni të dizajnoni fustanin tuaj të nusërisë.'},
    
    # RSVP Page
    'rsvp_celebration': {'mk': 'Свадбена прослава', 'tr': 'Düğün Kutlaması', 'sq': 'Festë martese'},
    'rsvp_join_us': {'mk': 'Придружете ни се за незаборавна вечер полна со љубов, радост и нови почетоци.', 'tr': 'Aşk, neşe ve yeni başlangıçlarla dolu unutulmaz bir akşam için bize katılın.', 'sq': 'Bashkohuni me ne për një mbrëmje të paharrueshme duke festuar dashurinë, gëzimin dhe fillimet e reja.'},
    'rsvp_now': {'mk': 'РСВП Сега', 'tr': 'Şimdi RSVP', 'sq': 'RSVP Tani'},
    'rsvp_contact_details': {'mk': 'Контакт детали', 'tr': 'İletişim Bilgileri', 'sq': 'Detajet e kontaktit'},
    'rsvp_full_name': {'mk': 'Име и презиме', 'tr': 'Ad Soyad', 'sq': 'Emri dhe mbiemri'},
    'rsvp_preferred_date': {'mk': 'Претпочитан датум', 'tr': 'Tercih Edilen Tarih', 'sq': 'Data e preferuar'},
    'rsvp_service': {'mk': 'Услуга', 'tr': 'Hizmet', 'sq': 'Shërbimi'},
    'rsvp_select_service': {'mk': '-- Изберете услуга --', 'tr': '-- Hizmet Seçiniz --', 'sq': '-- Zgjidhni shërbimin --'},
    'rsvp_no_services': {'mk': 'Нема достапни услуги', 'tr': 'Kullanılabilir hizmet yok', 'sq': 'Nuk ka shërbime të disponueshme'},
    'rsvp_specify_requests': {'mk': 'Наведете ги вашите барања', 'tr': 'Taleplerinizi belirtin', 'sq': 'Specifikoni kërkesat tuaja'},
    'rsvp_request_appointment': {'mk': 'Побарај термин', 'tr': 'Randevu Talep Et', 'sq': 'Kërko takim'},
    'rsvp_atelier_location': {'mk': 'Локација на атељето', 'tr': 'Atölye Konumu', 'sq': 'Vendndodhja e ateliesë'},
    
    # Pricing Page
    'pricing_packages': {'mk': 'Пакети за цени', 'tr': 'Fiyatlandırma Paketleri', 'sq': 'Paketat e çmimeve'},
    'pricing_additional': {'mk': 'Дополнителни услуги', 'tr': 'Ek Hizmetler', 'sq': 'Shërbime shtesë'},
    'pricing_select_additional': {'mk': 'Изберете дополнителни услуги за вашиот пакет', 'tr': 'Paketinize eklemek için ek hizmetleri seçin', 'sq': 'Zgjidhni shërbime shtesë për paketën tuaj'},
    
    # Portfolio Page
    'portfolio_collection': {'mk': 'Наша колекција', 'tr': 'Koleksiyonumuz', 'sq': 'Koleksioni ynë'},
    'portfolio_new_collection': {'mk': 'НОВА КОЛЕКЦИЈА', 'tr': 'YENİ KOLEKSİYON', 'sq': 'KOLEKSION I RI'},
    'portfolio_artworks': {'mk': 'Уметнички дела на нашите невести', 'tr': 'Gelinlerimizin Sanat Eserleri', 'sq': 'Veprat artistike të nuseve tona'},
    'portfolio_all': {'mk': 'Сите', 'tr': 'Hepsi', 'sq': 'Të gjitha'},
    'portfolio_details': {'mk': 'Детали', 'tr': 'Detaylar', 'sq': 'Detajet'},
    'portfolio_year': {'mk': 'Година', 'tr': 'Yıl', 'sq': 'Viti'},
    'portfolio_designer': {'mk': 'Дизајнер', 'tr': 'Tasarımcı', 'sq': 'Dizajneri'},
    'portfolio_features': {'mk': 'Карактеристики', 'tr': 'Özellikler', 'sq': 'Karakteristikat'},
    'portfolio_back': {'mk': 'Назад кон портфолио', 'tr': 'Portfolyoya Dön', 'sq': 'Kthehu te portofoli'},
    'portfolio_no_products': {'mk': 'Сè уште нема производи. Ве молиме проверете подоцна.', 'tr': 'Henüz ürün eklenmemiş. Lütfen daha sonra tekrar kontrol edin.', 'sq': 'Ende nuk ka produkte. Ju lutemi kontrolloni më vonë.'},
    
    # Blog Page
    'blog_notes': {'mk': 'Белешки од атељето', 'tr': 'Atölye Notları', 'sq': 'Shënime nga atelieja'},
    'blog_posts_appear': {'mk': 'Објави за нови колекции, процеси и инспиративни средби се појавуваат тука.', 'tr': 'Yeni koleksiyonlar, süreçler ve ilham buluşmaları hakkında paylaşımlar burada görünür.', 'sq': 'Postimet për koleksione të reja, procese dhe takime frymëzuese shfaqen këtu.'},
    'blog_read_details': {'mk': 'Прочитај детали', 'tr': 'Detayları Oku', 'sq': 'Lexo detajet'},
    'blog_not_found': {'mk': 'Не е пронајдена блог објава.', 'tr': 'Blog yazısı bulunamadı.', 'sq': 'Nuk u gjet postim blogu.'},
    'blog_previous': {'mk': 'Претходна', 'tr': 'Önceki', 'sq': 'E mëparshme'},
    'blog_next': {'mk': 'Следна', 'tr': 'Sonraki', 'sq': 'E ardhshme'},
    'blog_page': {'mk': 'Страница', 'tr': 'Sayfa', 'sq': 'Faqja'},
    'blog_explore': {'mk': 'Истражи', 'tr': 'Keşfet', 'sq': 'Eksploro'},
    'blog_inspiration': {'mk': 'Табла за инспирација', 'tr': 'İlham Panosu', 'sq': 'Tabela e frymëzimit'},
    'blog_popular': {'mk': 'Популарни наслови', 'tr': 'Popüler Başlıklar', 'sq': 'Titujt popullorë'},
    'blog_no_content': {'mk': 'Сè уште нема нова содржина.', 'tr': 'Henüz yeni içerik yok.', 'sq': 'Ende nuk ka përmbajtje të re.'},
    'blog_categories': {'mk': 'Категории', 'tr': 'Kategoriler', 'sq': 'Kategoritë'},
    'blog_content_update': {'mk': 'Ажурирање на содржина', 'tr': 'İçerik Güncellemesi', 'sq': 'Përditësim i përmbajtjes'},
    'blog_take_notes': {'mk': 'Земете белешки за вашиот план за невеста', 'tr': 'Gelin planınız için notlar alın', 'sq': 'Merrni shënime për planin tuaj të nusërisë'},
    'blog_subscribe': {'mk': 'Претплати се', 'tr': 'Abone Ol', 'sq': 'Abonohu'},
    'blog_share': {'mk': 'Сподели', 'tr': 'Paylaş', 'sq': 'Ndaj'},
    'blog_likes': {'mk': 'Допаѓања', 'tr': 'Beğeni', 'sq': 'Pëlqime'},
    'blog_tags': {'mk': 'Етикети', 'tr': 'Etiketler', 'sq': 'Etiketat'},
    'blog_all_posts': {'mk': 'Сите објави', 'tr': 'Tüm Yazılar', 'sq': 'Të gjitha postimet'},
    
    # General
    'skip_to_content': {'mk': 'Прескокни до содржина', 'tr': 'İçeriğe Atla', 'sq': 'Kalo te përmbajtja'},
    'show_menu': {'mk': 'Прикажи мени', 'tr': 'Menüyü Göster', 'sq': 'Shfaq menunë'},
    'go_up': {'mk': 'Оди горе', 'tr': 'Yukarı Çık', 'sq': 'Shko lart'},
}


@register.simple_tag(takes_context=True)
def t(context, key):
    """
    Get translated static text based on current language.
    Usage: {% t 'nav_home' %}
    """
    lang = get_language() or 'mk'
    if lang not in ['mk', 'tr', 'sq']:
        lang = 'mk'
    
    if key in STATIC_TEXTS:
        return STATIC_TEXTS[key].get(lang, STATIC_TEXTS[key].get('mk', key))
    return key


@register.filter
def get_lang(obj, attr_suffix):
    """
    Get language-specific attribute from an object.
    Usage: {{ object|get_lang:'title' }}
    Returns title_tr for Turkish, title_sq for Albanian, title for Macedonian
    """
    lang = get_language() or 'mk'
    
    if lang == 'tr':
        attr = f'{attr_suffix}_tr'
        value = getattr(obj, attr, None)
        if value:
            return value
    elif lang == 'sq':
        attr = f'{attr_suffix}_sq'
        value = getattr(obj, attr, None)
        if value:
            return value
    
    return getattr(obj, attr_suffix, '')


@register.simple_tag
def get_current_lang():
    """Get current language code"""
    return get_language() or 'mk'
