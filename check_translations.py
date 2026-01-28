#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wedding_site.settings')
django.setup()

from core.templatetags.multilang import STATIC_TEXTS

print("\n" + "="*80)
print("✓ EKLENEN YENİ METINLER".center(80))
print("="*80 + "\n")

new_keys = ['studio_prestige', 'experience_message', 'quality_commitment', 'custom_design_msg']

for key in new_keys:
    if key in STATIC_TEXTS:
        print(f"📌 Key: {key}")
        print(f"   Makedonca: {STATIC_TEXTS[key]['mk']}")
        print(f"   Türkçe: {STATIC_TEXTS[key]['tr']}")
        print(f"   Arnavutça: {STATIC_TEXTS[key]['sq']}")
        print()

print("="*80)
print("✓ MEVCUT home_hero_subtitle".center(80))
print("="*80 + "\n")

if 'home_hero_subtitle' in STATIC_TEXTS:
    print(f"Makedonca: {STATIC_TEXTS['home_hero_subtitle']['mk']}")
    print(f"\nTürkçe: {STATIC_TEXTS['home_hero_subtitle']['tr']}")
    print(f"\nArnavutça: {STATIC_TEXTS['home_hero_subtitle']['sq']}")

print("\n" + "="*80)
