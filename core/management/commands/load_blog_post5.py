from django.core.management.base import BaseCommand
from core.models import BlogPost
from datetime import date


class Command(BaseCommand):
    help = 'Load fifth blog post about minimal bridal designs'

    def handle(self, *args, **options):
        # Check if post already exists
        if BlogPost.objects.filter(slug='sade-gelinlik-modelleri').exists():
            self.stdout.write(self.style.WARNING('Blog post already exists!'))
            return

        post = BlogPost.objects.create(
            title='Sade Gelinlik Modelleri: Zamansız Zarafetin Modern Yorumu',
            slug='sade-gelinlik-modelleri',
            excerpt='Sade gelinlik modelleri, "az ama etkili" felsefesini benimseyen kadınların zamansız tercihini temsil eder. Naba Studio by Semma için sadelik; yalnızca detayları azaltmak değil, her çizgiyi bilinçle tasarlamak anlamına gelir.',
            body='''<p>Sade gelinlik modelleri, "az ama etkili" felsefesini benimseyen kadınların zamansız tercihini temsil eder. Naba Studio by Semma için sadelik; yalnızca detayları azaltmak değil, her çizgiyi bilinçle tasarlamak anlamına gelir. Gösterişten uzak ama güçlü bir silüet yaratmayı hedefleyen bu yaklaşımda, kusursuz kalıp, kaliteli kumaş ve mükemmel oranlar ön plandadır.</p>

<p>Minimalist gelinlik tasarımlarımızda mat satenler, ipek tüller, organze ve doğal dökümlü kumaşlar; formun zarafetini destekleyen temel yapı taşlarıdır. İnce düşünülmüş korse yapısı, omuz hattının dengesi, bel vurgusu ve net kesim etekler, sade gelinlik modellerinde tasarımın asıl gücünü ortaya çıkarır. Her parça, gelinin duruşunu yüceltecek şekilde sessiz ama etkileyici bir estetik sunar.</p>

<h2>Sade Gelinlik Ne Anlatır?</h2>

<p>Sade gelinlik, gelinin karakterini ve içsel zarafetini öne çıkaran güçlü bir stil dilidir. Abartıdan uzak oluşu, aslında yüksek bir özgüveni temsil eder; çünkü tüm dikkat, detaylardan çok gelinin duruşunda, yüz ifadesinde ve enerjisinde toplanır. Modern, romantik ya da sofistike çizgilerle yorumlanabilen sade gelinlikler; doğallığa saygıyı, sadelikteki inceliği ve zamansız şıklığı simgeler.</p>

<p><a href="/blog/couture-gelinlik-modelleri/">Naba Studio by Semma'da sade gelinlik tasarımları</a>, Kuzey Makedonya'daki modern gelinlerin yaşam tarzına uyum sağlayacak şekilde özel dikim anlayışıyla hazırlanır. İster şehir düğünü, ister kır ya da butik davetler için olsun; sade bir gelinlik, doğru kalıp ve doğru kumaşla birleştiğinde her ortamda etkileyici bir imza haline gelir.</p>

<blockquote>
<p><em>Sade gelinlik, modaya göre değişen geçici bir trend değil; her dönemin estetik anlayışına uyum sağlayabilen güçlü ve kalıcı bir stil ifadesidir.</em></p>
</blockquote>

<h2>Sade Gelinlik Tasarımında Özel Dokunuş</h2>

<p><a href="/blog/trend-gelinlik-modelleri/">Sade gelinlik modellerindeki minimalist yaklaşım</a>, <a href="/blog/balik-gelinlik-nedir/">balık kesim ya da prenses formları</a> ile birleştirebilir. <a href="/blog/yeni-sezon-gelinlik-modelleri/">Yeni sezonun sade tasarımlarını</a> keşfetmek ve size özel bir minimal gelinlik oluşturmak için <a href="/contacts/">bizimle iletişime geçebilirsiniz.</a></p>

<h2>Atölye Deneyimi</h2>

<p><a href="/services/">Naba Studio by Semma'nın couture gelinlik hizmetleri</a> ile sade ama etkileyici bir gelinlik tasarlayabilirsiniz. <a href="/pricing/">Paketlerimizi</a> inceleyerek ve <a href="/contacts/">randevu oluşturarak</a> kendi sade tasarımınıza başlayabilirsiniz.</p>''',
            published_at=date.today(),
            category='Moda Trendleri',
            hero_image='https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=80',
            tags='sade gelinlik, minimal, tasarım, zamansız, couture, elegans',
            meta_title='Sade Gelinlik Modelleri | Zamansız ve Minimal Tasarımlar – Naba Studio by Semma',
            meta_description='Sade gelinlik modelleri ile kusursuz kalıp, kaliteli kumaş ve zamansız zarafet bir arada. Naba Studio by Semma özel dikim gelinlik koleksiyonunu Kuzey Makedonya\'da keşfedin.',
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created blog post: {post.title}'))
