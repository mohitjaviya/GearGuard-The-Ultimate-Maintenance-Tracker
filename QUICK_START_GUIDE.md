# GearGuard - Quick Start Guide

## 🚀 Start Here (5 Minutes)

### For Windows Users - Copy & Paste Commands

**Step 1: Open PowerShell and navigate to project**
```powershell
cd C:\Users\PREMIUM\GearGuard-The-Ultimate-Maintenance-Tracker
```

**Step 2: Create virtual environment**
```powershell
python -m venv venv
```

**Step 3: Activate virtual environment**
```powershell
venv\Scripts\activate
```

Your prompt should now show: `(venv) C:\Users\PREMIUM\GearGuard-The-Ultimate-Maintenance-Tracker>`

**Step 4: Install dependencies**
```powershell
pip install -r requirements.txt
```

**Step 5: Run migrations**
```powershell
python manage.py migrate
```

**Step 6: Create admin account**
```powershell
python manage.py createsuperuser
```

When prompted, enter:
- Username: `admin`
- Email: `admin@gearguard.com`
- Password: (create your own secure password)

**Step 7: Start the server**
```powershell
python manage.py runserver
```

**Step 8: Open in browser**
Visit: http://localhost:8000/admin

Login with your credentials!

---

## 📌 Project Summary

**Project Name**: GearGuard - The Ultimate Maintenance Tracker
**Language**: Python
**Framework**: Django 5.2.9
**Database**: SQLite (Development) / PostgreSQL (Production)
**Frontend**: HTML5, CSS3, JavaScript
**Type**: Web Application (Full-Stack)

---

## 🎯 What GearGuard Does

A **complete maintenance tracking system** that helps organizations:

1. **Track Equipment** - Register and monitor all equipment
2. **Manage Requests** - Create and track maintenance tickets
3. **Assign Teams** - Distribute work to maintenance staff
4. **Generate Reports** - Analyze maintenance performance
5. **Monitor Status** - Real-time status of all activities

---

## 📊 Technology Stack Breakdown

| Component | Technology | Why? |
|-----------|-----------|------|
| **Server** | Django (Python) | Powerful, secure, rapid development |
| **Database** | SQLite | Easy for development, no setup needed |
| **Frontend** | HTML/CSS/JS | Standard web technologies |
| **Framework** | Django (MVC/MVT) | Built-in admin, ORM, security |
| **API** | Django REST Framework | RESTful API for mobile/external integration |

---

## 🏗️ Project Architecture

```
┌─────────────────────────────────────┐
│     User Interface (HTML/CSS/JS)    │
│     (Browser: http://localhost:8000)│
└──────────────┬──────────────────────┘
               │ (HTTP Requests)
┌──────────────▼──────────────────────┐
│        Django Web Framework         │
│  ┌─────────────────────────────────┐│
│  │  URL Routing (urls.py)          ││
│  │  Views (views.py)               ││
│  │  Templates (HTML files)         ││
│  │  Forms (forms.py)               ││
│  └─────────────────────────────────┘│
└──────────────┬──────────────────────┘
               │ (ORM Queries)
┌──────────────▼──────────────────────┐
│     SQLite Database (db.sqlite3)    │
│  ┌─────────────────────────────────┐│
│  │  Equipment Table                ││
│  │  MaintenanceRequest Table       ││
│  │  MaintenanceTeam Table          ││
│  │  User & Auth Tables             ││
│  └─────────────────────────────────┘│
└─────────────────────────────────────┘
```

---

## 📁 File Structure Explanation

