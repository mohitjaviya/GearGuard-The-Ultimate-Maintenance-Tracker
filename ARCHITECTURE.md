# GearGuard - Architecture & API Documentation

## 🏛️ System Architecture

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend Layer                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  HTML Templates  │  CSS Styling  │  JavaScript       │  │
│  │  (User Interface)                                     │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP Requests/Responses
┌────────────────────────▼────────────────────────────────────┐
│                  Application Layer (Django)                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  URL Router (urls.py)                                │  │
│  │  Views (views.py) - Business Logic                   │  │
│  │  Forms (forms.py) - Data Validation                  │  │
│  │  Middleware - Request/Response Processing            │  │
│  │  Authentication & Authorization                      │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ ORM Queries
┌────────────────────────▼────────────────────────────────────┐
│                   Data Layer (Models)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Equipment Model  │  Request Model                   │  │
│  │  Team Model       │  User Model (Django Built-in)    │  │
│  │  ORM (Object-Relational Mapping)                     │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ SQL Commands
┌────────────────────────▼────────────────────────────────────┐
│               Database Layer (SQLite/PostgreSQL)            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Equipment  │  MaintenanceRequest  │  MaintenanceTeam  │  │
│  │  User       │  Auth Tables         │  Other Tables     │  │
│  │  (Persisted Data)                                    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Request/Response Flow

### Example: Viewing Equipment List

```
1. User opens browser and visits: http://localhost:8000/equipment/

2. Browser sends: GET /equipment/
                        ↓
3. Django URL Router matches: equipment/
                        ↓
4. Calls View Function: equipment_list(request)
                        ↓
5. View queries Database: Equipment.objects.all()
                        ↓
6. Database returns: List of equipment records
                        ↓
7. View renders Template: equipment_list.html
   (Injects equipment data into HTML)
                        ↓
8. Browser receives: HTML response
                        ↓
9. Browser displays: Equipment list page
```

---

## 🗂️ Django App Structure

### Equipment App Structure
```
src/equipment/
├── __init__.py              # Package marker
├── admin.py                 # Admin interface config
├── apps.py                  # App configuration
├── models.py                # Database models
├── views.py                 # Request handlers
├── urls.py                  # URL routing
├── forms.py                 # Form definitions
├── tests.py                 # Test cases
├── migrations/              # Database migrations
│   ├── __init__.py
│   └── 0001_initial.py      # Auto-generated
└── templates/
    └── equipment/
        ├── list.html        # Equipment list
        ├── detail.html      # Equipment detail
        └── form.html        # Create/Edit form
```

---

## 📊 Database Schema (Detailed)

### Equipment Table
```sql
CREATE TABLE equipment_equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    equipment_type VARCHAR(50),
    serial_number VARCHAR(100) UNIQUE,
    location VARCHAR(100),
    status VARCHAR(20),  -- 'active', 'inactive', 'maintenance'
    purchase_date DATE,
    last_maintenance DATE,
    created_at DATETIME AUTO_NOW_ADD,
    updated_at DATETIME AUTO_NOW
);
```

### MaintenanceRequest Table
```sql
CREATE TABLE maintenance_request_maintenancerequest (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    equipment_id INTEGER FOREIGN KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    priority VARCHAR(20),  -- 'low', 'medium', 'high', 'urgent'
    status VARCHAR(20),    -- 'pending', 'assigned', 'in_progress', 'completed'
    assigned_to_id INTEGER FOREIGN KEY (MaintenanceTeam),
    requested_date DATETIME,
    completion_date DATETIME,
    created_at DATETIME AUTO_NOW_ADD,
    updated_at DATETIME AUTO_NOW
);
```

### MaintenanceTeam Table
```sql
CREATE TABLE maintenance_team_maintenanceteam (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    email EMAIL,
    phone VARCHAR(20),
    role VARCHAR(50),
    specialization VARCHAR(100),
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME AUTO_NOW_ADD
);
```

### User Table (Django Built-in)
```sql
CREATE TABLE auth_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(150) UNIQUE,
    email EMAIL,
    password VARCHAR(128),  -- Hashed
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    is_staff BOOLEAN,
    is_active BOOLEAN,
    date_joined DATETIME
);
```

---

## 🔐 Authentication & Authorization

### User Roles

```
Admin
├─ Full access to all features
├─ Manage users
├─ System configuration
└─ All CRUD operations

Manager/Supervisor
├─ Create/edit maintenance requests
├─ Assign to teams
├─ View reports
└─ Cannot delete data

Maintenance Team
├─ View assigned requests
├─ Update request status
├─ Cannot create requests
└─ Cannot manage equipment

Viewer
├─ View-only access
├─ Cannot create or edit
└─ Cannot delete
```

