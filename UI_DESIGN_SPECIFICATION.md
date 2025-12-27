# GearGuard UI/UX Design Specification

## 🎨 Design Overview

### Color Scheme
```
Primary Blue:    #0D47A1
Secondary:       #1565C0
Success Green:   #43A047
Warning Orange:  #FB8C00
Danger Red:      #E53935
Light Gray:      #F5F5F5
Dark Gray:       #424242
White:           #FFFFFF
```

### Typography
- **Header Font**: Segoe UI, Arial (sans-serif)
- **Body Font**: Segoe UI, Arial (sans-serif)
- **Code Font**: Courier New, monospace

### Responsive Breakpoints
```
Mobile:    < 768px
Tablet:    768px - 1024px
Desktop:   > 1024px
```

---

## 📄 Page Wireframes & Components

### 1. Login/Authentication Page

**URL**: `/admin/login/` or `/login/`

**Elements**:
- GearGuard Logo (top center)
- Username/Email input field
- Password input field
- "Remember Me" checkbox
- "Forgot Password" link
- Login button (Primary Blue)
- Sign up link (optional)

**Layout**:
```
┌─────────────────────────────┐
│      GearGuard Logo         │
├─────────────────────────────┤
│                             │
│   Username: [_________]     │
│   Password: [_________]     │
│   ☐ Remember Me             │
│                             │
│   [    Login Button    ]    │
│   [Forgot Password]         │
│                             │
└─────────────────────────────┘
```

---

### 2. Dashboard/Home Page

**URL**: `/dashboard/`

**Key Elements**:
- **Navigation Bar**: Top horizontal menu
  - Logo/Home link
  - Dashboard
  - Equipment
  - Maintenance Requests
  - Team
  - Reports
  - User profile dropdown
  - Logout button

- **Sidebar**: Left navigation (optional, can be collapsible)
  - Dashboard
  - Equipment Management
  - Maintenance Requests
  - Team Management
  - Reports

- **Main Content Area**:
  - Welcome message
  - Quick stats cards
  - Recent activities
  - Charts/Graphs

**Stats Cards**:
```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Active     │  │  Pending     │  │  In Progress │  │  Completed   │
│   Equipment  │  │ Requests     │  │   Requests   │  │  This Month  │
│      45      │  │      12      │  │       8      │  │      23      │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘
```

**Layout**:
```
┌────────────────────────────────────────────┐
│ Logo  Dashboard  Equipment  Requests  Team │
├────────────────────────────────────────────┤
│                                            │
│ Welcome, Admin! | [Profile▼]  [Logout]    │
│                                            │
├─────────────────────────────────────────── │
│  Dashboard                                 │
│                                            │
│  Quick Stats:                              │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐     │
│  │ 45   │ │ 12   │ │  8   │ │ 23   │     │
│  │ Equip│ │Pend │ │InProg│ │ Done │     │
│  └──────┘ └──────┘ └──────┘ └──────┘     │
│                                            │
│  Recent Activities:                        │
│  • Compressor serviced - 2 hours ago      │
│  • New request created - 4 hours ago      │
│  • Team assigned - yesterday               │
│                                            │
└────────────────────────────────────────────┘
```

---

### 3. Equipment Management Page

**URL**: `/equipment/`

**Features**:

#### a) Equipment List View
```
┌─────────────────────────────────────────────┐
│ Equipment List                  [+ Add New]  │
├─────────────────────────────────────────────┤
│                                             │
│ Search: [_________________]  Filter [▼]    │
│                                             │
├─────────────────────────────────────────────┤
│ Name    │Type      │Location │Status │ Act.│
├─────────────────────────────────────────────┤
│Compressor│Mechanical│Bldg A   │Active │ ✎ ⋯ │
│Pump      │Hydraulic │Bldg B   │Maint. │ ✎ ⋯ │
│Generator │Electrical│Bldg C   │Inactive│ ✎ ⋯ │
│                                             │
│ < 1 2 3 4 5 >                              │
└─────────────────────────────────────────────┘
```

**Columns**:
- Equipment Name
- Type
- Serial Number
- Location
- Status (with color indicator)
- Last Maintenance
- Next Maintenance (due)
- Actions (Edit, Delete, View Details)

