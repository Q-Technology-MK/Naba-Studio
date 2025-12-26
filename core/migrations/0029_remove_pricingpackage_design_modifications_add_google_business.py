from django.db import migrations, models


def remove_design_modifications_column(apps, schema_editor):
    """Remove orphan design_modifications column from core_pricingpackage if it exists"""
    from django.db import connection
    with connection.cursor() as cursor:
        # Check if column exists
        cursor.execute("PRAGMA table_info(core_pricingpackage);")
        columns = [row[1] for row in cursor.fetchall()]
        if 'design_modifications' in columns:
            # SQLite requires recreating the table to drop a column
            cursor.execute("ALTER TABLE core_pricingpackage DROP COLUMN design_modifications;")


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_blogpost_tags_alter_blogpost_tags_sq'),
    ]

    operations = [
        # Remove orphan column from database if it exists
        migrations.RunPython(remove_design_modifications_column, migrations.RunPython.noop),
        # Add Google Business URL to SiteSettings
        migrations.AddField(
            model_name='sitesettings',
            name='google_business_url',
            field=models.URLField(blank=True, help_text='Google My Business profil linki'),
        ),
    ]
