# 🔧 GearGuard Quick Reference Card

## 🚀 Getting Started

### Launch the Application
```bash
cd GearGuard-The-Ultimate-Maintenance-Tracker
python manage.py runserver
```
Then open: **http://localhost:8000**

---

## 👥 Test Accounts (Pre-loaded Sample Data)

### Admin Account
- **URL**: http://localhost:8000/admin/
- **Username**: john.admin
- **Password**: admin123
- **Role**: Superuser, Full Access

### Manager Account
- **Username**: sarah.manager
- **Password**: manager123
- **Role**: Manager, Can assign requests

### Technician Account  
- **Username**: mike.tech
- **Password**: tech123
- **Role**: Technician, Can complete requests

### Other Accounts
- **lisa.supervisor** / super123 (Supervisor)
- **david.tech** / tech123 (Technician)

---

## 📍 Main Pages

| Page | URL | Purpose |
|------|-----|---------|
| **Home** | `/` | Introduction & features |
| **Dashboard** | `/dashboard/` | Quick stats & recent requests |
| **Equipment** | `/equipment/` | Inventory with filters |
| **Teams** | `/teams/` | Team roster & workload |
| **Reports** | `/reports/` | Analytics & metrics |
| **Calendar** | `/dashboard/calendar/` | Monthly schedule view |
| **New Request** | `/requests/new/` | Submit maintenance request |
| **Admin** | `/admin/` | Full CRUD management |

---

## 🎯 Common Tasks

### Create a Maintenance Request
1. Click **"+ New Request"** button
2. Select **Equipment** from dropdown
3. Enter **Title** and **Description**
4. Set **Priority** (Low/Medium/High/Urgent)
5. Pick **Due Date**
6. Enter **Estimated Hours**
7. Click **Submit**

### Assign Request to Technician
1. Login as **Manager** or **Admin**
2. Go to `/admin/` → **Maintenance Requests**
3. Click on the request
4. Set **Status** to "assigned"
5. Select **Assigned To** technician
6. Click **Save**

### Mark Request Complete
1. Login as **Technician**
2. Go to `/admin/` → **Maintenance Requests**
3. Click on request assigned to you
4. Set **Status** to "completed"
5. Set **Completed At** timestamp
6. System auto-calculates **Actual Hours**
7. Click **Save**

### View Equipment Status
1. Go to `/equipment/`
2. Use **Status** dropdown to filter
3. Use **Type** dropdown to filter
4. Cards show:
   - Equipment name & serial number
   - Current status (Active/Maintenance/Inactive)
   - Last maintenance date
   - Next maintenance due

### Check Team Workload
1. Go to `/teams/`
2. See each team member's card
3. Workload bar shows active requests
4. Click member for details

### Generate Reports
1. Go to `/reports/`
2. View key metrics:
   - Completion rate %
   - Monthly request count
   - Average completion hours
   - Critical equipment count
3. Export data (admin panel)

---

## 📊 Dashboard Overview

### Stat Cards (Real-Time Data)
- **🔴 Critical Equipment**: Equipment in maintenance or inactive
- **⚙️ Technician Load**: % of team with active requests
- **✅ Open Requests**: Pending requests + overdue count

### Recent Requests Table
Shows last 10 requests with:
- Request ID
- Equipment name
- Title/Description
- Assigned technician
- Status badge (colored)
- Priority badge (colored)
- Due date

### Navigation Tabs
Quick access to:
- Dashboard (current view)
- Equipment Inventory
- Team Roster
- Reporting Analytics
- Maintenance Calendar

---

## 🔐 User Roles & Permissions

### 👨‍💼 Administrator
- ✅ Full system access
- ✅ User management
- ✅ Create/edit/delete equipment
- ✅ Manage team members
- ✅ View all reports
- ✅ Configure settings
- **Access**: `/admin/` panel

### 📋 Manager
- ✅ View all requests
- ✅ Assign requests to technicians
- ✅ Update request status
- ✅ View reports
- ✅ View team performance
- **Access**: Dashboard + `/admin/`

### 🔧 Technician
- ✅ View assigned requests
- ✅ Mark requests as in-progress
- ✅ Mark requests as complete
- ✅ View equipment details
- ✅ Create new requests
- **Access**: Dashboard only (no admin)

### 👁️ Viewer
- ✅ View dashboard
- ✅ View equipment
- ✅ View team info
- ✅ View reports
- ✅ Create requests
- **Access**: Dashboard only

### ❌ Unauthenticated
- ✅ View home page
- ✅ Login/signup page
- **Access**: `/`, `/accounts/`

---

## 🎨 Color Codes

### Status Badges
- 🟢 **Pending** (Light): Awaiting assignment
- 🟠 **Assigned** (Orange): Assigned to technician
- 🔵 **In Progress** (Blue): Work in progress
- ✅ **Completed** (Green): Work finished
- ❌ **Cancelled** (Red): Cancelled request

### Priority Badges
- 🟢 **Low** (Green): Non-urgent
- 🔵 **Medium** (Blue): Standard
- 🟠 **High** (Orange): Time-sensitive
- 🔴 **Urgent** (Red): Critical/Emergency

