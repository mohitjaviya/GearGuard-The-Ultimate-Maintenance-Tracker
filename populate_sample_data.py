"""
GearGuard Sample Data
Run this script to populate the database with sample data
Command: python manage.py shell < populate_sample_data.py
"""

from django.contrib.auth.models import User, Group, Permission
from src.equipment.models import Equipment
from src.maintenance_team.models import MaintenanceTeam
from src.maintenance_request.models import MaintenanceRequest
from datetime import datetime, timedelta
from django.utils import timezone

print("🚀 Starting GearGuard sample data population...")

# Create Groups
print("\n📁 Creating User Groups...")
groups_data = [
    {'name': 'Administrators', 'description': 'Full system access'},
    {'name': 'Managers', 'description': 'Manage equipment and requests'},
    {'name': 'Technicians', 'description': 'View and update maintenance requests'},
    {'name': 'Supervisors', 'description': 'Supervise maintenance operations'},
    {'name': 'Viewers', 'description': 'Read-only access'},
]

groups = {}
for group_data in groups_data:
    group, created = Group.objects.get_or_create(name=group_data['name'])
    groups[group_data['name']] = group
    print(f"  {'✓ Created' if created else '✓ Found'}: {group.name}")

# Create Users
print("\n👥 Creating Sample Users...")
users_data = [
    {
        'username': 'john.admin',
        'email': 'john.admin@gearguard.com',
        'password': 'admin123',
        'first_name': 'John',
        'last_name': 'Administrator',
        'is_staff': True,
        'is_superuser': True,
        'groups': ['Administrators']
    },
    {
        'username': 'sarah.manager',
        'email': 'sarah.manager@gearguard.com',
        'password': 'manager123',
        'first_name': 'Sarah',
        'last_name': 'Johnson',
        'is_staff': True,
        'groups': ['Managers']
    },
    {
        'username': 'mike.tech',
        'email': 'mike.tech@gearguard.com',
        'password': 'tech123',
        'first_name': 'Mike',
        'last_name': 'Smith',
        'is_staff': True,
        'groups': ['Technicians']
    },
    {
        'username': 'lisa.supervisor',
        'email': 'lisa.supervisor@gearguard.com',
        'password': 'super123',
        'first_name': 'Lisa',
        'last_name': 'Brown',
        'is_staff': True,
        'groups': ['Supervisors']
    },
    {
        'username': 'david.tech',
        'email': 'david.tech@gearguard.com',
        'password': 'tech123',
        'first_name': 'David',
        'last_name': 'Wilson',
        'is_staff': True,
        'groups': ['Technicians']
    },
]

created_users = {}
for user_data in users_data:
    groups_list = user_data.pop('groups', [])
    password = user_data.pop('password')
    
    user, created = User.objects.get_or_create(
        username=user_data['username'],
        defaults=user_data
    )
    
    if created:
        user.set_password(password)
        user.save()
        print(f"  ✓ Created: {user.username} ({user.get_full_name()}) - Password: {password}")
    else:
        print(f"  ✓ Found: {user.username} ({user.get_full_name()})")
    
    # Add to groups
    for group_name in groups_list:
        if group_name in groups:
            user.groups.add(groups[group_name])
    
    created_users[user.username] = user

