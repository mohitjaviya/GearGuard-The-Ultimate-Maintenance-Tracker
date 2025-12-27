import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gearguard.settings')
django.setup()

from src.maintenance_request.models import MaintenanceRequest
from src.equipment.models import WorkCenter
from datetime import datetime, timedelta

# Get all work centers and create sample requests for them
workcenters = list(WorkCenter.objects.all())

for idx, wc in enumerate(workcenters):
    # Create a maintenance request for this work center
    mr = MaintenanceRequest.objects.create(
        title=f'{wc.name} - Preventive Maintenance',
        description=f'Routine preventive maintenance for {wc.name}',
        target_type='work_center',
        work_center=wc,
        requested_by='Maintenance Manager',
        status='pending' if idx % 2 == 0 else 'assigned',
        priority='high' if idx % 3 == 0 else 'medium',
        due_date=datetime.now().date() + timedelta(days=7 + (idx * 3))
    )
    print(f'Created request #{mr.id}: {mr.title}')

print(f'\nTotal work center maintenance requests created: {MaintenanceRequest.objects.filter(target_type="work_center").count()}')
