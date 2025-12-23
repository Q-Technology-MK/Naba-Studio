from django.core.management.base import BaseCommand
from core.models import BlogPost
from datetime import date


class Command(BaseCommand):
    help = 'Load fourth blog post about trending bridal designs'

    def handle(self, *args, **options):
        # Check if post already exists
        if BlogPost.objects.filter(slug='trend-gelinlik-modelleri').exists():
            self.stdout.write(self.style.WARNING('Blog post already exists!'))
            return

        post = BlogPost.objects.create(
            title='Trend Gelinlik Modelleri | Naba Studio by Semma',
            slug='trend-gelinlik-modelleri',
            excerpt='Gelinlik modası, her sezon yeniden yazılan sofistike bir hikâyedir. Naba Studio by Semma olarak biz, trendleri takip etmekten ziyade onları zarafetle yorumlayan bir tasarım anlayışını benimsiyoruz.',
            body='''<p>Gelinlik modası, her sezon yeniden yazılan sofistike bir hikâyedir. Naba Studio by Semma olarak biz, trendleri takip etmekten ziyade onları zarafetle yorumlayan bir tasarım anlayışını benimsiyoruz. Son yıllarda öne çıkan trend gelinlik modelleri; abartıdan uzak, güçlü silüetlere sahip ve zamansız bir estetik sunan tasarımlarla tanımlanıyor.</p>

<p>Minimal çizgilerle şekillenen A kesim ve düz kesim gelinlikler, her vücut tipine uyum sağlaması ve modern duruşuyla çağdaş gelinlerin ilk tercihi haline geliyor. Belden oturan özel korsajlar, yumuşak drapeler ve akışkan tül eteklerle birleştiğinde sade ama son derece etkileyici bir görünüm ortaya çıkıyor. <a href="/blog/balik-gelinlik-nedir/">Bunun yanında prenses kesim gelinlikler ve balık formundaki iddialı silüetler</a>, trendler arasında yerini güçlü şekilde koruyor.</p>

<h2>2025 Gelinlik Trendlerinde Öne Çıkan Detaylar</h2>

<p>2025 sezonunda gelinlik trendleri, detay odaklı bir lüks anlayışıyla şekilleniyor. Transparan korsajlar, üç boyutlu çiçek aplikeleri, el işçiliği dantel detaylar ve zarif dokunuşlar, gelinliğin karakterini belirleyen unsurlar arasında yer alıyor. Kumaş seçiminde ise mat saten, ince tül, ipek şifon ve doğal dokulu mikado kumaşlar ön plana çıkıyor.</p>

<p><a href="/blog/yeni-sezon-gelinlik-modelleri/">Naba Studio by Semma koleksiyonlarında trendler, gelinin vücut yapısı ve düğün konseptiyle bütünleşecek şekilde ele alınıyor.</a> Kuzey Makedonya'da gerçekleşen salon düğünlerinden açık hava organizasyonlarına kadar her mekâna uygun, dengeli ve sofistike tasarımlar sunuluyor.</p>

<h2>Trend Gelinlik Seçerken Naba Studio Dokunuşu</h2>

<p>Bir gelinliğin trend olması kadar, gelinin üzerinde kusursuz hissettirmesi de önemlidir. <a href="/blog/couture-gelinlik-modelleri/">Naba Studio by Semma'da her tasarım, özel dikim yaklaşımıyla kişiye özel hale getirilir.</a> Mevsim, düğün mekânı, vücut oranları ve kişisel stil analiz edilerek en doğru silüet belirlenir.</p>

<blockquote>
<p><em>Trendleri taşıyan ama zamana meydan okuyan bir gelinlik arıyorsanız, Naba Studio by Semma'nın couture bakış açısıyla tanışmanın tam zamanı.</em></p>
</blockquote>

<h2>Trend Gelinliğinizi Tasarlayalım</h2>

<p><a href="/services/">Naba Studio by Semma'nın couture gelinlik hizmetleri</a> hakkında daha fazla bilgi almak ve <a href="/contacts/">atölye randevusu oluşturmak</a> için bizimle iletişime geçebilirsiniz. <a href="/pricing/">Paketlerimizi</a> inceleyerek sizi en iyi şekilde hizmet etmek için hangi seçeneklerin uygun olduğunu öğrenebilirsiniz.</p>''',
            published_at=date.today(),
            category='Moda Trendleri',
            hero_image='https://images.unsplash.com/photo-1566281684033-5461c3920994?auto=format&fit=crop&w=1200&q=80',
            tags='trend, gelinlik, moda, 2025, tasarım, koleksiyon, couture',
            meta_title='Trend Gelinlik Modelleri 2025 | Naba Studio by Semma',
            meta_description='2025 trend gelinlik modelleri keşfedin. Naba Studio by Semma couture tasarımlarıyla zamansız ve sofistike gelinlik modelleri. Kuzey Makedonya\'da özel dikim.',
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created blog post: {post.title}'))
