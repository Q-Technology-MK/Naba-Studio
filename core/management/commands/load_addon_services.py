from django.core.management.base import BaseCommand
from core.models import AddOnService


class Command(BaseCommand):
    help = "Load Add-On Services for pricing page"

    def handle(self, *args, **options):
        addon_services = [
            {
                "name": "Ücretsiz İlk Danışmanlık",
                "name_tr": "Ücretsiz İlk Danışmanlık",
                "name_sq": "Konsultimi i Parë Falas",
                "description": "Besplatna inicijalna konsultacija sa diskusijom o dizajnu i prezentacijom tkanina",
                "description_tr": "Ücretsiz ilk görüşme, tasarım konuşması ve kumaş seçimi tanıtımı. En çok müşteri çeken hizmet.",
                "description_sq": "Konsultim falas me diskutim për dizajnin dhe shfaqje të pëlhurave",
                "price": "Ücretsiz",
                "icon": "✨",
                "order": 1,
            },
            {
                "name": "Kişiye Özel Tasarım Çizimi",
                "name_tr": "Kişiye Özel Tasarım Çizimi",
                "name_sq": "Skicë Personalizuar e Dizajnit",
                "description": "Profesionalna prilagođena skica/ilustracija na osnovu preferencija klijenta",
                "description_tr": "1 adet profesyonel tasarım çizimi. Müşterinin istediği modelden ilham alınarak özel çizim yapılır.",
                "description_sq": "1 skicë profesionale të përshtatur sipas preferencave të klientit",
                "price": "Ücretsiz",
                "icon": "🎨",
                "order": 2,
            },
            {
                "name": "Kapsamlı Ölçü Alma Hizmeti",
                "name_tr": "Kapsamlı Ölçü Alma Hizmeti",
                "name_sq": "Shërbimi i Matjeve Gjithëpërfshirëse",
                "description": "Profesionalno mjerenje tela i preporuke modela na osnovu tipa tijela",
                "description_tr": "Profesyonel vücut ölçülendirme ve vücut tipine göre model önerisi. Paket içinde ücretsiz!",
                "description_sq": "Matjet profesionale të trupit dhe rekomandime modelesh sipas tipit të trupit",
                "price": "Ücretsiz",
                "icon": "📏",
                "order": 3,
            },
            {
                "name": "Prova Seçenekleri",
                "name_tr": "Prova Seçenekleri",
                "name_sq": "Opsionet e Provimit",
                "description": "Basic: 2 prova | Standard: 3 prova | Premium: Sınırsız prova",
                "description_tr": "Farklı paketlerde farklı prova sayıları. Gelinler prova sayısını bilmek ister.",
                "description_sq": "Bazike: 2 prova | Standard: 3 prova | Premium: Prova të pakufizuara",
                "price": "Pakete Dahil",
                "icon": "👗",
                "order": 4,
            },
            {
                "name": "Express Delivery",
                "name_tr": "Acele Teslimat Hizmeti",
                "name_sq": "Shërbimi i Dorëzimit të Shpejtë",
                "description": "Hızlı dikim hizmeti (15-25 gün). Son dakika gelinleri için çok çekici",
                "description_tr": "Ekspres (acele) üretim hizmeti. 15-25 gün içinde teslim. Son dakika gelinleri için perfect.",
                "description_sq": "Shërbim i shpejtë i dikimit (15-25 ditë) për nuset e minutës së fundit",
                "price": "+500₺",
                "icon": "⚡",
                "order": 5,
            },
            {
                "name": "Premium Hediye Paketi",
                "name_tr": "Premium Hediye Paketi",
                "name_sq": "Paketa Premium e Dhuratës",
                "description": "Duvak hediye + Saç aksesuarı %50 indirim + Gelin kemeri hediye",
                "description_tr": "Duvak hediye + Saç aksesuarı %50 indirimli + Gelin kemeri hediye. Premium pakette harika görünür!",
                "description_sq": "Dhurata velu + Aksesor flokësh 50% zbritje + Kordon i nusërisë",
                "price": "Premium Paket",
                "icon": "🎁",
                "order": 6,
            },
            {
                "name": "Tasarım Değişiklikleri Dahil",
                "name_tr": "Tasarım Değişiklikleri Dahil",
                "name_sq": "Modifikimet e Dizajnit të Përfshira",
                "description": "Yaka, kol, etek boyu ve bel hattı değişiklikleri dahil",
                "description_tr": "Yaka değişikliği, kol ekleme, etek boyu ayarlama - hepsi paket içinde ücretsiz!",
                "description_sq": "Ndryshime në jakë, mëngë, gjatësinë e fundit dhe linjën e belit",
                "price": "Paket İçinde",
                "icon": "✂️",
                "order": 7,
            },
            {
                "name": "Profesyonel Kumaş Danışmanlığı",
                "name_tr": "Profesyonel Kumaş Danışmanlığı",
                "name_sq": "Konsultanca Profesionale për Pëlhurën",
                "description": "Kumaş türü seçimi, doku/dikim dayanıklılığı ve ton karşılaştırması",
                "description_tr": "Kumaş türü seçimi, dokulu ve dayanıklılık inceleme, ton karşılaştırma danışmanlığı",
                "description_sq": "Zgjedhja e llojit të pëlhurës, analiza e teksturës dhe krahasimi i ngjyrave",
                "price": "Premium Paket",
                "icon": "🧵",
                "order": 8,
            },
            {
                "name": "Son Gün Ütü/Buharlama Ücretsiz",
                "name_tr": "Son Gün Ütü/Buharlama Ücretsiz",
                "name_sq": "Hekurimi/Avulli i Ditës Së Fundit Falas",
                "description": "Düğün gününden önce profesyonel hazırlama ve ütüleme",
                "description_tr": "Düğün günü öncesi gelinliğin profesyonel sterilasyon/ütüleme hizmeti ücretsiz",
                "description_sq": "Përgatitje dhe uthullim profesional para ditës së martesës",
                "price": "Ücretsiz",
                "icon": "♨️",
                "order": 9,
            },
            {
                "name": "Premium Saklama Çantası",
                "name_tr": "Premium Saklama Çantası",
                "name_sq": "Çanta e Sigurt Premium",
                "description": "Toz geçirmez özel koruma çantası teslim ile birlikte",
                "description_tr": "Toz geçirmez özel çanta ile teslimat. Premium pakette ücretsiz. Çok profesyonel durur.",
                "description_sq": "Çantë mbrojtëse spesiale pa hyrjen e pluhurit me dorëzimin",
                "price": "Premium Paket",
                "icon": "📦",
                "order": 10,
            },
            {
                "name": "Online Tasarım Toplantısı",
                "name_tr": "Online Tasarım Toplantısı",
                "name_sq": "Takim Online i Dizajnit",
                "description": "Video görüşme ile tasarım konsultasyonu ve kumaş gösterimi",
                "description_tr": "Şehir dışındaki gelinler için video call üzerinden tasarım danışmanlığı ve kumaş gösterimi",
                "description_sq": "Konsultacion i dizajnit përmes video dhe shfaqje të pëlhurave për klientët e largët",
                "price": "Ücretsiz",
                "icon": "💻",
                "order": 11,
            },
            {
                "name": "Dış Çekim Hazırlığı",
                "name_tr": "Dış Çekim Hazırlığı",
                "name_sq": "Përgatitje për Foto-Sesionin",
                "description": "Profesyonel stilizasyon ve gelinlik ayarlaması dış çekimler için",
                "description_tr": "Dış çekimler öncesi profesyonel stilizasyon, gelinlik ayarlaması ve saç-makyöz koordinasyonu",
                "description_sq": "Përgatitje profesionale para fotografimeve me stilizim dhe rregullime të fustanit",
                "price": "Premium Paket",
                "icon": "📸",
                "order": 12,
            },
        ]

        # Clear existing add-ons
        AddOnService.objects.all().delete()
        
        # Create add-on services
        created_count = 0
        for addon_data in addon_services:
            addon = AddOnService.objects.create(**addon_data)
            created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f"Uspesno ucitani {created_count} Add-On servisa - Makedonski, Albanski, Turski")
        )
