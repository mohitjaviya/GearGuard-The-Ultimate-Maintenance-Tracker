# GearGuard - Complete Setup Guide

## 🎯 Quick Start (5 Minutes)

### For Windows Users:

```bash
# 1. Open PowerShell in the project directory
cd C:\Users\PREMIUM\GearGuard-The-Ultimate-Maintenance-Tracker

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create admin user
python manage.py createsuperuser

# 7. Start development server
python manage.py runserver

# 8. Access the application
# Open browser: http://localhost:8000/admin
```

---

## 📦 Project Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend Framework** | Django 5.2.9 |
| **Database** | SQLite (Dev) / PostgreSQL (Prod) |
| **API** | Django REST Framework |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Server** | Django Dev Server / Gunicorn (Prod) |
| **Python Version** | 3.8+ |

---

## 🏗️ Project Structure Explanation

```
GearGuard/
│
├── gearguard/              # Project Configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL routing
│   ├── wsgi.py             # Production server config
│   └── asgi.py             # Async server config
│
├── src/                    # Django Applications
│   ├── equipment/          # Equipment CRUD operations
│   ├── maintenance_request/# Maintenance ticket management
│   ├── maintenance_team/   # Staff/Team management
│   └── reports/            # Analytics & reports
│
├── assets/                 # Static files (CSS, JS, images)
├── docs/                   # Documentation files
├── manage.py               # Django CLI tool
└── db.sqlite3              # Database file
```

---

## 🔑 Database Models Structure

### Equipment Model
```
- id: Auto-increment
- name: Equipment name
- description: Detailed info
- equipment_type: Type classification
- serial_number: Unique identifier
- location: Physical location
- status: Active/Inactive/Maintenance
- purchase_date: When acquired
- last_maintenance: Last service date
```

### MaintenanceRequest Model
```
- id: Auto-increment
- equipment: Foreign key to Equipment
- title: Request title
- description: Issue details
- priority: Low/Medium/High/Urgent
- status: Pending/Assigned/In Progress/Completed
- requested_date: When requested
- completion_date: When completed
```

### MaintenanceTeam Model
```
- id: Auto-increment
- name: Team member name
- email: Contact email
- phone: Contact number
- role: Job title
- specialization: Technical specialty
- is_active: Active status
```

---

## 🚀 Installation Steps Detailed

### Step 1: Install Python
- Download from python.org
- Version 3.8 or higher required
- Add to PATH during installation

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install from requirements.txt
pip install -r requirements.txt
```

### Step 4: Configure Database

```bash
# Create database tables
python manage.py migrate

# You should see:
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations...
#   Applying... OK
```

### Step 5: Create Administrator Account

```bash
python manage.py createsuperuser

# Enter details when prompted:
# Username: admin
# Email: admin@gearguard.com
# Password: (enter secure password)
# Password (again): (confirm)
```

### Step 6: Collect Static Files (Optional for Development)

```bash
python manage.py collectstatic
```

### Step 7: Start Development Server

```bash
python manage.py runserver

# Output should show:
# Quit the server with CTRL-BREAK
# Starting development server at http://127.0.0.1:8000/
```

### Step 8: Access the Application

- **Admin Panel**: http://localhost:8000/admin
- **Login**: Use credentials from Step 5

---

## 📱 Application Flow

```
User Login
    ↓
Dashboard (Overview)
    ↓
├─→ Equipment Management
│   ├─→ View all equipment
│   ├─→ Add new equipment
│   ├─→ Edit equipment
│   └─→ Delete equipment
│
├─→ Maintenance Requests
│   ├─→ Create request
│   ├─→ Assign to team
│   ├─→ Update status
│   └─→ Close request
│
├─→ Team Management
│   ├─→ Add team member
│   ├─→ View assignments
│   └─→ Manage availability
│
└─→ Reports
    ├─→ Maintenance history
    ├─→ Team performance
    └─→ Equipment status
```

---

## 🔧 Common Development Commands

```bash
# View all Django management commands
python manage.py help

# Start interactive Python shell with Django context
python manage.py shell

# Check project configuration
python manage.py check

# Create a new app
python manage.py startapp app_name

# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate app_name

# Load initial data
python manage.py loaddata fixture_name

# Dump data
python manage.py dumpdata app_name > data.json

# Create superuser
python manage.py createsuperuser