### Permission System (Django)

```python
# In models.py
class Equipment(models.Model):
    class Meta:
        permissions = [
            ("can_view_equipment", "Can view equipment"),
            ("can_add_equipment", "Can add equipment"),
            ("can_change_equipment", "Can change equipment"),
            ("can_delete_equipment", "Can delete equipment"),
        ]

# In views.py
from django.contrib.auth.decorators import permission_required

@permission_required('equipment.can_view_equipment')
def equipment_list(request):
    ...
```

---

## 🔌 REST API Endpoints (Optional Enhancement)

If you implement Django REST Framework, these endpoints would be available:

### Equipment Endpoints
```
GET     /api/equipment/              # List all equipment
POST    /api/equipment/              # Create new equipment
GET     /api/equipment/{id}/         # Get equipment details
PUT     /api/equipment/{id}/         # Update equipment
DELETE  /api/equipment/{id}/         # Delete equipment
GET     /api/equipment/{id}/status/  # Get equipment status
```

### MaintenanceRequest Endpoints
```
GET     /api/requests/               # List all requests
POST    /api/requests/               # Create new request
GET     /api/requests/{id}/          # Get request details
PUT     /api/requests/{id}/          # Update request
DELETE  /api/requests/{id}/          # Delete request
PATCH   /api/requests/{id}/status/   # Update status
```

### Team Endpoints
```
GET     /api/team/                   # List all team members
POST    /api/team/                   # Add team member
GET     /api/team/{id}/              # Get member details
PUT     /api/team/{id}/              # Update member
DELETE  /api/team/{id}/              # Remove member
GET     /api/team/{id}/assignments/  # Get member's tasks
```

### Report Endpoints
```
GET     /api/reports/dashboard/      # Dashboard stats
GET     /api/reports/equipment/      # Equipment report
GET     /api/reports/requests/       # Request report
GET     /api/reports/team/           # Team report
GET     /api/reports/export/pdf/     # Export as PDF
GET     /api/reports/export/excel/   # Export as Excel
```

---

## 📤 Request/Response Examples

### Create Equipment Request

**Request**:
```
POST /api/equipment/
Content-Type: application/json

{
    "name": "Compressor Unit A",
    "description": "Industrial air compressor",
    "equipment_type": "Mechanical",
    "serial_number": "CPR-2024-001",
    "location": "Building A, Floor 2",
    "status": "active",
    "purchase_date": "2020-01-15"
}
```

**Response** (201 Created):
```json
{
    "id": 1,
    "name": "Compressor Unit A",
    "description": "Industrial air compressor",
    "equipment_type": "Mechanical",
    "serial_number": "CPR-2024-001",
    "location": "Building A, Floor 2",
    "status": "active",
    "purchase_date": "2020-01-15",
    "last_maintenance": null,
    "created_at": "2025-12-27T10:30:00Z",
    "updated_at": "2025-12-27T10:30:00Z"
}
```

---

### Create Maintenance Request

**Request**:
```
POST /api/requests/
Content-Type: application/json

{
    "equipment": 1,
    "title": "Oil leak detected",
    "description": "Oil seeping from valve connection",
    "priority": "urgent",
    "status": "pending"
}
```

**Response** (201 Created):
```json
{
    "id": 1,
    "equipment": 1,
    "title": "Oil leak detected",
    "description": "Oil seeping from valve connection",
    "priority": "urgent",
    "status": "pending",
    "requested_date": "2025-12-27T14:00:00Z",
    "completion_date": null,
    "created_at": "2025-12-27T14:00:00Z",
    "updated_at": "2025-12-27T14:00:00Z"
}
```

---

## 🔄 Data Flow Scenarios

### Scenario 1: Create Maintenance Request

```
Admin User
    ↓ (clicks "Create Request")
View: request_create()
    ↓ (displays form)
User fills form and submits
    ↓ (POST request)
Form validation
    ↓ (if valid)
Create MaintenanceRequest instance
    ↓
Save to database
    ↓
Send notification to assigned team (optional)
    ↓
Redirect to request list
    ↓
Display confirmation message
```

### Scenario 2: Update Request Status