**Status Indicators**:
- 🟢 Active
- 🔴 Inactive
- 🟡 Under Maintenance

#### b) Equipment Detail View
```
┌─────────────────────────────────────────────┐
│ Equipment Details: Compressor      [Edit]   │
├─────────────────────────────────────────────┤
│                                             │
│ Basic Information:                          │
│ ┌─────────────────────────────────────────┐│
│ │ Name: Compressor Unit A                 ││
│ │ Type: Mechanical/Pneumatic              ││
│ │ Serial #: CPR-2024-001                  ││
│ │ Location: Building A, Floor 2           ││
│ │ Status: Active                          ││
│ │ Purchase Date: 01/15/2020               ││
│ │ Last Maintenance: 12/20/2025            ││
│ │ Next Maintenance: 01/20/2026            ││
│ └─────────────────────────────────────────┘│
│                                             │
│ Maintenance History:                        │
│ • 12/20/2025 - Regular Service             │
│ • 11/15/2025 - Repair                      │
│ • 10/10/2025 - Inspection                  │
│                                             │
│ [Back]  [Edit]  [Delete]  [New Request]   │
└─────────────────────────────────────────────┘
```

#### c) Equipment Form (Add/Edit)
```
┌─────────────────────────────────────────────┐
│ Add New Equipment              [Close]      │
├─────────────────────────────────────────────┤
│                                             │
│ Equipment Name: [_________________]         │
│ Description:    [_________________]         │
│ Equipment Type: [Dropdown▼]                 │
│ Serial Number:  [_________________]         │
│ Location:       [_________________]         │
│ Status:         [Active ▼]                  │
│ Purchase Date:  [Select Date ▼]             │
│ Warranty Until: [Select Date ▼]             │
│                                             │
│ [Cancel]  [Reset]  [Save]                  │
│                                             │
└─────────────────────────────────────────────┘
```

---

### 4. Maintenance Requests Page

**URL**: `/maintenance-requests/`

#### a) Requests List View
```
┌──────────────────────────────────────────────┐
│ Maintenance Requests           [+ New Request]│
├──────────────────────────────────────────────┤
│                                              │
│ Filter: Status [All▼]  Priority [All▼]  [⊗] │
│ Search: [_________________]                  │
│                                              │
├──────────────────────────────────────────────┤
│ ID │Equipment │Status  │Priority │Due Date │Act│
├──────────────────────────────────────────────┤
│#001│Compressor│Assigned│Urgent ⚠ │12/28   │ ✎ │
│#002│Pump      │Pending │High    │12/30   │ ✎ │
│#003│Generator │Completed│Medium │12/25   │ ✎ │
│                                              │
│ < 1 2 3 4 5 >                               │
└──────────────────────────────────────────────┘
```

**Status Colors**:
- 🟢 Pending (Light)
- 🟠 Assigned (Orange)
- 🔵 In Progress (Blue)
- ✓ Completed (Green)
- ✗ Cancelled (Red)

#### b) Maintenance Request Detail View
```
┌──────────────────────────────────────────────┐
│ Request #001 - Compressor Repair   [Edit]   │
├──────────────────────────────────────────────┤
│                                              │
│ Status: Assigned                            │
│                                              │
│ Equipment:     Compressor Unit A            │
│ Title:         Oil leak detected            │
│ Description:   Oil seeping from valve conn. │
│ Priority:      Urgent                       │
│ Requested By:  John Admin                   │
│ Requested On:  12/27/2025 10:30 AM          │
│                                              │
│ Assigned Team: Team B                       │
│ Assigned To:   Mike Johnson                 │
│ Due Date:      12/28/2025                   │
│                                              │
│ Timeline:                                    │
│ [12/27 10:30] Created by John               │
│ [12/27 14:00] Assigned to Team B            │
│ [12/27 15:30] In progress...                │
│                                              │
│ [Reassign] [Update Status] [Complete] [Cancel]│
│                                              │
└──────────────────────────────────────────────┘
```

