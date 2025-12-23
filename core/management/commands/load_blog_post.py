from django.core.management.base import BaseCommand
from core.models import BlogPost
from datetime import date


class Command(BaseCommand):
    help = 'Load initial blog posts'

    def handle(self, *args, **options):
        # Check if post already exists
        if BlogPost.objects.filter(slug='couture-gelinlik-modelleri').exists():
            self.stdout.write(self.style.WARNING('Blog post already exists!'))
            return

        post = BlogPost.objects.create(
            title='Özel Dikim Couture Gelinlik Modelleri Hakkında',
            slug='couture-gelinlik-modelleri',
            excerpt='Couture gelinlik modellerinin en büyük farkı, tasarım sürecinin merkezinde sizin olmanızdır. Naba Studio by Semma\'da, sıfırdan, sizin ölçülerinize, vücut oranlarınıza ve stilinize göre inşa edilen benzersiz gelinlikler yaratılır.',
            body='''<h2>Couture Gelinlik Nedir?</h2>
<p>Gelinlik seçimi, bir kadının hayatındaki en özel ve en kişisel moda yolculuklarından biridir. Bu yolculukta binlerce hazır model arasından sıyrılan, yalnızca size özel tasarlanan ve her dikişinde bir hikâye barındıran gelinlikler ise Couture dünyasına aittir.</p>

<p>Fransızca Haute Couture kavramından gelen couture, "yüksek terzilik" anlamını taşır. Naba Studio by Semma'da tasarlanan couture gelinlik modelleri, seri üretimin sınırlarını aşarak; gelin adayının hayallerini, vücut yapısını ve ruhunu yansıtan benzersiz bir sanat eserine dönüşür.</p>

<h2>Couture Gelinlik Modelleri ile Hazır Gelinlik Arasındaki Fark</h2>
<p>Couture gelinlik modellerinin en büyük farkı, tasarım sürecinin merkezinde sizin olmanızdır.</p>

<p>Hazır gelinliklerde beden uyarlaması yalnızca bir tadilat sürecidir. Oysa couture gelinlikte;</p>

<ul>
<li>Gelinlik sıfırdan,</li>
<li>Sizin ölçülerinize,</li>
<li>Sizin vücut oranlarınıza,</li>
<li>Sizin stilinize göre inşa edilir.</li>
</ul>

<p>Kumaş türünden dantel yerleşimine, işleme yoğunluğundan inci boyutuna kadar tüm detaylar sizin onayınızla belirlenir.</p>

<p>Naba Studio by Semma, Kuzey Makedonya'da sunduğu özel dikim deneyimiyle yalnızca estetik değil; konfor, hareket özgürlüğü ve kusursuz kalıp anlayışını da ön planda tutar. İç korsaj yapısı, kumaşın akışı ve görünmez dikiş teknikleri couture sanatının gizli kahramanlarıdır.</p>

<h2>Naba Studio by Semma'da Özel Dikim Süreci</h2>
<p>Bir couture gelinliğin ortaya çıkışı sabır, ustalık ve tutku gerektirir. Atölyemizde bu süreç aşağıdaki adımlarla ilerler:</p>

<h3>1. Tasarım &amp; Stil Danışmanlığı</h3>
<p>Gelin adayımızın tarzı, düğün konsepti ve hayalları detaylı şekilde dinlenir. Vücut tipine en uygun silüet birlikte belirlenir:</p>

<ul>
<li><strong>Prenses</strong> – Volümlü etek ile rüya gibi bir görünüm</li>
<li><strong>Balık</strong> – Diz altına kadar dar, sonra çan şeklinde açılan kesim</li>
<li><strong>A Kesim</strong> – Dar göğüs, rahat akan etek</li>
<li><strong>Düz Kesim</strong> – Modern ve minimalist yapı</li>
</ul>

<h3>2. Kumaş ve Detay Seçimi</h3>
<p>Özel ithal Fransız dantelleri, ipek satenler, tüller ve el işçiliği taşlar arasından seçim yapılır. Minimal bir mimari yapı mı, yoksa yoğun işlemeli couture detaylar mı istediğinize bu aşamada karar verilir.</p>

<h3>3. Prova Süreci</h3>
<p>Genellikle 3 ana prova gerçekleştirilir. Her prova, gelinliğin vücudunuzla bütünleşmesini sağlar. Usta terzilerimiz her dikişte couture hassasiyetini uygular.</p>

<h2>Couture Gelinliklerde Detayların Önemi</h2>
<p>Couture gelinlik modellerinin ruhu, detaylarda gizlidir.</p>

<ul>
<li>El işçiliği aplikler</li>
<li>Özel tasarım dantel kesimleri</li>
<li>Elle işlenen taş ve inci detayları</li>
<li>Kişiye özel pelerinler ve kuyruk tasarımları</li>
</ul>

<p>Aile yadigârı bir dantelin modernize edilerek gelinliğe eklenmesi ya da omuzlardan süzülen özel bir pelerin gibi hayaller yalnızca özel dikim couture ile mümkündür.</p>

<h2>Kuzey Makedonya'da Couture Gelinlik Deneyimi</h2>
<p>Naba Studio by Semma, Kuzey Makedonya'da couture gelinlik tasarımı denince akla gelen özel adreslerden biridir. Her gelinlik, yalnızca bir kıyafet değil; gelinin hikâyesini anlatan zamansız bir tasarım olarak ele alınır.</p>

<blockquote>
<p><em>Mükemmel gelinliği bulmak zordur, ama onu yaratmak paha biçilemez bir deneyimdir.</em></p>
</blockquote>

<h2>Atelier Ziyareti &amp; Randevu</h2>
<p>Eğer düğün gününüzde üzerinizde taşıdığınız her detayın bir anlamı olmasını istiyorsanız, doğru yerdesiniz.</p>

<p><strong>📍 Naba Studio by Semma – Kuzey Makedonya</strong></p>
<ul>
<li>✨ Kişiye özel couture tasarımlar</li>
<li>✨ El işçiliği &amp; yüksek terzilik</li>
<li>✨ Sınırlı sayıda özel üretim</li>
</ul>

<p>👉 Atölye randevusu almak ve couture dünyamızı yakından keşfetmek için <a href="/contacts/">bizimle iletişime geçebilirsiniz</a>. <a href="/services/">Tüm hizmetlerimizi inceleyebilir</a> ve <a href="/about/">atelier hakkında daha fazla bilgi</a> edebilirsiniz.</p>''',
            published_at=date.today(),
            category='Moda Trendleri',
            hero_image='https://images.unsplash.com/photo-1595777707802-52b966efb60f?auto=format&fit=crop&w=1200&q=80',
            tags='couture, gelinlik, özel dikim, tasarım, moda',
            meta_title='Özel Dikim Couture Gelinlik Modelleri | Naba Studio by Semma',
            meta_description='Kuzey Makedonya\'da sıfırdan tasarlanan özel dikim couture gelinlikleri. Kişiye özel ölçü ve stilize hizmeti.',
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created blog post: {post.title}'))