```
Project Root (c:\Users\PREMIUM\GearGuard-...)
│
├── gearguard/              ← Project Configuration
│   ├── settings.py         ← Database, apps, middleware config
│   ├── urls.py             ← Main URL routing
│   └── wsgi.py             ← Production deployment
│
├── src/                    ← Django Apps (Business Logic)
│   ├── equipment/          ← Equipment management module
│   │   ├── models.py       ← Database structure
│   │   ├── views.py        ← Request handlers
│   │   ├── urls.py         ← URL patterns
│   │   └── templates/      ← HTML pages
│   │
│   ├── maintenance_request/← Request management
│   ├── maintenance_team/   ← Staff management
│   └── reports/            ← Analytics & reports
│
├── assets/                 ← Static files (CSS, JS, images)
├── db.sqlite3              ← Database file (auto-created)
├── manage.py               ← Django command tool
├── requirements.txt        ← Python dependencies
└── README.md               ← Project documentation
```

---

## 🔄 Request Flow Example

When user clicks "Create Maintenance Request":

```
1. Browser sends HTTP POST request
                ↓
2. Django receives at urls.py route
                ↓
3. View function processes form data
                ↓
4. Form validation happens
                ↓
5. Model saves data to database
                ↓
6. Database stores in MaintenanceRequest table
                ↓
7. View redirects to request list
                ↓
8. Browser displays updated list
```

---

## 🔑 Key Django Concepts

### Models (models.py)
Defines database tables and their fields.
```python
class Equipment(models.Model):
    name = models.CharField(max_length=100)  # Text field
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Views (views.py)
Handles business logic and returns responses.
```python
def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipment': equipment})
```

### Templates (templates/)
HTML files with Django template syntax.
```html
{% for item in equipment %}
    <div>{{ item.name }} - {{ item.status }}</div>
{% endfor %}
```

### URLs (urls.py)
Maps URLs to views.
```python
path('equipment/', equipment_list, name='equipment-list')
# Accessible at http://localhost:8000/equipment/
```

---

## 📱 Main Pages You'll Create

| URL | Purpose | What Happens |
|-----|---------|--------------|
| `/admin/` | Admin panel | Manage all data |
| `/dashboard/` | Main dashboard | Overview & stats |
| `/equipment/` | Equipment list | View all equipment |
| `/equipment/add/` | Add equipment | Create new equipment |
| `/requests/` | Requests list | View maintenance requests |
| `/requests/add/` | Add request | Create new request |
| `/team/` | Team members | Manage staff |
| `/reports/` | Reports | Analytics & reports |

---

## 💾 Database Tables (Auto-Created)

### Equipment Table
```
Columns: id, name, type, serial_number, location, status, 
         purchase_date, last_maintenance, created_at, updated_at
```

### MaintenanceRequest Table
```
Columns: id, equipment_id (FK), title, description, priority, status,
         requested_date, completion_date, created_at, updated_at
```

### MaintenanceTeam Table
```
Columns: id, name, email, phone, role, specialization, is_active, created_at
```

### User Table (Auto-Created by Django)
```
Columns: id, username, email, password, first_name, last_name, is_staff, is_active
```

---

## 🔐 Default Admin Panel

Django provides a built-in admin panel at `/admin/`

**Features**:
- Add/edit/delete data
- User management
- Permissions
- Change history

**Login**: 
- URL: http://localhost:8000/admin/
- Username: admin (or your custom username)
- Password: (the one you created)

---

## ⚙️ Customization Guide

### Change Database (from SQLite to PostgreSQL)

1. Install PostgreSQL and psycopg2:
```bash
pip install psycopg2-binary
```

2. Update `gearguard/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gearguard_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

3. Run migrations:
```bash
python manage.py migrate
```

---

### Add a New Field to Equipment

1. Edit `src/equipment/models.py`:
```python
class Equipment(models.Model):
    warranty_expiry = models.DateField(null=True, blank=True)  # Add this
```

2. Create migration:
```bash
python manage.py makemigrations equipment
```

3. Apply migration:
```bash
python manage.py migrate equipment
```

---

## 🧪 Testing Your Setup

### Test 1: Django Installation
```bash
python -m django --version
# Should show: 5.2.9
```

### Test 2: Check Apps
```bash
python manage.py check
# Should show: System check identified no issues
```

