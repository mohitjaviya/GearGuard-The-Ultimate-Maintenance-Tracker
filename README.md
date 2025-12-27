# GearGuard-The-Ultimate-Maintenance-Tracker

## 📋 Project Overview

**GearGuard** is a comprehensive maintenance tracking system designed to manage equipment maintenance requests, track maintenance teams, and generate reports. It helps organizations streamline their maintenance operations by providing a centralized platform for scheduling, tracking, and reporting on equipment maintenance activities.

### Key Features:
- **Equipment Management**: Register and track all equipment
- **Maintenance Requests**: Create and manage maintenance tickets
- **Team Management**: Assign and track maintenance team members
- **Reporting**: Generate detailed reports on maintenance activities
- **Real-time Status Tracking**: Monitor maintenance request status

---

## 💻 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Django (Python) |
| **Database** | SQLite (Development) / PostgreSQL (Production) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **API** | Django REST Framework (if needed) |
| **Web Server** | Django Development Server / Gunicorn (Production) |

---

## 📁 Project Structure

```
GearGuard-The-Ultimate-Maintenance-Tracker/
├── gearguard/                    # Main Django project settings
│   ├── __init__.py
│   ├── settings.py               # Project configuration
│   ├── urls.py                   # URL routing
│   ├── asgi.py                   # ASGI config
│   └── wsgi.py                   # WSGI config
├── src/                          # Django applications
│   ├── equipment/                # Equipment management module
│   ├── maintenance_request/      # Maintenance request module
│   ├── maintenance_team/         # Team management module
│   └── reports/                  # Reports & analytics module
├── assets/                       # Static files (CSS, JS, images)
├── docs/                         # Documentation
├── manage.py                     # Django management script
├── db.sqlite3                    # SQLite database
└── README.md                     # This file
```

---

## 🚀 Step-by-Step Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git
- Windows/Mac/Linux

### Step 1: Clone/Setup the Project

```bash
# Navigate to your workspace
cd c:\Users\PREMIUM\GearGuard-The-Ultimate-Maintenance-Tracker

# Verify you're in the right directory
dir
```

### Step 2: Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Required Dependencies

```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install Django and dependencies
pip install django==5.2.9
pip install djangorestframework
pip install django-cors-headers
pip install python-dotenv
pip install pillow
```

### Step 4: Install Project Dependencies (Create requirements.txt)

Create a `requirements.txt` file in the project root:

```
Django==5.2.9
djangorestframework==3.14.0
django-cors-headers==4.3.0
python-dotenv==1.0.0
pillow==10.0.0
gunicorn==21.2.0
psycopg2-binary==2.9.0
```

Then install:
```bash
pip install -r requirements.txt
```

### Step 5: Configure Django Apps

Update `gearguard/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    # Your apps
    'equipment',
    'maintenance_request',
    'maintenance_team',
    'reports',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
]
```

### Step 6: Create Database Models

**src/equipment/models.py**:
```python
from django.db import models

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    equipment_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    purchase_date = models.DateField()
    last_maintenance = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
```

**src/maintenance_request/models.py**:
```python
from django.db import models
from equipment.models import Equipment

class MaintenanceRequest(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    requested_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
```

**src/maintenance_team/models.py**:
```python
from django.db import models

class MaintenanceTeam(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

### Step 7: Run Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Step 8: Create Superuser (Admin)

```bash
python manage.py createsuperuser
# Follow prompts to create admin account
```

### Step 9: Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://localhost:8000`

---

## 🎨 UI/UX Design Overview

Based on your requirements, the interface includes:

### Main Components:

1. **Dashboard**: Overview of all maintenance activities
2. **Equipment Management**: CRUD operations for equipment
3. **Maintenance Requests**: Create and track maintenance tickets
4. **Team Management**: Manage maintenance staff
5. **Reports**: Analytics and maintenance reports
6. **Admin Panel**: Django admin for system management

### Recommended UI Framework:
- **Frontend Framework**: React.js (optional, for better UX)
- **UI Library**: Bootstrap 5 or Material-UI
- **Icons**: FontAwesome or Material Icons

---

## 🔧 Common Commands

```bash
# Create a new app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

# Collect static files
python manage.py collectstatic

# Shell for testing
python manage.py shell

# Check project status
python manage.py check
```

---

## 📊 Database Schema

```
Equipment
├── id (Primary Key)
├── name
├── description
├── equipment_type
├── serial_number
├── location
├── status
├── purchase_date
├── last_maintenance
└── timestamps

MaintenanceRequest
├── id (Primary Key)
├── equipment_id (Foreign Key)
├── title
├── description
├── priority
├── status
├── requested_date
├── completion_date
└── timestamps

MaintenanceTeam
├── id (Primary Key)
├── name
├── email
├── phone
├── role
├── specialization
├── is_active
└── created_at
```

---

## 🔐 Security Considerations

- Change `SECRET_KEY` before production
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Implement proper authentication
- Add HTTPS in production
- Use security headers

---

## 📝 Development Workflow

1. **Setup Environment**: Virtual environment + dependencies
2. **Create Models**: Define database structure
3. **Run Migrations**: Update database
4. **Create Views**: Handle business logic
5. **Build Templates**: Create HTML interfaces
6. **Test**: Test all features
7. **Deploy**: Deploy to production

---

## 🤝 Contributing

1. Create a feature branch
2. Make changes
3. Test thoroughly
4. Commit with clear messages
5. Push and create pull request

---

## 📞 Support

For issues or questions, check the documentation or contact the development team.

---

## 📄 License