# Create Equipment
print("\n🏭 Creating Sample Equipment...")
equipment_data = [
    {
        'name': 'Air Compressor Unit A',
        'description': 'Industrial air compressor for pneumatic tools',
        'equipment_type': 'pneumatic',
        'serial_number': 'CPR-2024-001',
        'location': 'Building A - Floor 2',
        'status': 'active',
        'purchase_date': datetime(2020, 1, 15).date(),
        'manufacturer': 'Atlas Copco',
        'model_number': 'GA-75',
        'last_maintenance': datetime(2025, 11, 20).date(),
        'next_maintenance': datetime(2026, 2, 20).date(),
    },
    {
        'name': 'Hydraulic Press Machine',
        'description': 'Heavy-duty hydraulic press for metal forming',
        'equipment_type': 'hydraulic',
        'serial_number': 'HPM-2024-002',
        'location': 'Building B - Manufacturing Floor',
        'status': 'active',
        'purchase_date': datetime(2019, 6, 10).date(),
        'manufacturer': 'Schuler AG',
        'model_number': 'HPS-500',
        'last_maintenance': datetime(2025, 10, 15).date(),
        'next_maintenance': datetime(2026, 1, 15).date(),
    },
    {
        'name': 'CNC Milling Machine',
        'description': 'Computer numerical control milling machine',
        'equipment_type': 'mechanical',
        'serial_number': 'CNC-2024-003',
        'location': 'Building A - Machining Center',
        'status': 'maintenance',
        'purchase_date': datetime(2021, 3, 25).date(),
        'manufacturer': 'Haas Automation',
        'model_number': 'VF-4SS',
        'last_maintenance': datetime(2025, 12, 1).date(),
    },
    {
        'name': 'Industrial Generator',
        'description': 'Backup power generator - 500kW',
        'equipment_type': 'electrical',
        'serial_number': 'GEN-2024-004',
        'location': 'Building C - Power Room',
        'status': 'active',
        'purchase_date': datetime(2018, 9, 5).date(),
        'manufacturer': 'Caterpillar',
        'model_number': 'C18-500',
        'warranty_expiry': datetime(2028, 9, 5).date(),
        'last_maintenance': datetime(2025, 12, 10).date(),
        'next_maintenance': datetime(2026, 3, 10).date(),
    },
    {
        'name': 'Cooling Tower System',
        'description': 'HVAC cooling tower for facility climate control',
        'equipment_type': 'mechanical',
        'serial_number': 'CLT-2024-005',
        'location': 'Building A - Rooftop',
        'status': 'active',
        'purchase_date': datetime(2017, 5, 20).date(),
        'manufacturer': 'Baltimore Aircoil',
        'model_number': 'VXC-400',
        'last_maintenance': datetime(2025, 11, 5).date(),
        'next_maintenance': datetime(2026, 2, 5).date(),
    },
    {
        'name': 'Conveyor Belt System',
        'description': 'Automated material handling conveyor',
        'equipment_type': 'mechanical',
        'serial_number': 'CVY-2024-006',
        'location': 'Building B - Warehouse',
        'status': 'active',
        'purchase_date': datetime(2020, 11, 12).date(),
        'manufacturer': 'Dorner Manufacturing',
        'model_number': '2200-Series',
        'last_maintenance': datetime(2025, 12, 15).date(),
        'next_maintenance': datetime(2026, 3, 15).date(),
    },
    {
        'name': 'Welding Robot Arm',
        'description': 'Automated robotic welding system',
        'equipment_type': 'electronic',
        'serial_number': 'WRB-2024-007',
        'location': 'Building A - Welding Station',
        'status': 'inactive',
        'purchase_date': datetime(2022, 2, 8).date(),
        'manufacturer': 'FANUC',
        'model_number': 'ARC Mate 100iD',
        'last_maintenance': datetime(2025, 9, 20).date(),
    },
]

created_equipment = []
for eq_data in equipment_data:
    equipment, created = Equipment.objects.get_or_create(
        serial_number=eq_data['serial_number'],
        defaults=eq_data
    )
    created_equipment.append(equipment)
    status_icon = {'active': '🟢', 'inactive': '🔴', 'maintenance': '🟡'}.get(equipment.status, '⚪')
    print(f"  {'✓ Created' if created else '✓ Found'}: {equipment.name} {status_icon} [{equipment.serial_number}]")

# Create Maintenance Team
print("\n👷 Creating Maintenance Team Members...")
team_data = [
    {
        'name': 'Michael Johnson',
        'email': 'michael.johnson@gearguard.com',
        'phone': '+1-555-0101',
        'role': 'senior_technician',
        'specialization': 'mechanical',
        'employee_id': 'EMP-001',
        'hire_date': datetime(2018, 4, 15).date(),
        'certifications': 'Certified Maintenance Professional (CMP), OSHA 30-Hour',
        'is_active': True,
    },
    {
        'name': 'Jennifer Martinez',
        'email': 'jennifer.martinez@gearguard.com',
        'phone': '+1-555-0102',
        'role': 'engineer',
        'specialization': 'electrical',
        'employee_id': 'EMP-002',
        'hire_date': datetime(2019, 7, 20).date(),
        'certifications': 'Licensed Electrical Engineer, PLC Programming',
        'is_active': True,
    },
    {
        'name': 'Robert Chen',
        'email': 'robert.chen@gearguard.com',
        'phone': '+1-555-0103',
        'role': 'technician',
        'specialization': 'hydraulic',
        'employee_id': 'EMP-003',
        'hire_date': datetime(2020, 2, 10).date(),
        'certifications': 'Hydraulics Specialist, Level II Certification',
        'is_active': True,
    },
    {
        'name': 'Emily Davis',
        'email': 'emily.davis@gearguard.com',
        'phone': '+1-555-0104',
        'role': 'supervisor',
        'specialization': 'general',
        'employee_id': 'EMP-004',
        'hire_date': datetime(2017, 11, 5).date(),
        'certifications': 'Maintenance Management, Six Sigma Green Belt',
        'is_active': True,
    },
    {
        'name': 'James Wilson',
        'email': 'james.wilson@gearguard.com',
        'phone': '+1-555-0105',
        'role': 'technician',
        'specialization': 'electronic',
        'employee_id': 'EMP-005',
        'hire_date': datetime(2021, 6, 18).date(),
        'certifications': 'Electronics Technician, Robotics Certification',
        'is_active': True,
    },
]