### Equipment Status
- 🟢 **Active**: Operating normally
- 🟡 **Maintenance**: Under maintenance
- 🔴 **Inactive**: Out of service

---

## 📱 Responsive Design

### Mobile Support
- ✅ Works on phones (< 768px)
- ✅ Optimized for tablets (768px - 1024px)
- ✅ Full features on desktop (> 1024px)
- ✅ Touch-friendly buttons
- ✅ Readable on small screens

### Navigation on Mobile
- Use hamburger menu (if implemented)
- Swipe between sections
- Back button to return
- Bottom navigation tabs

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `/` | Focus search (when available) |
| `Esc` | Close modal/dialog |
| `Enter` | Submit form |
| `Tab` | Navigate form fields |
| `Shift+Tab` | Reverse field navigation |

---

## 🆘 Troubleshooting

### "Page Not Found" Error
- Check URL spelling
- Ensure trailing slash: `/dashboard/` (not `/dashboard`)
- Try reloading page (Ctrl+R)

### Can't Login
- Verify username spelling
- Check caps lock (password is case-sensitive)
- Try resetting database: `python manage.py flush`
- Use sample account: mike.tech / tech123

### Admin Panel Not Accessible
- Ensure you logged in as admin
- Check user is_staff = True in database
- Try: `/admin/login/` directly

### Technician Can't See Dashboard
- Verify user is in 'Technicians' group
- Check user is_staff = True (optional)
- Log out and log back in
- Clear browser cache (Ctrl+Shift+Delete)

### Equipment Not Filtering
- Ensure equipment exists in system
- Try clearing filters (click "Clear" button)
- Refresh page
- Check equipment status values

### Slow Page Loading
- Check server is running properly
- Close other browser tabs
- Clear browser cache
- Run: `python manage.py check`

---

## 📞 Support Resources

### Documentation Files
- **FINAL_PROJECT_SUMMARY.md** - Complete project details
- **UI_IMPROVEMENTS.md** - Design system & UI specs
- **GETTING_STARTED.md** - Installation guide
- **ARCHITECTURE.md** - System design
- **DEVELOPER_REFERENCE.md** - API details

### Online Resources
- Django Docs: https://docs.djangoproject.com/
- Bootstrap CSS: https://getbootstrap.com/
- SQLite3: https://www.sqlite.org/
- Python: https://www.python.org/

### Common Commands

```bash
# Start server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Check for issues
python manage.py check

# Clear database
python manage.py flush

# Access Django shell
python manage.py shell

# Load sample data
python manage.py shell < populate_sample_data.py
```

---

## 📊 Data Models at a Glance

### Equipment (⚙️)
- Name, Type, Serial Number
- Location, Manufacturer
- Status, Warranty Info
- Maintenance dates

### MaintenanceRequest (📋)
- Equipment, Title, Description
- Priority, Status
- Assigned technician
- Due date, Hours estimated/actual

### MaintenanceTeam (👥)
- Name, Email, Phone
- Role, Specialization
- Employee ID, Hire date
- Active requests count

### User (👤)
- Username, Email, Password
- First/Last name
- Groups, Permissions
- Staff status

---

## 🔄 Workflow Summary

```
REQUEST LIFECYCLE:
1. User Creates Request (Pending)
   ↓
2. Manager Reviews & Assigns (Assigned)
   ↓
3. Technician Starts Work (In Progress)
   ↓
4. System Updates Equipment Status (Maintenance)
   ↓
5. Technician Finishes Work (Completed)
   ↓
6. System Updates:
   - Equipment status → Active
   - Last maintenance → Today
   - Hours calculated
   ↓
7. Request archived in Reports
```

---

## 💡 Pro Tips

1. **Use Filters**: Equipment page has status/type filters
2. **Check Workload**: Teams page shows technician capacity
3. **Review Calendar**: Plan maintenance using calendar view
4. **Monitor Metrics**: Reports show completion rates
5. **Bulk Actions**: Admin panel supports bulk operations
6. **Search**: Use admin search for quick lookup
7. **Export**: Admin panel has export options
8. **Mobile**: Fully responsive on smartphones

---

## ✅ Checklist for New Users

- [ ] Create account (signup)
- [ ] Verify email (if configured)
- [ ] Login to system
- [ ] Update profile
- [ ] Review dashboard
- [ ] Browse equipment list
- [ ] Check team roster
- [ ] Submit test request
- [ ] Review confirmation
- [ ] Check reports

---

## 🎓 Video Tutorial Topics (If Available)

1. User Registration & Login
2. Submitting Maintenance Requests
3. Viewing Equipment Inventory
4. Understanding Team Workload
5. Reading Reports & Analytics
6. Admin Panel Overview
7. Managing Maintenance Lifecycle
8. Generating Custom Reports

---

**GearGuard v1.0** - Quick Reference  
*For more info, see FINAL_PROJECT_SUMMARY.md*

Last Updated: December 27, 2025