#### c) New Request Form
```
┌──────────────────────────────────────────────┐
│ Create Maintenance Request      [Close]     │
├──────────────────────────────────────────────┤
│                                              │
│ Equipment: [Select Equipment ▼]              │
│ Title:     [_________________]               │
│ Description: [_________________________]    │
│             [_________________________]    │
│                                              │
│ Priority: [Select ▼]                        │
│           ○ Low  ○ Medium  ○ High ○ Urgent │
│                                              │
│ Estimated Duration: [_______] hours         │
│ Notes: [_________________________]          │
│        [_________________________]          │
│                                              │
│ [Cancel]  [Save as Draft]  [Submit]        │
│                                              │
└──────────────────────────────────────────────┘
```

---

### 5. Team Management Page

**URL**: `/team/`

#### a) Team Members List
```
┌──────────────────────────────────────────────┐
│ Maintenance Team              [+ Add Member] │
├──────────────────────────────────────────────┤
│                                              │
│ Search: [_________________]  Active [☑]     │
│                                              │
├──────────────────────────────────────────────┤
│ Name        │Role          │Specialization  │Act│
├──────────────────────────────────────────────┤
│John Smith   │Senior Tech   │Mechanical      │ ✎ │
│Jane Doe     │Tech 1        │Electrical      │ ✎ │
│Mike Johnson │Tech 2        │Hydraulic       │ ✎ │
│                                              │
│ < 1 2 3 >                                   │
└──────────────────────────────────────────────┘
```

#### b) Team Member Detail
```
┌──────────────────────────────────────────────┐
│ John Smith - Senior Technician     [Edit]   │
├──────────────────────────────────────────────┤
│                                              │
│ Profile:                                     │
│ Email: john.smith@gearguard.com              │
│ Phone: +1-555-123-4567                      │
│ Role: Senior Technician                     │
│ Specialization: Mechanical & Hydraulic      │
│ Status: Active ●                            │
│ Hire Date: 01/15/2020                       │
│                                              │
│ Current Assignments:                        │
│ • Request #001 - Compressor (In Progress)   │
│ • Request #005 - Pump (Pending)             │
│                                              │
│ Performance:                                 │
│ Completed Requests: 156                     │
│ Avg. Completion Time: 4.2 hours             │
│ Satisfaction Rating: 4.8/5.0                │
│                                              │
│ [Back]  [Edit]  [Deactivate]  [Delete]     │
│                                              │
└──────────────────────────────────────────────┘
```

---

### 6. Reports & Analytics Page

**URL**: `/reports/`

#### a) Reports Dashboard
```
┌──────────────────────────────────────────────┐
│ Reports & Analytics                         │
├──────────────────────────────────────────────┤
│                                              │
│ Date Range: [From: ____] [To: ____]  [Apply]│
│                                              │
│ Key Metrics:                                 │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│ │Total Req │ │Avg Time  │ │Team Load │    │
│ │   156    │ │ 4.2 hrs  │ │  85%     │    │
│ └──────────┘ └──────────┘ └──────────┘    │
│                                              │
│ Request Status Distribution:                 │
│ ┌──────────────────────────────────────┐   │
│ │ Completed: ████████████░░░░░░░ 75%   │   │
│ │ In Progress:░░░░░░░░░░░░░░░░░░░ 12%  │   │
│ │ Pending:   ░░░░░░░░░░░░░░░░░░░░░ 13% │   │
│ └──────────────────────────────────────┘   │
│                                              │
│ Equipment Utilization:                       │
│ [Pie Chart / Bar Chart]                    │
│                                              │
│ Team Performance:                            │
│ [Line Chart - Requests over time]           │
│                                              │
│ [Export PDF] [Export Excel] [Print]        │
│                                              │
└──────────────────────────────────────────────┘
```

---

### 7. User Profile Page

**URL**: `/profile/`