# Change user password
python manage.py changepassword username
```

---

## 🎨 Frontend Development

### Templates Structure
```
templates/
├── base.html              # Base template
├── index.html             # Home page
├── equipment/
│   ├── list.html          # Equipment list
│   ├── detail.html        # Equipment detail
│   └── form.html          # Equipment form
├── maintenance/
│   ├── list.html
│   ├── detail.html
│   └── form.html
└── reports/
    └── dashboard.html
```

### Static Files
```
assets/
├── css/
│   ├── style.css          # Custom styles
│   └── bootstrap.css      # Bootstrap
├── js/
│   ├── main.js            # Main script
│   └── bootstrap.js
└── images/
    └── logo.png
```

---

## 🧪 Testing Your Setup

### Test 1: Verify Python Installation
```bash
python --version
# Should output: Python 3.x.x
```

### Test 2: Check Virtual Environment
```bash
where python
# Should show path to venv
```

### Test 3: Verify Django Installation
```bash
python -m django --version
# Should output: 5.2.9
```

### Test 4: Test Database Connection
```bash
python manage.py dbshell
# Should open SQLite shell
# Type: .exit to quit
```

### Test 5: Run Development Server
```bash
python manage.py runserver

# Visit http://localhost:8000/admin
# Login with superuser credentials
```

---

## 🐛 Troubleshooting

### Issue: "django module not found"
```bash
# Solution: Activate virtual environment
venv\Scripts\activate

# Or install Django
pip install django==5.2.9
```

### Issue: "No such table" error
```bash
# Solution: Run migrations
python manage.py migrate
```

### Issue: Superuser not created
```bash
# Solution: Create superuser
python manage.py createsuperuser
```

### Issue: Port 8000 already in use
```bash
# Solution: Use different port
python manage.py runserver 8001
```

### Issue: Database locked
```bash
# Solution: Delete db.sqlite3 and recreate
# (Only for development!)
python manage.py migrate
```

---

## 📊 Performance Optimization Tips

1. **Use Database Indexing**
```python
class Equipment(models.Model):
    serial_number = models.CharField(max_length=100, db_index=True)
```

2. **Enable Query Caching**
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

3. **Paginate Large Querysets**
```python
from django.core.paginator import Paginator
paginator = Paginator(queryset, 25)
page = paginator.get_page(1)
```

---

## 🔐 Security Checklist

- [ ] Change SECRET_KEY before production
- [ ] Set DEBUG = False in production
- [ ] Use environment variables for sensitive data
- [ ] Implement HTTPS
- [ ] Add CSRF protection
- [ ] Validate user inputs
- [ ] Use prepared statements for queries
- [ ] Set SECURE_SSL_REDIRECT = True
- [ ] Configure ALLOWED_HOSTS properly
- [ ] Use strong authentication

---

## 📈 Next Steps After Setup

1. **Create Django Apps** (if not already created)
```bash
python manage.py startapp equipment
python manage.py startapp maintenance_request
python manage.py startapp maintenance_team
python manage.py startapp reports
```

2. **Define Models** - Based on database schema provided

3. **Create Admin Interface**
```python
# admin.py
from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'location', 'last_maintenance']
    search_fields = ['name', 'serial_number']
    list_filter = ['status', 'equipment_type']
```

4. **Create Views and Templates**

5. **Implement API (Optional)**
```bash
pip install djangorestframework
```

6. **Deploy to Production**
- Use Gunicorn as application server
- Use Nginx as reverse proxy
- Use PostgreSQL for production database
- Set up SSL/TLS certificates

---

## 📚 Useful Resources

- Django Documentation: https://docs.djangoproject.com/
- Django REST Framework: https://www.django-rest-framework.org/
- Python Documentation: https://docs.python.org/
- SQLite Documentation: https://www.sqlite.org/docs.html

---

## 💬 FAQ

**Q: Should I commit db.sqlite3 to git?**
A: No, add it to .gitignore in production. For development, it's optional.

**Q: Can I use PostgreSQL instead of SQLite?**
A: Yes, update DATABASES in settings.py and install psycopg2.

**Q: How do I reset the database?**
A: Delete db.sqlite3 and run `python manage.py migrate` again.

**Q: How do I add a new field to a model?**
A: Add field to model, run `python manage.py makemigrations`, then `python manage.py migrate`.

**Q: How do I test my code?**
A: Create tests.py files and run `python manage.py test`.

---

## Version History

- **v1.0.0** - Initial setup (December 27, 2025)

---

**Last Updated**: December 27, 2025
