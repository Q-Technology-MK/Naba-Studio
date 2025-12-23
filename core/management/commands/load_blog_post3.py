from django.core.management.base import BaseCommand
from core.models import BlogPost
from datetime import date


class Command(BaseCommand):
    help = 'Load third blog post about mermaid bridal dresses'

    def handle(self, *args, **options):
        # Check if post already exists
        if BlogPost.objects.filter(slug='balik-gelinlik-nedir').exists():
            self.stdout.write(self.style.WARNING('Blog post already exists!'))
            return

        post = BlogPost.objects.create(
            title='Balık Gelinlik Nedir? | Couture Balık Gelinlik Modelleri',
            slug='balik-gelinlik-nedir',
            excerpt='Balık gelinlik, gelinlik modasının en feminen, en iddialı ve en sofistike silüetlerinden biridir. Vücut hatlarını kusursuz biçimde saran bu form, güçlü bir duruşun, zarafetin ve modern kadın estetiğinin sembolüdür.',
            body='''<p>Balık gelinlik, gelinlik modasının en feminen, en iddialı ve en sofistike silüetlerinden biridir. Vücut hatlarını kusursuz biçimde saran bu form, sadece bir gelinlik modeli değil; güçlü bir duruşun, zarafetin ve modern kadın estetiğinin sembolüdür.</p>

<p>Naba Studio by Semma'da balık gelinlikler, bedeni saran bir kalıp olmanın ötesine geçerek couture terziliğin heykelsi bir yorumuna dönüşür.</p>

<h2>Balık Gelinlik Nedir?</h2>

<p>Balık gelinlik; üst bedenden kalça hizasına kadar vücuda oturan, diz veya diz altından itibaren dramatik biçimde genişleyen etek yapısıyla tanımlanır. Bu silüet, bele odaklanır, vücut oranlarını dengeler ve gelinin duruşunu çarpıcı bir zarafetle ön plana çıkarır.</p>

<p><a href="/blog/couture-gelinlik-modelleri/">Naba Studio by Semma couture balık gelinliklerinde;</a></p>

<ul>
<li>El işçiliği dantel aplikler</li>
<li>Mimari korsaj teknikleri</li>
<li>İpek saten, mikado ve özel dokuma Fransız dantelleri</li>
</ul>

<p>bir araya gelerek adeta kumaştan bir heykel yaratır.</p>

<h2>Balık Gelinlik Ne Anlatır?</h2>

<p>Bu silüet, özgüvenli ve stilini net biçimde ortaya koyan gelinlerin tercihidir. Masalsı kabarıklıktan ziyade sofistike bir zarafet sunar. Derin sırt dekolteleri, straplez veya ince askılı yapılarla birleştiğinde balık gelinlik, modern feminenliğin en güçlü temsilcilerinden biri haline gelir.</p>

<p><a href="/blog/yeni-sezon-gelinlik-modelleri/">Naba Studio by Semma balık gelinlikleri;</a></p>

<ul>
<li><strong>Zamansız lüks</strong></li>
<li><strong>Sessiz ihtişam</strong></li>
<li><strong>Güçlü ama rafine bir stil</strong></li>
</ul>

<p>arayışındaki gelinlere hitap eder.</p>

<h2>Balık Gelinliğin Moda Yolculuğu</h2>

<p>Balık formu, ilk kez 1930'lu yıllarda Hollywood'un altın çağında kırmızı halı silüetleriyle öne çıktı. Gelinlik dünyasında ise 1990'ların sonu ve 2000'lerin başında couture moda evlerinin koleksiyonlarıyla ikonikleşti.</p>

<p>Bugün balık gelinlik, klasik prenses kesime modern bir alternatif olarak zamansızlığını korumaya devam ediyor. <a href="/blog/couture-gelinlik-modelleri/">Naba Studio by Semma'da bu silüet, global couture anlayışı ile Kuzey Makedonya'daki özel dikim gelinlik geleneğini birleştirerek yeniden yorumlanıyor.</a></p>

<h2>Size Özel Balık Gelinlik Tasarımı</h2>

<p><a href="/services/">Naba Studio by Semma'nın couture terzilik hizmetleri</a> ile balık gelinlik silüetini tam da sizin vücut yapınıza ve tarzınıza uyacak şekilde tasarlayabilirsiniz. <a href="/contacts/">Randevu oluşturun</a> ve kendi couture hikâyenizi yazın.</p>''',
            published_at=date.today(),
            category='Moda Trendleri',
            hero_image='https://images.unsplash.com/photo-1594938298603-c8148c4dae35?auto=format&fit=crop&w=1200&q=80',
            tags='balık gelinlik, couture, silüet, moda, lüks gelinlik, tasarım',
            meta_title='Balık Gelinlik Nedir? | Couture Balık Gelinlik Modelleri – Naba Studio by Semma',
            meta_description='Balık gelinlik nedir, kimler için uygundur? Naba Studio by Semma\'nın couture balık gelinlik modelleriyle vücut hatlarını kusursuz vurgulayan lüks silüetleri keşfedin. Kuzey Makedonya\'da özel dikim gelinlik deneyimi.',
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created blog post: {post.title}'))
