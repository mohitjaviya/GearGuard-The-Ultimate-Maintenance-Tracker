# GearGuard - Developer Reference Card

**Quick lookup reference for common tasks and commands**

---

## 🚀 Environment Setup

### Initial Setup (One Time)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -m django --version  # Should show: 5.2.9
```

### Daily Startup
```bash
# Activate virtual environment
venv\Scripts\activate

# Start development server
python manage.py runserver

# Access admin
http://localhost:8000/admin
```

---

## 📚 Django Commands

### Database Operations
```bash
# Create new migrations
python manage.py makemigrations

# Apply pending migrations
python manage.py migrate

# Specific app migration
python manage.py migrate app_name

# Show migration info
python manage.py showmigrations

# Undo last migration
python manage.py migrate app_name 0001  # Revert to first
```

### User Management
```bash
# Create superuser
python manage.py createsuperuser

# Change password
python manage.py changepassword username

# Create user (in shell)
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('username', 'email@ex.com', 'password')
```

### Development
```bash
# Start development server
python manage.py runserver

# Start on different port
python manage.py runserver 8001

# Interactive Python shell with Django
python manage.py shell

# Check project configuration
python manage.py check

# List all available commands
python manage.py help
```

### App Management
```bash
# Create new app
python manage.py startapp app_name

# Create app in src folder
python manage.py startapp -d src/app_name app_name

# Start new project
django-admin startproject project_name
```

### Static Files
```bash
# Collect static files (production)
python manage.py collectstatic

# Find static files
python manage.py findstatic filename
```

### Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test app_name

# Run specific test class
python manage.py test app_name.tests.TestClassName

# Run with verbosity
python manage.py test --verbosity=2
```

### Other
```bash
# Dump database
python manage.py dumpdata > backup.json

# Load data
python manage.py loaddata backup.json

# Clear all data
python manage.py flush

# Generate secret key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

---

## 🗄️ Django Shell Basics

Access interactive Python shell with Django loaded:
```bash
python manage.py shell
```

### Common Shell Commands

```python
# Import models
from equipment.models import Equipment
from maintenance_request.models import MaintenanceRequest
from maintenance_team.models import MaintenanceTeam

# Query all
Equipment.objects.all()

# Count
Equipment.objects.count()

# Get specific
Equipment.objects.get(id=1)
Equipment.objects.get(serial_number='CPR-2024-001')

# Filter
Equipment.objects.filter(status='active')
Equipment.objects.filter(status='active').count()

# Create
Equipment.objects.create(
    name='Compressor',
    equipment_type='Mechanical',
    serial_number='CPR-001',
    location='Building A'
)

# Update
eq = Equipment.objects.get(id=1)
eq.status = 'maintenance'
eq.save()

# Delete
eq = Equipment.objects.get(id=1)
eq.delete()

# Order by
Equipment.objects.all().order_by('name')
Equipment.objects.all().order_by('-created_at')  # Descending

# Exclude
Equipment.objects.exclude(status='inactive')

# Or query
from django.db.models import Q
Equipment.objects.filter(Q(status='active') | Q(status='maintenance'))

# First/Last
Equipment.objects.first()
Equipment.objects.last()

# Limit
Equipment.objects.all()[:5]  # First 5

# Count distinct
Equipment.objects.values('equipment_type').distinct().count()

# Get or create
obj, created = Equipment.objects.get_or_create(serial_number='NEW-001', defaults={'name': 'New'})

# Bulk create (faster)
objs = [Equipment(...), Equipment(...)]
Equipment.objects.bulk_create(objs)

# Exit shell
exit()
```

---

## 📝 File Locations

### Important Directories
```
gearguard/
├── settings.py          # Configuration here
├── urls.py              # Main routes here
└── wsgi.py              # Production config

src/equipment/
├── models.py            # Data structures
├── views.py             # Request handlers
├── urls.py              # App routes
├── forms.py             # Form classes
├── admin.py             # Admin config
└── templates/           # HTML files
    └── equipment/
        ├── list.html
        ├── detail.html
        └── form.html

assets/
├── css/
├── js/
└── images/
```

### Python Path Variables
```python
# In settings.py
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / 'assets'
TEMPLATES_DIR = BASE_DIR / 'templates'
```

---

## 🔧 Common Code Snippets

### Model Definition
```python
from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Equipment'
```

### View (Function-Based)
```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment
from .forms import EquipmentForm

@login_required
def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment/list.html', {'equipment': equipment})

@login_required
def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'equipment/detail.html', {'equipment': equipment})

@login_required
def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment/form.html', {'form': form})
```

### URL Routing
```python
# src/equipment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('add/', views.equipment_create, name='equipment_create'),
]

# gearguard/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipment/', include('equipment.urls')),
]
```

### Form Definition
```python
from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
```

### Template Fragment
```html
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <h1>Equipment List</h1>
    
    {% for item in equipment %}
        <div class="card">
            <h3>{{ item.name }}</h3>
            <p>{{ item.description }}</p>
            <span class="badge">{{ item.status }}</span>
        </div>
    {% empty %}
        <p>No equipment found.</p>
    {% endfor %}