created_team = []
for team_member in team_data:
    member, created = MaintenanceTeam.objects.get_or_create(
        employee_id=team_member['employee_id'],
        defaults=team_member
    )
    created_team.append(member)
    print(f"  {'✓ Created' if created else '✓ Found'}: {member.name} - {member.get_role_display()} ({member.get_specialization_display()})")

# Create Maintenance Requests
print("\n🔧 Creating Sample Maintenance Requests...")
if created_equipment and created_team:
    requests_data = [
        {
            'equipment': created_equipment[2],  # CNC Machine
            'title': 'Spindle alignment issue',
            'description': 'CNC spindle showing wobble during high-speed operations. Requires immediate inspection and realignment.',
            'priority': 'high',
            'status': 'in_progress',
            'assigned_to': created_team[0],  # Michael Johnson
            'requested_by': 'Sarah Johnson',
            'due_date': (timezone.now() + timedelta(days=2)).date(),
            'estimated_hours': 8.5,
            'notes': 'Parts ordered. Scheduled for weekend maintenance window.',
        },
        {
            'equipment': created_equipment[0],  # Air Compressor
            'title': 'Routine pressure valve inspection',
            'description': 'Quarterly inspection of safety pressure valves and gaskets.',
            'priority': 'medium',
            'status': 'assigned',
            'assigned_to': created_team[2],  # Robert Chen
            'requested_by': 'Mike Smith',
            'due_date': (timezone.now() + timedelta(days=7)).date(),
            'estimated_hours': 3.0,
        },
        {
            'equipment': created_equipment[3],  # Generator
            'title': 'Oil change and filter replacement',
            'description': 'Scheduled maintenance: engine oil change, oil filter, air filter replacement.',
            'priority': 'medium',
            'status': 'pending',
            'requested_by': 'Lisa Brown',
            'due_date': (timezone.now() + timedelta(days=14)).date(),
            'estimated_hours': 4.5,
        },
        {
            'equipment': created_equipment[1],  # Hydraulic Press
            'title': 'Hydraulic fluid leak repair',
            'description': 'Small hydraulic fluid leak detected at main cylinder seal. Needs immediate attention.',
            'priority': 'urgent',
            'status': 'assigned',
            'assigned_to': created_team[2],  # Robert Chen
            'requested_by': 'David Wilson',
            'due_date': (timezone.now() + timedelta(days=1)).date(),
            'estimated_hours': 6.0,
            'notes': 'Replacement seals available in stock.',
        },
        {
            'equipment': created_equipment[6],  # Welding Robot
            'title': 'System diagnostic and recalibration',
            'description': 'Robot arm positioning errors. Requires full diagnostic check and recalibration.',
            'priority': 'high',
            'status': 'pending',
            'requested_by': 'Sarah Johnson',
            'due_date': (timezone.now() + timedelta(days=5)).date(),
            'estimated_hours': 10.0,
        },
    ]
    
    for req_data in requests_data:
        request, created = MaintenanceRequest.objects.get_or_create(
            equipment=req_data['equipment'],
            title=req_data['title'],
            defaults=req_data
        )
        priority_icon = {'low': '🟢', 'medium': '🟡', 'high': '🟠', 'urgent': '🔴'}.get(request.priority, '⚪')
        print(f"  {'✓ Created' if created else '✓ Found'}: #{request.id} - {request.title} {priority_icon} [{request.get_status_display()}]")

print("\n" + "="*60)
print("✅ Sample data population completed!")
print("="*60)

# Print summary
print("\n📊 SUMMARY:")
print(f"  Users: {User.objects.count()}")
print(f"  Groups: {Group.objects.count()}")
print(f"  Equipment: {Equipment.objects.count()}")
print(f"  Team Members: {MaintenanceTeam.objects.count()}")
print(f"  Maintenance Requests: {MaintenanceRequest.objects.count()}")

print("\n" + "="*60)
print("🔐 LOGIN CREDENTIALS:")
print("="*60)
print("\n👤 USERS:")
for user_data in users_data:
    print(f"\n  Username: {user_data['username']}")
    print(f"  Password: admin123 / manager123 / tech123 / super123")
    print(f"  Name: {user_data['first_name']} {user_data['last_name']}")
    print(f"  Role: {', '.join(user_data.get('groups', []))}")

print("\n✅ You can now login to http://localhost:8000/admin")
print("   with any of the credentials above!")
