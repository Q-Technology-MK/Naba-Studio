from django.core.management.base import BaseCommand
from core.models import FAQItem


class Command(BaseCommand):
    help = "Fix FAQ item categories to use correct key format"

    def handle(self, *args, **options):
        # Map old category names to new key format
        category_mapping = {
            # Old Macedonian display names -> new keys
            'Закажување термини и Проби': 'booking_trials',
            'Резервации и проби': 'booking_trials',
            'Booking & Trials': 'booking_trials',
            
            'Дизајн и прилагодување': 'design_customization',
            'Design & Customization': 'design_customization',
            
            'Рокови и цени': 'timeline_pricing',
            'Timeline & Pricing': 'timeline_pricing',
            
            'Достава и нега': 'delivery_care',
            'Delivery & Care': 'delivery_care',
            
            'Производи и материјали': 'products_materials',
            'Products & Materials': 'products_materials',
            
            'Контакт и информации': 'contact_info',
            'Contact & Information': 'contact_info',
        }
        
        updated_count = 0
        for faq in FAQItem.objects.all():
            old_category = faq.category
            if old_category in category_mapping:
                faq.category = category_mapping[old_category]
                faq.save()
                updated_count += 1
                self.stdout.write(f"Updated: '{old_category}' -> '{faq.category}'")
        
        self.stdout.write(
            self.style.SUCCESS(f"Successfully updated {updated_count} FAQ categories")
        )
