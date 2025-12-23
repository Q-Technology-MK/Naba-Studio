from django.core.management.base import BaseCommand
from core.models import BlogPost
from datetime import date


class Command(BaseCommand):
    help = 'Load second blog post'

    def handle(self, *args, **options):
        # Check if post already exists
        if BlogPost.objects.filter(slug='yeni-sezon-gelinlik-modelleri').exists():
            self.stdout.write(self.style.WARNING('Blog post already exists!'))
            return

        post = BlogPost.objects.create(
            title='Yeni Sezon Gelinlik Modelleri | Couture Zarafetin Yeni Yorumu',
            slug='yeni-sezon-gelinlik-modelleri',
            excerpt='Her gelin adayı, hayatının en özel gününde yalnızca bir gelinlik değil; kendini, ruhunu ve stilini yansıtan bir couture deneyimi taşımayı hayal eder. Naba Studio by Semma, bu hayali gerçeğe dönüştürür.',
            body='''<p>Naba Studio by Semma, bu hayali Kuzey Makedonya'daki atölyesinde, yüksek terzilik geleneği ile çağdaş tasarım anlayışını bir araya getirerek gerçeğe dönüştürür.</p>

<p>Yeni sezon gelinlik modellerimiz; zarafeti, cesareti ve zamansız şıklığı tek bir silüette buluşturur. Her tasarım, yalnızca bir elbise değil; detaylarında duygu, formunda güç barındıran bir imza parça olarak kurgulanır.</p>

<h2>Gelinlik Modelleri – Couture Ruhu ile Tasarlandı</h2>

<p>Yeni sezonda couture dünyası daha net silüetler, sofistike dokular ve kişisel dokunuşlara açık tasarımlar etrafında şekilleniyor. <a href="/blog/couture-gelinlik-modelleri/">Naba Studio by Semma koleksiyonunda</a> öne çıkan gelinlik modelleri iki ana eksende hayat buluyor:</p>

<ul>
<li><strong>İhtişamlı Prenses Gelinlikler</strong> – Vücut hatlarını zarafetle saran</li>
<li><strong>Balık Kesim Gelinlikler</strong> – Dinamik ve zarif kesim</li>
</ul>

<p>Şeffaf korsaj detayları, çıkarılabilir pelerinler (cape), üç boyutlu çiçek aplikleri ve el işçiliği inci nakışlar; koleksiyonun couture DNA'sını oluşturur.</p>

<h2>Gelinliğin Bedenle Uyumu: Couture'un Sırrı</h2>

<p>Askıda güzel görünen bir gelinlik yeterli değildir. Gerçek fark, gelinliğin bedenle kurduğu kusursuz uyumda ortaya çıkar. Bu nedenle Naba Studio by Semma'da her model, <a href="/blog/couture-gelinlik-modelleri/">özel dikim yaklaşımıyla</a> gelinin vücut yapısına, düğün konseptine ve kişisel stiline göre yeniden yorumlanır.</p>

<h2>Gelinlik Seçiminde Naba Studio by Semma Dokunuşu</h2>

<p>Bir balo salonu düğünü için daha hacimli ve dramatik silüetler önerilirken; sahil, kır veya butik düğünlerde daha hafif, akışkan ve modern formlar ön plana çıkarılır.</p>

<p>Tasarım sürecinde yalnızca trendler değil; mekân, ışık, hareket ve konfor gibi detaylar da dikkate alınır.</p>

<blockquote>
<p><em>Amaç, düğün gününüzde yalnızca güzel görünmeniz değil; kendinizi özgüvenli, rahat ve güçlü hissetmenizdir.</em></p>
</blockquote>

<h2>Atölyeye Davet</h2>

<p>Yeni sezon gelinlik modellerimizi yakından görmek, kumaş dokularını hissetmek ve size <a href="/services/">özel dikim sürecimizi</a> deneyimlemek için Naba Studio by Semma Kuzey Makedonya atölyemize davetlisiniz.</p>

<p><a href="/about/">Naba Studio by Semma hakkında</a> daha fazla bilgi alabilir, <a href="/contacts/">birebir danışmanlık için randevunuzu</a> oluşturabilir veya <a href="/pricing/">paketlerimizi</a> inceleyebilirsiniz.</p>

<p><strong>Her Naba Studio by Semma gelini biriciktir. Siz de kendi couture hikâyenizi yazmaya hazır mısınız?</strong></p>''',
            published_at=date.today(),
            category='Moda Trendleri',
            hero_image='https://images.unsplash.com/photo-1588718435921-edb75dc48a8d?auto=format&fit=crop&w=1200&q=80',
            tags='sezon, gelinlik, couture, moda, tasarım, yeni koleksiyon',
            meta_title='Yeni Sezon Gelinlik Modelleri | Naba Studio by Semma Couture',
            meta_description='Naba Studio by Semma yeni sezon gelinlik modelleri ile couture zarafeti keşfedin. Kuzey Makedonya\'da özel dikim, lüks gelinlik tasarımları.',
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created blog post: {post.title}'))
