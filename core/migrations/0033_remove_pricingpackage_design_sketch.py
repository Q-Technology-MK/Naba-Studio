from django.db import migrations


def remove_design_sketch_column(apps, schema_editor):
    """Remove design_sketch column from PricingPackage table if it exists"""
    if schema_editor.connection.vendor == 'sqlite':
        # For SQLite, we need to check if column exists first
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("PRAGMA table_info(core_pricingpackage);")
            columns = [row[1] for row in cursor.fetchall()]
            if 'design_sketch' in columns:
                # SQLite doesn't support DROP COLUMN directly in older versions
                # We need to recreate the table without the column
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS core_pricingpackage_new (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(100) NOT NULL,
                        name_tr VARCHAR(100) NOT NULL,
                        name_sq VARCHAR(100) NOT NULL,
                        price VARCHAR(50) NOT NULL,
                        period VARCHAR(50) NOT NULL,
                        period_tr VARCHAR(50) NOT NULL,
                        period_sq VARCHAR(50) NOT NULL,
                        features TEXT NOT NULL,
                        features_tr TEXT NOT NULL,
                        features_sq TEXT NOT NULL,
                        "order" INTEGER UNSIGNED NOT NULL,
                        is_featured BOOL NOT NULL
                    );
                """)
                cursor.execute("""
                    INSERT INTO core_pricingpackage_new (id, name, name_tr, name_sq, price, period, period_tr, period_sq, features, features_tr, features_sq, "order", is_featured)
                    SELECT id, name, COALESCE(name_tr, ''), COALESCE(name_sq, ''), price, period, COALESCE(period_tr, ''), COALESCE(period_sq, ''), features, COALESCE(features_tr, ''), COALESCE(features_sq, ''), "order", is_featured
                    FROM core_pricingpackage;
                """)
                cursor.execute("DROP TABLE core_pricingpackage;")
                cursor.execute("ALTER TABLE core_pricingpackage_new RENAME TO core_pricingpackage;")


def reverse_migration(apps, schema_editor):
    """No reverse needed - column was orphaned"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_pagemedia_section'),
    ]

    operations = [
        migrations.RunPython(remove_design_sketch_column, reverse_migration),
    ]