```
┌──────────────────────────────────────────────┐
│ User Profile                                │
├──────────────────────────────────────────────┤
│                                              │
│ Profile Picture: [Avatar]      [Change]    │
│                                              │
│ Full Name:        [_________________]       │
│ Email:            [_________________]       │
│ Username:         [_________________]       │
│ Department:       [_________________]       │
│ Role:             [Admin ▼]                 │
│                                              │
│ Security:                                    │
│ Password:         [••••••••]  [Change]      │
│ Two-Factor Auth:  [☐ Enable]                │
│ Last Login:       12/27/2025 09:15 AM       │
│                                              │
│ [Cancel]  [Save Changes]                   │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 🎯 UI Components

### Buttons
```
Primary Button:    [Blue background, white text]
Secondary Button:  [Light gray, blue text]
Danger Button:     [Red background, white text]
Success Button:    [Green background, white text]
Ghost Button:      [Transparent, colored border]
Disabled Button:   [Gray background, gray text]
```

### Forms
```
Text Input:        Single-line text field
Text Area:         Multi-line text field
Select Dropdown:   List selection
Date Picker:       Calendar selector
Checkbox:          Multiple selections
Radio Button:      Single selection
Toggle Switch:     On/Off state
```

### Alerts & Notifications
```
Success Alert:     Green background + checkmark
Error Alert:       Red background + X icon
Warning Alert:     Orange background + ! icon
Info Alert:        Blue background + i icon
Toast Message:     Auto-dismissing notification
```

### Tables
```
Header Row:        Darker background
Zebra Striping:    Alternating row colors
Hover Effect:      Slight highlight on row hover
Pagination:        Page numbers at bottom
Sort Indicators:   ↑↓ arrows on headers
```

---

## 📱 Responsive Design

### Mobile Layout (< 768px)
- Single column layout
- Collapsible navigation menu (hamburger)
- Stacked form fields
- Full-width buttons
- Simplified tables (cards view)

### Tablet Layout (768px - 1024px)
- Two column layout
- Sidebar navigation (can collapse)
- Side-by-side form fields (where appropriate)
- Compressed tables

### Desktop Layout (> 1024px)
- Full layout
- Visible sidebar
- Multi-column layouts
- Full tables with all columns

---

## 🎨 Accessibility Features

- High contrast text (WCAG AA)
- Alt text for all images
- Keyboard navigation support
- ARIA labels for screen readers
- Focus indicators on interactive elements
- Skip to main content link
- Proper heading hierarchy (H1 > H2 > H3)
- Form labels associated with inputs

---

## 📋 File Structure for Templates

```
templates/
├── base.html                    # Main template
├── navbar.html                  # Navigation
├── sidebar.html                 # Sidebar
├── auth/
│   ├── login.html               # Login page
│   ├── logout.html              # Logout confirmation
│   └── register.html            # Registration (optional)
├── dashboard/
│   └── index.html               # Dashboard
├── equipment/
│   ├── list.html                # Equipment list
│   ├── detail.html              # Equipment detail
│   ├── form.html                # Add/Edit form
│   └── delete.html              # Delete confirmation
├── maintenance/
│   ├── request_list.html        # Requests list
│   ├── request_detail.html      # Request detail
│   ├── request_form.html        # Create/Edit
│   └── request_delete.html      # Delete confirmation
├── team/
│   ├── list.html                # Team members list
│   ├── detail.html              # Member detail
│   ├── form.html                # Add/Edit member
│   └── delete.html              # Delete confirmation
├── reports/
│   ├── dashboard.html           # Reports dashboard
│   ├── equipment_report.html    # Equipment report
│   ├── request_report.html      # Requests report
│   └── team_report.html         # Team report
├── profile/
│   └── profile.html             # User profile
└── error/
    ├── 404.html                 # Page not found
    └── 500.html                 # Server error
```

---

## 🎬 User Interactions

### Creating Equipment
1. Click "+ Add New" button
2. Fill in form fields
3. Click "Save"
4. Confirmation message
5. Redirect to equipment list

### Creating Maintenance Request
1. Click "+ New Request"
2. Select equipment
3. Fill in details
4. Assign to team member (optional)
5. Set priority
6. Submit
7. Notification sent to assigned team

### Completing Request
1. Click on request
2. Click "Update Status"
3. Select "Completed"
4. Add completion notes
5. Save
6. System updates equipment's "last_maintenance" date

---

## 🔄 Workflow States

```
Equipment Lifecycle:
New → Active → Maintenance → Active → Inactive

Request Lifecycle:
Created → Pending → Assigned → In Progress → Completed
                           ↓
                      Cancelled
```

---

**Design Version**: 1.0.0
**Last Updated**: December 27, 2025
