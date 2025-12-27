from src.equipment.models import Equipment, WorkCenter
import random

wcs = list(WorkCenter.objects.all())
eq_list = Equipment.objects.all()

for eq in eq_list:
    eq.work_center = random.choice(wcs)
    eq.save()

print(f'Assigned {eq_list.count()} equipment to work centers')
for wc in wcs:
    print(f'{wc.code}: {wc.equipment.count()} machines')
