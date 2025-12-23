from django.core.management.base import BaseCommand
from core.models import BlogPost
from datetime import date


class Command(BaseCommand):
    help = 'Load sixth blog post about bridal dress cleaning and storage'

    def handle(self, *args, **options):
        # Check if post already exists
        if BlogPost.objects.filter(slug='gelinlik-temizligi-saklama-yontemleri').exists():
            self.stdout.write(self.style.WARNING('Blog post already exists!'))
            return

        post = BlogPost.objects.create(
            title='Gelinlik Nasıl Temizlenir, Nasıl Saklanır?',
            slug='gelinlik-temizligi-saklama-yontemleri',
            excerpt='Bir gelinlik, yalnızca bir kıyafet değil; bir anı, bir hikâye ve çoğu zaman nesiller boyu saklanan bir mirastır. Gelinlik temizliği ve saklama yöntemleri hakkında profesyonel rehberimizi keşfedin.',
            body='''<p>Bir gelinlik, yalnızca bir kıyafet değil; bir anı, bir hikâye ve çoğu zaman nesiller boyu saklanan bir mirastır. Özel dikim veya couture bir gelinlik, düğün gününün ardından doğru şekilde temizlenmez ve saklanmazsa; zamanla sararma, kumaş yorgunluğu ve dantel deformasyonu gibi geri dönüşü olmayan hasarlara uğrayabilir.</p>

<p><a href="/blog/couture-gelinlik-modelleri/">Naba Studio by Semma olarak Kuzey Makedonya'daki atölyemizde</a>, her gelinliğin yalnızca tasarım sürecinde değil, düğün sonrasında da ilk günkü zarafetini korumasını önemsiyoruz. Bu yazıda, gelinlik temizliği nasıl yapılır ve gelinlik nasıl saklanır sorularına profesyonel rehberlik sunuyoruz.</p>

<h2>Düğün Sonrası Temizlik Neden Hayati Önem Taşır?</h2>

<p>Düğün günü boyunca gelinlik;</p>

<ul>
<li>makyaj ve parfüm kalıntılarına</li>
<li>ter ve vücut yağına</li>
<li>içecek, yiyecek ve toprak lekelerine</li>
<li>açık alan düğünlerinde çim ve toz temasına</li>
</ul>

<p>maruz kalır. Bu kalıntılar kumaş üzerinde bekledikçe oksitlenir, sararmaya ve lif yapısının zayıflamasına neden olur.</p>

<blockquote>
<p><strong>Profesyonel önerimiz:</strong> Gelinliğinizi düğünden en geç 7 gün içinde temizletin. Erken müdahale, couture kumaşların ömrünü yıllarca uzatır.</p>
</blockquote>

<h2>Gelinlik Temizliği Nasıl Yapılır?</h2>

<h3>1. Profesyonel Gelinlik Temizliği (Önerilen)</h3>

<p>İşlemeli, taşlı, Fransız dantelli veya ipek içerikli gelinliklerde mutlaka profesyonel temizlik tercih edilmelidir.</p>

<p><a href="/services/">Naba Studio by Semma'da</a>:</p>

<ul>
<li>Kumaş türüne özel leke analizleri yapılır</li>
<li>El işçiliği detaylar korunarak temizlik uygulanır</li>
<li>Gelinlik formu ve korsaj yapısı bozulmaz</li>
</ul>

<p>Bu yöntem, özellikle <a href="/blog/couture-gelinlik-modelleri/">özel dikim ve couture gelinlikleri</a> için en güvenli seçenektir.</p>

<h3>2. Evde Temizlik (Sınırlı Kullanım)</h3>

<p>Evde temizlik yalnızca sade, taşsız ve sentetik içermeyen gelinlikleri için uygundur.</p>

<p>Dikkat edilmesi gerekenler:</p>

<ul>
<li>Ağartıcı içermeyen nazik ürünler (bebek şampuanı vb.)</li>
<li>Sadece elde ve bastırmadan temizlik</li>
<li>Makine yıkaması kesinlikle önerilmez</li>
<li>Kurulama gölgede, serin ortamda yapılmalıdır</li>
</ul>

<p>İpek, şifon, tül ve dantel gelinliklerde evde temizlik önerilmez.</p>

<h2>Gelinlik Saklama Yöntemleri</h2>

<p>Temizlik kadar önemli olan bir diğer konu da doğru saklama koşullarıdır.</p>

<h3>1. Kutu ile Saklama (En Güvenli Yöntem)</h3>

<ul>
<li>Asitsiz, nefes alabilen özel kutular kullanılmalı</li>
<li>Naylon poşet yerine pamuklu kılıf tercih edilmeli</li>
<li>Katlama aralarına asitsiz kâğıt yerleştirilmeli</li>
</ul>

<h3>2. Askıda Saklama</h3>

<ul>
<li>Geniş ve destekli askılar kullanılmalı</li>
<li>Direkt güneş ışığı ve nemden uzak tutulmalı</li>
</ul>

<h3>3. Vakumlu Saklama</h3>

<ul>
<li>Sadece kısa süreli kullanım için uygundur</li>
<li>Uzun vadede kumaşın nefes alması engellenir</li>
</ul>

<h2>Saklama Öncesi Altın Kurallar</h2>

<ul>
<li>Gelinliğin tamamen kuru olduğundan emin olun</li>
<li>Nemli ve sıcak ortamlardan kaçının</li>
<li>Yılda 1–2 kez gelinliği havalandırın</li>
<li>Üzerine ağır eşyalar koymayın</li>
</ul>

<h2>Naba Studio by Semma'dan Özel Tavsiyeler</h2>

<p>Naba Studio by Semma olarak yalnızca gelinlik tasarlamıyor; gelinliğinizin zamansız bir miras olmasını sağlıyoruz.</p>

<ul>
<li>Gelinlikler özel koruma kılıfı ile teslim edilir</li>
<li>Saklama ve bakım rehberi kişiye özel anlatılır</li>
<li><a href="/blog/couture-gelinlik-modelleri/">Couture gelinlikleri</a> için uzun vadeli bakım önerileri sunulur</li>
</ul>

<p><a href="/contacts/">Gelinliğinizin bakımı hakkında sorularınız için bizimle iletişime geçebilirsiniz.</a> <a href="/services/">Naba Studio by Semma'nın couture hizmetleri</a> ve <a href="/blog/sade-gelinlik-modelleri/">koleksiyonlarımızı</a> keşfetmeyi unutmayın.</p>''',
            published_at=date.today(),
            category='Bakım & Tavsiyeleri',
            hero_image='https://images.unsplash.com/photo-1487180144351-b8472da7d491?auto=format&fit=crop&w=1200&q=80',
            tags='bakım, temizlik, saklama, gelinlik, couture, rehber',
            meta_title='Gelinlik Temizliği ve Saklama Yöntemleri | Naba Studio by Semma',
            meta_description='Gelinlik nasıl temizlenir ve nasıl saklanır? Couture gelinlikleri için profesyonel temizlik ve saklama rehberi. Naba Studio by Semma – Kuzey Makedonya.',
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created blog post: {post.title}'))
