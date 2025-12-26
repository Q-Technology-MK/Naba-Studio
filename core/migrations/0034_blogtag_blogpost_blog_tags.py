from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_remove_pricingpackage_design_sketch'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Етикета (Македонски)')),
                ('name_tr', models.CharField(blank=True, max_length=50, verbose_name='Etiket (Türkçe)')),
                ('name_sq', models.CharField(blank=True, max_length=50, verbose_name='Etiketa (Shqip)')),
                ('slug', models.SlugField(help_text='URL için benzersiz tanımlayıcı', unique=True)),
            ],
            options={
                'verbose_name': 'Blog Etiketi',
                'verbose_name_plural': 'Blog Etiketleri',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='blog_tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='core.blogtag', verbose_name='Etiketler'),
        ),
    ]
