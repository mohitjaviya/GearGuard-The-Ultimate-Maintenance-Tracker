import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gearguard.settings')
django.setup()

from src.equipment.models import Equipment, EquipmentCategory

# Map equipment types to categories
type_to_category = {
    'mechanical': 'Mechanical',
    'electrical': 'Electrical',
    'hydraulic': 'Hydraulic',
    'pneumatic': 'Pneumatic',
    'electronic': 'Electronic',
}

# Assign categories to equipment
equipment = Equipment.objects.all()
for eq in equipment:
    category_name = type_to_category.get(eq.equipment_type)
    if category_name:
        try:
            category = EquipmentCategory.objects.get(name=category_name)
            eq.category = category
            eq.save()
            print(f'✓ {eq.name} → {category.name}')
        except EquipmentCategory.DoesNotExist:
            print(f'✗ Category not found: {category_name}')

print(f'\nAssigned categories to {equipment.count()} equipment')