### Test 3: Database Connection
```bash
python manage.py shell
>>> from equipment.models import Equipment
>>> Equipment.objects.count()  # Should return 0
>>> exit()
```

### Test 4: Admin Access
1. Start server: `python manage.py runserver`
2. Visit: http://localhost:8000/admin
3. Login with admin credentials

---

## 🐛 Common Issues & Solutions

### Issue: `ModuleNotFoundError: No module named 'django'`
**Solution**: Activate virtual environment first
```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: `No such table: equipment_equipment`
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Issue: Superuser password wrong
**Solution**: Create new superuser
```bash
python manage.py createsuperuser
```

### Issue: Port 8000 already in use
**Solution**: Use different port
```bash
python manage.py runserver 8001
```

### Issue: Database locked
**Solution**: Delete db.sqlite3 and recreate
```bash
# Delete: db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 📚 Next Steps

1. **Add Models** - Define Equipment, Request, Team models
2. **Create Views** - Build list/detail/create/edit views
3. **Build Templates** - Create HTML pages
4. **Style with CSS** - Add Bootstrap or custom CSS
5. **Test** - Write and run tests
6. **Deploy** - Move to production server

---

## 🚀 Production Deployment Preview

When ready for production:

```bash
# 1. Set DEBUG = False in settings.py
# 2. Update ALLOWED_HOSTS = ['yourdomain.com']
# 3. Generate SECRET_KEY from environment
# 4. Use PostgreSQL instead of SQLite
# 5. Collect static files
python manage.py collectstatic

# 6. Use Gunicorn as app server
pip install gunicorn
gunicorn gearguard.wsgi:application

# 7. Use Nginx as reverse proxy
# 8. Enable HTTPS/SSL
# 9. Set up monitoring & backups
```

---

## 📞 Quick Help

### Getting Help in Django Shell
```bash
python manage.py shell

# List all equipment
>>> from equipment.models import Equipment
>>> Equipment.objects.all()

# Count equipment
>>> Equipment.objects.count()

# Get first equipment
>>> e = Equipment.objects.first()
>>> print(e.name)

# Create new equipment
>>> Equipment.objects.create(name="Pump", type="Hydraulic")

# Exit shell
>>> exit()
```

---

## ✅ Installation Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Dependencies installed from requirements.txt
- [ ] Database migrated successfully
- [ ] Superuser created
- [ ] Development server starts without errors
- [ ] Admin panel accessible at http://localhost:8000/admin
- [ ] Login works with credentials

---

## 📖 Documentation Files

Inside your project:
- **README.md** - Project overview
- **SETUP_GUIDE.md** - Detailed setup instructions
- **UI_DESIGN_SPECIFICATION.md** - UI/UX design details
- **IMPLEMENTATION_CHECKLIST.md** - Task checklist
- **QUICK_START_GUIDE.md** - This file

---

## 🎓 Learning Path

1. **Understand Django Basics** (1-2 hours)
   - Models, Views, Templates, URLs
   - Admin interface

2. **Create Models** (2-3 hours)
   - Define Equipment, Request, Team models
   - Understand relationships

3. **Build Views** (3-4 hours)
   - List views, Detail views
   - Create/Edit/Delete functionality

4. **Create Templates** (3-4 hours)
   - HTML pages, Bootstrap styling
   - Forms and tables

5. **Test Application** (2 hours)
   - Manual testing
   - Bug fixes

6. **Deploy** (2-3 hours)
   - Production setup
   - Domain configuration

---

## 🎉 You're Ready!

You now have:
- ✅ Complete project structure
- ✅ All dependencies configured
- ✅ Database ready
- ✅ Admin panel functional
- ✅ Comprehensive documentation
- ✅ Implementation checklist
- ✅ UI design specifications

**Next**: Choose a feature from IMPLEMENTATION_CHECKLIST.md and start coding!

---

**Version**: 1.0.0
**Last Updated**: December 27, 2025
**Project**: GearGuard - The Ultimate Maintenance Tracker
