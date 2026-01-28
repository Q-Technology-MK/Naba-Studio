"""
Management command to update repetitive translations.
Updates the multilang.py file with proper translations in Macedonian, Turkish, and Albanian.
"""

from django.core.management.base import BaseCommand
import os
import re

class Command(BaseCommand):
    help = 'Update repetitive translations in the multilingual template tags'

    def handle(self, *args, **options):
        # Define the translations to update
        translations = {
            'home_hero_subtitle': {
                'mk': 'Најпрестижното couture атеље за венчаници во Северна Македонија. Секоја венчаница има своја приказна. Дали си подготвена да ја напишеш твојата?',
                'tr': "Kuzey Makedonya'nın en prestijli couture gelinlik tasarım atölyesi. Her gelinliğin bir hikâyesi vardır. Seninkini yazmaya hazır mısın?",
                'sq': 'Atelieja më prestigjioze e fustaneve të nusërisë couture në Maqedoninë e Veriut. Çdo fustan nusërie ka një histori. A jeni gati të shkruani tuajën?'
            },
            'about_studio_mission': {
                'mk': 'Нашата мисија е да創 венчаници кои ја одразуваат личноста и елеганција на секоја невеста.',
                'tr': 'Misyonumuz, her gelin\'in kişiliğini ve zarafetini yansıtan gelinlikler yaratmaktır.',
                'sq': 'Misioni ynë është të krijojmë fustan nusërie që pasqyrojnë personalitetin dhe elegancën e çdo nuse.'
            },
            'services_header': {
                'mk': 'Комплетни услуги за вашиот специјален ден',
                'tr': 'Özel gününüz için kapsamlı hizmetler',
                'sq': 'Shërbime të plota për ditën tuaj të posaçme'
            },
            'contact_cta': {
                'mk': 'Имаш прашање? Контактирај ни денес!',
                'tr': 'Bir sorunuz var mı? Bugün bize ulaşın!',
                'sq': 'A keni një pyetje? Kontaktoni ne sot!'
            }
        }

        # Path to multilang.py
        multilang_path = os.path.join(
            os.path.dirname(__file__),
            '../../templatetags/multilang.py'
        )

        if not os.path.exists(multilang_path):
            self.stdout.write(
                self.style.ERROR(f'File not found: {multilang_path}')
            )
            return

        # Read the file
        with open(multilang_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Display information about what will be updated
        self.stdout.write(self.style.SUCCESS('\n=== Güncellenecek Metinler ===\n'))
        
        for key, langs in translations.items():
            self.stdout.write(f"\n{key}:")
            self.stdout.write(f"  Macedonian: {langs['mk']}")
            self.stdout.write(f"  Turkish: {langs['tr']}")
            self.stdout.write(f"  Albanian: {langs['sq']}")

        # Update translations in the file
        for key, langs in translations.items():
            # Create the translation dictionary string
            translation_str = f"""    '{key}': {{'mk': '{langs['mk']}', 'tr': "{langs['tr']}", 'sq': '{langs['sq']}'}}"""
            
            # Find and replace or add new translation
            pattern = rf"'{key}':\s*\{{'mk':\s*'[^']*',\s*'tr':\s*\"[^\"]*\",\s*'sq':\s*'[^']*'\}}"
            
            if re.search(pattern, content):
                # Replace existing translation
                content = re.sub(pattern, translation_str, content)
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Updated {key}')
                )
            else:
                # Add new translation before the closing of STATIC_TEXTS
                insert_position = content.rfind('}')
                if insert_position > 0:
                    # Find the last translation entry
                    last_entry_pattern = r"('[a-zA-Z_]+': \{[^}]+\}),?\n"
                    last_match = None
                    for match in re.finditer(last_entry_pattern, content):
                        last_match = match
                    
                    if last_match:
                        insert_position = last_match.end()
                        content = content[:insert_position] + f",\n{translation_str}" + content[insert_position:]
                        self.stdout.write(
                            self.style.SUCCESS(f'✓ Added {key}')
                        )

        # Write back to file
        with open(multilang_path, 'w', encoding='utf-8') as f:
            f.write(content)

        self.stdout.write(
            self.style.SUCCESS('\n✓ Tüm çeviriler başarıyla güncellendi!')
        )
        self.stdout.write(
            self.style.WARNING('\nNOT: Değişikliklerin etkili olması için sunucuyu yeniden başlatın.')
        )