```
Team Member
    ↓ (clicks on request)
View: request_detail()
    ↓ (displays request details)
Team member selects new status
    ↓ (clicks "Update Status")
View: update_request_status()
    ↓ (validates permission)
Update status in database
    ↓
Calculate completion time if completed
    ↓ (if completed)
Update equipment's last_maintenance date
    ↓
Send notification to requester (optional)
    ↓
Redirect to request list
```

---

## 🔧 Configuration Files

### settings.py Key Settings

```python
# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'equipment',
    'maintenance_request',
    'maintenance_team',
    'reports',
]

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security
SECRET_KEY = 'your-secret-key-here'
DEBUG = True  # Set to False in production
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

### urls.py Configuration

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipment.urls')),
    path('maintenance/', include('maintenance_request.urls')),
    path('team/', include('maintenance_team.urls')),
    path('reports/', include('reports.urls')),
]
```

---

## 📊 Performance Optimization

### Database Query Optimization

```python
# Bad: N+1 Query Problem
requests = MaintenanceRequest.objects.all()
for request in requests:
    print(request.equipment.name)  # Causes separate query per item

# Good: Use select_related() for ForeignKey
requests = MaintenanceRequest.objects.select_related('equipment')
for request in requests:
    print(request.equipment.name)  # No extra queries

# Good: Use prefetch_related() for ManyToMany
teams = MaintenanceTeam.objects.prefetch_related('assignments')
```

### Pagination

```python
# In views.py
from django.core.paginator import Paginator

def equipment_list(request):
    all_equipment = Equipment.objects.all()
    paginator = Paginator(all_equipment, 25)  # 25 per page
    page_num = request.GET.get('page', 1)
    equipment = paginator.get_page(page_num)
    return render(request, 'equipment/list.html', {'equipment': equipment})
```

### Caching

```python
# Simple cache
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # Cache for 5 minutes
def dashboard(request):
    stats = get_dashboard_stats()
    return render(request, 'dashboard.html', {'stats': stats})
```

---

## 🧪 Testing Architecture

### Test Structure

```
tests/
├── test_models.py           # Model tests
├── test_views.py            # View tests
├── test_forms.py            # Form tests
├── test_apis.py             # API tests
└── test_integration.py      # Integration tests
```

### Example Test

```python
from django.test import TestCase
from equipment.models import Equipment

class EquipmentModelTest(TestCase):
    def setUp(self):
        Equipment.objects.create(
            name="Compressor",
            equipment_type="Mechanical",
            serial_number="CPR-001"
        )
    
    def test_equipment_creation(self):
        eq = Equipment.objects.get(serial_number="CPR-001")
        self.assertEqual(eq.name, "Compressor")
    
    def test_string_representation(self):
        eq = Equipment.objects.get(serial_number="CPR-001")
        self.assertEqual(str(eq), "Compressor")
```

---

## 🔒 Security Considerations

### CSRF Protection
```python
# Enabled by default in Django
# Always use {% csrf_token %} in forms
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

### SQL Injection Prevention
```python
# Safe (using ORM)
equipment = Equipment.objects.filter(name=user_input)

# Unsafe (avoid)
query = f"SELECT * FROM equipment WHERE name = '{user_input}'"
```

### Authentication Checks
```python
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    # Only logged-in users can access
    pass
```

---

## 📈 Scalability Considerations

### Phase 1: Single Server (Current)
- Django development server
- SQLite database
- Static files served by Django

### Phase 2: Production Single Server
- Gunicorn application server
- Nginx reverse proxy
- PostgreSQL database
- Static files with WhiteNoise

### Phase 3: Scaled Infrastructure
- Load balancer (Nginx/HAProxy)
- Multiple Django instances
- Separate database server
- Redis cache
- Celery for async tasks

---

## 🔄 Deployment Checklist

- [ ] DEBUG = False
- [ ] SECRET_KEY from environment variable
- [ ] ALLOWED_HOSTS configured
- [ ] Database migration run
- [ ] Static files collected
- [ ] HTTPS enabled
- [ ] Email configured
- [ ] Backup strategy implemented
- [ ] Monitoring setup
- [ ] Error logging configured

---

## 📚 Architecture Decision Records (ADR)

### ADR 1: Why Django?
- Rapid development
- Built-in admin interface
- Excellent ORM
- Strong security features
- Large community

### ADR 2: Why SQLite for Development?
- No setup required
- Easy testing
- File-based storage
- Perfect for development

### ADR 3: Why PostgreSQL for Production?
- Robust and reliable
- Better performance
- Advanced features
- Better for multiple connections

---

**Version**: 1.0.0
**Last Updated**: December 27, 2025