</div>
{% endblock %}
```

### Admin Configuration
```python
from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'location', 'created_at']
    search_fields = ['name', 'serial_number']
    list_filter = ['status', 'equipment_type']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
```

---

## 🐛 Debugging

### Print Debugging
```python
# In your code
print(f"Equipment: {equipment.name}")
print(f"Type: {type(equipment)}")
print(f"Vars: {vars(equipment)}")
```

### Django Debug Toolbar
```bash
pip install django-debug-toolbar

# Add to INSTALLED_APPS
'debug_toolbar',

# Add to MIDDLEWARE
'debug_toolbar.middleware.DebugToolbarMiddleware',

# Add to urls.py
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
```

### Logging
```python
import logging
logger = logging.getLogger(__name__)

logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
```

### Check Configuration
```bash
python manage.py check
python manage.py test --no-migrations
```

---

## 🔄 Git Workflow

```bash
# Initial commit
git init
git add .
git commit -m "Initial commit"

# Create branch
git checkout -b feature/equipment-management

# Make changes
# ... edit files ...

# Commit changes
git add src/equipment/models.py
git commit -m "Add equipment model"

# Push branch
git push origin feature/equipment-management

# Merge (on main branch)
git checkout main
git merge feature/equipment-management

# Delete branch
git branch -d feature/equipment-management
```

---

## 🧪 Testing Examples

```python
from django.test import TestCase
from .models import Equipment

class EquipmentTestCase(TestCase):
    def setUp(self):
        Equipment.objects.create(
            name='Compressor',
            equipment_type='Mechanical',
            serial_number='CPR-001'
        )
    
    def test_equipment_creation(self):
        eq = Equipment.objects.get(serial_number='CPR-001')
        self.assertEqual(eq.name, 'Compressor')
    
    def test_equipment_string(self):
        eq = Equipment.objects.get(serial_number='CPR-001')
        self.assertEqual(str(eq), 'Compressor')
```

Run tests:
```bash
python manage.py test equipment
python manage.py test equipment.tests.EquipmentTestCase.test_equipment_creation
```

---

## 📦 Installing Packages

```bash
# Install specific version
pip install django==5.2.9

# Install from requirements
pip install -r requirements.txt

# Save installed packages
pip freeze > requirements.txt

# Uninstall package
pip uninstall package_name

# List installed packages
pip list

# Upgrade package
pip install --upgrade package_name
```

---

## 🔐 Security Checklist

```python
# In settings.py

# Development
DEBUG = True  # Set False in production
SECRET_KEY = os.environ.get('SECRET_KEY')  # Use environment variable

# Production
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {...}
```

---

## 📊 Database Queries

### Performance Tips
```python
# Bad: N+1 queries
for request in MaintenanceRequest.objects.all():
    print(request.equipment.name)  # Extra query per item

# Good: Select related (for ForeignKey)
for request in MaintenanceRequest.objects.select_related('equipment'):
    print(request.equipment.name)  # No extra queries

# Good: Prefetch related (for reverse ForeignKey)
team_members = MaintenanceTeam.objects.prefetch_related('assignments')

# Cache results
from django.views.decorators.cache import cache_page
@cache_page(60 * 5)  # 5 minutes
def view_name(request):
    ...
```

---

## 🌐 URL Examples

```
Admin Panel:        http://localhost:8000/admin/
Equipment List:     http://localhost:8000/equipment/
Equipment Detail:   http://localhost:8000/equipment/1/
Equipment Create:   http://localhost:8000/equipment/add/
Equipment Edit:     http://localhost:8000/equipment/1/edit/
Equipment Delete:   http://localhost:8000/equipment/1/delete/
```

---

## 💡 Tips & Tricks

### Use Django Shell for Testing
```bash
python manage.py shell

>>> from equipment.models import Equipment
>>> eq = Equipment.objects.first()
>>> eq.name
```

### Quick Database Reset
```bash
# CAUTION: Deletes all data!
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Create Fixture
```bash
python manage.py dumpdata > backup.json
python manage.py loaddata backup.json
```

### Prettify JSON
```bash
python manage.py dumpdata --indent 2 > backup.json
```

---

## 📈 Useful Patterns

### Query with Count
```python
from django.db.models import Count

# Count requests per equipment
equipment = Equipment.objects.annotate(request_count=Count('maintenancerequest'))
```

### Pagination
```python
from django.core.paginator import Paginator

paginator = Paginator(queryset, 25)
page = paginator.get_page(request.GET.get('page', 1))
```

### Filter with Multiple Conditions
```python
from django.db.models import Q

# Complex queries
results = Equipment.objects.filter(
    Q(status='active') | Q(status='maintenance'),
    location='Building A'
)
```

---

## 🎯 Quick Checklist

Every time you add a model:
- [ ] Create model in models.py
- [ ] Create migration: `python manage.py makemigrations`
- [ ] Apply migration: `python manage.py migrate`
- [ ] Register in admin.py
- [ ] Test in shell
- [ ] Create views
- [ ] Create URLs
- [ ] Create templates
- [ ] Test in browser

---

**Reference Version**: 1.0.0
**Last Updated**: December 27, 2025
**Project**: GearGuard - The Ultimate Maintenance Tracker
