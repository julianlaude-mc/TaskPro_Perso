================================================================================
                    DOST PROJECT MANAGEMENT SYSTEM
                         User Guide & Documentation
================================================================================

TABLE OF CONTENTS
-----------------
0. What's New (April 2026)
1. System Overview
2. Getting Started
3. User Roles & Permissions
4. Module Guide
   4.1 Dashboard
   4.2 User Management
   4.3 Budget Management
   4.4 Proposal Management
   4.5 Project Management
   4.6 Task Management
   4.7 Extension Requests
   4.8 Reports & Analytics
   4.9 Communication Hub
   4.10 Forms Management
   4.11 Audit Logs
   4.12 Settings
5. DOST Compliance Features
6. Technical Requirements
7. Installation & Setup
8. Troubleshooting
9. Contact & Support

================================================================================
0. WHAT'S NEW (APRIL 2026)
================================================================================

LATEST UI/UX AND RELIABILITY IMPROVEMENTS
-----------------------------------------
• Real-time notifications across Administrator, Staff, Proponent, and
   Beneficiary modules using a live server stream with automatic polling fallback.

• Enhanced quick action hubs for Administrator and Staff:
   - Color-coded action cards per function
   - Stronger hover/press states and visual click affordance
   - Improved CTA readability for faster navigation

• Dark mode consistency improvements across role modules:
   - Persistent theme state while switching modules/pages
   - Better contrast and visual hierarchy for cards, filters, and sidebar elements

• Admin simple-mode rendering improvements:
   - Reduced visual flash on GIS refresh/module navigation
   - Better sidebar logo visibility and improved active-state aesthetics

• Project milestone validation hardening:
   - Robust server-side date parsing and validation
   - Safer handling for invalid milestone dates/progress values
   - UI date input constraints to minimize invalid submissions

SETUP / ENVIRONMENT NOTES
-------------------------
• No additional Python package is required for the above updates.
• No settings.py configuration change is required for local development.
• Existing virtual environment setup remains valid.

================================================================================
1. SYSTEM OVERVIEW
================================================================================

The DOST Project Management System is a comprehensive web-based application 
designed for the Department of Science and Technology (DOST) to manage:

• Technology transfer projects (SETUP Program)
• Budget allocation and equipment delivery tracking
• Proposal submission and approval workflows
• Task assignment and monitoring
• Beneficiary Technology Needs Assessment (TNA)
• Equipment ownership and property tag management
• Multi-stakeholder communication

The system supports 4 user roles with role-based access control:
- Administrator (Full system access)
- DOST Staff (Project management and oversight)
- Proponent (Proposal submission and project execution)
- Beneficiary (Project tracking and equipment receiving)

================================================================================
2. GETTING STARTED
================================================================================

ACCESSING THE SYSTEM
--------------------
1. Open your web browser (Chrome, Firefox, Edge recommended)
2. Navigate to: http://localhost:8000 (or your deployed URL)
3. Enter your email address and password
4. Click "Login"

FIRST-TIME LOGIN
----------------
• Default admin credentials are provided by your system administrator
• You will be redirected to your role-specific dashboard after login
• Update your password in Settings for security

NAVIGATION
----------
• Use the left sidebar menu to access different modules
• The top bar shows your profile, notifications, and quick actions
• Click on your profile picture (top-right) to access settings or logout

================================================================================
3. USER ROLES & PERMISSIONS
================================================================================

ADMINISTRATOR
-------------
Full access to all system features:
✓ Manage all users (create, edit, delete, activate/deactivate)
✓ Manage budgets and fund allocations
✓ Approve/reject proposals
✓ Create and manage projects
✓ Assign tasks to any user
✓ View all reports and audit logs
✓ Manage form templates
✓ System settings and configurations

DOST STAFF
----------
Project oversight and management:
✓ View all users (read-only)
✓ View budgets
✓ View and process proposals (review, recommend)
✓ Manage projects assigned to them
✓ Create and manage tasks
✓ View reports
✓ Communicate with proponents/beneficiaries

PROPONENT
---------
Project execution and proposal submission:
✓ Submit new proposals
✓ View and update own proposals
✓ View projects assigned to them
✓ View and update assigned tasks
✓ Submit extension requests
✓ View own activity reports
✓ Communicate with staff/admin

BENEFICIARY
-----------
Project tracking and equipment receiving:
✓ View projects assigned to them
✓ Track equipment deliveries
✓ Update TNA (Technology Needs Assessment) status
✓ View own activity reports
✓ Communicate with project team

================================================================================
4. MODULE GUIDE
================================================================================

4.1 DASHBOARD
-------------
The dashboard provides an at-a-glance overview:

• Quick Stats Cards: Total users, proposals, projects, pending extensions
• GIS Map: Interactive map showing project locations in Biliran
• Charts: Project status, task completion, user demographics
• Summary Cards: Equipment value allocated/delivered, delivery rate

Using the GIS Map:
- Click on markers to view project details
- Use the layer control to filter by project status
- Click anywhere on the map to find nearest projects
- Toggle between OpenStreetMap and Satellite views

-------------------------------------------------------------------------------

4.2 USER MANAGEMENT (Administrator Only)
----------------------------------------
Navigate to: Sidebar → Users

ADDING A NEW USER:
1. Click "Add User" button
2. Fill in required fields:
   - Email (used as username)
   - First Name, Last Name
   - Password (min 8 characters, must include uppercase, lowercase, number)
   - Role (Administrator, Staff, Proponent, Beneficiary)
3. Optional: Add profile picture, contact number, address
4. Click "Save"

EDITING A USER:
1. Click the "Edit" button on the user's row
2. Modify the necessary fields
3. Leave password blank to keep existing password
4. Click "Update"

DEACTIVATING A USER:
1. Click "Edit" on the user's row
2. Change Status to "Inactive"
3. Click "Update"
Note: Inactive users cannot login but their data is preserved.

MASS DELETE:
1. Check the boxes next to users you want to delete
2. Click "Delete Selected" button
3. Confirm the deletion

-------------------------------------------------------------------------------

4.3 BUDGET MANAGEMENT
---------------------
Navigate to: Sidebar → Budgets

CREATING A BUDGET:
1. Click "Add Budget" button
2. Enter:
   - Fiscal Year (e.g., 2026)
   - Fund Source (e.g., "DOST SETUP", "GAA")
   - Total Equipment Value (total allocation amount)
   - Upload supporting budget document (optional)
3. Click "Save"

VIEWING BUDGET DETAILS:
- Each budget card shows: fiscal year, fund source, allocated/remaining amounts
- Progress bar shows utilization percentage
- Click "View Allocations" to see detailed breakdown

BUDGET ALLOCATION WORKFLOW:
1. Budget is created with total amount
2. When proposals are approved, amounts are allocated
3. When equipment is delivered, delivered value is updated
4. Status changes to "Exhausted" when fully allocated

-------------------------------------------------------------------------------

4.4 PROPOSAL MANAGEMENT
-----------------------
Navigate to: Sidebar → Proposals

SUBMITTING A PROPOSAL (Proponent):
1. Click "Add Proposal" button
2. Fill in:
   - Title (descriptive project name)
   - Description (detailed project description)
   - Proposed Amount (requested funding)
   - Select Budget (fund source)
   - Location (municipality, province)
   - Upload supporting document
3. Click "Submit"

PROPOSAL STATUS FLOW:
Pending → For Review → Approved/Rejected/Needs Revision

APPROVING A PROPOSAL (Administrator):
1. Click "Approve" on the proposal
2. Enter:
   - Approved Amount (may differ from proposed)
   - Assign Budget
   - Set Project Start and End Dates
3. Click "Approve"
Note: An approved proposal automatically creates a new Project.

DECLINING A PROPOSAL:
1. Click "Decline" on the proposal
2. Enter rejection reason (required)
3. Click "Confirm Decline"

-------------------------------------------------------------------------------

4.5 PROJECT MANAGEMENT
----------------------
Navigate to: Sidebar → Projects

VIEWING PROJECTS:
- Grid view shows project cards with key info
- Click on a project card for detailed view
- Use filters to narrow down by status, municipality, year

PROJECT STATUS:
- New: Recently created from approved proposal
- Ongoing: Active project in execution
- Completed: All deliverables met
- Terminated: Project cancelled/stopped

RECORDING EQUIPMENT DELIVERY:
1. Open project detail page
2. Click "Record Delivery" button
3. Enter:
   - Equipment Name
   - Category
   - Quantity
   - Property Tag Number (DOST requirement)
   - Serial Numbers
   - Delivery Date
   - Received By
4. Click "Save Delivery"

MARKING PROJECT AS COMPLETED:
1. Ensure all equipment is delivered
2. Click "Mark as Completed" button
3. Confirm the action

-------------------------------------------------------------------------------

4.6 TASK MANAGEMENT
-------------------
Navigate to: Sidebar → Tasks

CREATING A TASK:
1. Click "Add Task" button
2. Enter:
   - Task Title
   - Description
   - Assign to (select user)
   - Project (link to project)
   - Priority (Low, Medium, High, Urgent)
   - Due Date
3. Click "Save"

TASK STATUS:
- Pending: Not started
- In Progress: Currently being worked on
- Completed: Task finished
- Overdue: Past due date and not completed

UPDATING TASK STATUS:
1. Click on the task
2. Click status dropdown
3. Select new status
4. Add comments if needed

TASK CHECKLIST:
1. Open task detail
2. Add checklist items in the checklist section
3. Check items as they're completed
4. Progress percentage updates automatically

-------------------------------------------------------------------------------

4.7 EXTENSION REQUESTS
----------------------
Navigate to: Sidebar → Extension Requests

REQUESTING AN EXTENSION (Proponent):
1. Click "Request Extension"
2. Select the Project/Proposal
3. Enter:
   - Requested Days (extension period)
   - Reason/Justification
   - Upload supporting document (optional)
4. Click "Submit"

APPROVING EXTENSIONS (Administrator):
1. Review the extension request
2. Click "Approve" or "Reject"
3. If approving, confirm the approved days
4. If rejecting, provide rejection reason

BULK OPERATIONS:
1. Check multiple pending requests
2. Click "Approve Selected" or "Reject Selected"
3. Enter common reason/days
4. Confirm action

-------------------------------------------------------------------------------

4.8 REPORTS & ANALYTICS
-----------------------
Navigate to: Sidebar → Reports

FILTERING REPORTS:
1. Click "Show Filters" button
2. Select:
   - Year
   - Municipality
   - Date Range
   - Status
3. Click "Apply Filters"
4. Click "Clear Filters" to reset

EXPORTING REPORTS:

Excel Export:
1. Click "Export Excel" dropdown
2. Select report type:
   - Master Report (all data)
   - Projects only
   - Proposals only
   - Budgets only
   - Tasks only

PDF Export:
1. Click "Export PDF" button
2. Select sections to include:
   - Summary Statistics
   - Equipment Allocations
   - Projects List
   - Proposals List
   - TNA Summary
3. Click "Generate PDF"

Print Report:
1. Click "Print" button
2. Select printer or Save as PDF
3. Adjust print settings as needed

-------------------------------------------------------------------------------

4.9 COMMUNICATION HUB
---------------------
Navigate to: Sidebar → Messages or Group Chats

DIRECT MESSAGES:
1. Click "Messages" in sidebar
2. Click "New Message" or select existing conversation
3. Type message and press Enter or click Send
4. Attach files using the attachment button

GROUP CHATS:
1. Click "Group Chats" in sidebar
2. Click "Create Group Chat" (Admin/Staff only)
3. Enter group name and description
4. Add members from the user list
5. Link to a project (optional)
6. Click "Create"

Note: Proponents and Beneficiaries can participate in group chats 
but cannot create them.

-------------------------------------------------------------------------------

4.10 FORMS MANAGEMENT (Administrator Only)
------------------------------------------
Navigate to: Sidebar → Forms

CREATING A FORM TEMPLATE:
1. Click "Add Form"
2. Enter:
   - Form Name
   - Description
   - Category
   - Upload template file (PDF, DOCX)
3. Click "Save"

FORM SUBMISSIONS:
- Users can fill out forms online
- Submissions are stored and can be reviewed
- Export submissions to PDF/Excel

-------------------------------------------------------------------------------

4.11 AUDIT LOGS
---------------
Navigate to: Sidebar → Audit Logs

The audit log tracks all system activities:
- User logins/logouts
- Create/Update/Delete operations
- Approvals and rejections
- Status changes

VIEWING LOG DETAILS:
1. Click "View Details" on any log entry
2. Modal shows:
   - User who performed action
   - Timestamp
   - Action type
   - Previous data (for updates)
   - New data (for updates)
   - IP Address

FILTERING LOGS:
- Use the search box to filter by user or action
- Sort by clicking column headers
- Pagination controls at bottom

-------------------------------------------------------------------------------

4.12 SETTINGS
-------------
Navigate to: Profile dropdown → Settings

PROFILE SETTINGS:
- Update profile picture
- Edit personal information
- Change contact details

CHANGE PASSWORD:
1. Click "Change Password"
2. Enter current password
3. Enter new password (twice)
4. Click "Update Password"

Password Requirements:
- Minimum 8 characters
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 number

================================================================================
5. DOST COMPLIANCE FEATURES
================================================================================

TECHNOLOGY NEEDS ASSESSMENT (TNA)
---------------------------------
• Tracks beneficiary's technology adoption status
• Status levels: Not Started, In Progress, Completed, Expired
• Completion date tracking for compliance reporting

EQUIPMENT OWNERSHIP TRACKING
----------------------------
• All equipment starts as "DOST Owned"
• After 5 years, equipment becomes eligible for transfer
• Transfer requires formal documentation and approval
• Property tag numbers are mandatory for all equipment

TRANCHE RELEASE MONITORING
--------------------------
• Track fund releases by tranche (1st, 2nd, Final)
• Record release dates and amounts
• Monitor liquidation requirements
• Flag overdue liquidations

PROPERTY TAG MANAGEMENT
-----------------------
• Unique property tags for all DOST-funded equipment
• Serial number tracking
• Delivery documentation with receipts
• Condition monitoring

================================================================================
6. TECHNICAL REQUIREMENTS
================================================================================

BROWSER REQUIREMENTS:
- Google Chrome 90+ (Recommended)
- Mozilla Firefox 88+
- Microsoft Edge 90+
- Safari 14+

SCREEN RESOLUTION:
- Minimum: 1024 x 768
- Recommended: 1920 x 1080

INTERNET CONNECTION:
- Stable internet connection required
- Minimum 1 Mbps for basic operations
- 5 Mbps+ recommended for file uploads

FILE UPLOAD LIMITS:
- Maximum file size: 10 MB
- Supported formats: PDF, DOC, DOCX, XLS, XLSX, JPG, PNG
- Profile pictures: JPG, PNG (max 5 MB)

================================================================================
7. INSTALLATION & SETUP (For Administrators)
================================================================================

PREREQUISITES:
- Python 3.9 or higher
- pip (Python package manager)
- SQLite (included) or PostgreSQL/MySQL for production

INSTALLATION STEPS:

1. Clone or download the project:
   cd /path/to/DOST/myproject

2. Create virtual environment:
   python -m venv myenv

3. Activate virtual environment:
   # Windows:
   myenv\Scripts\activate
   
   # macOS/Linux:
   source myenv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Configure environment variables (required for AI assistant):
   Create a .env file in the project root (same level as manage.py) and add:
   GOOGLE_API_KEY=your_api_key_here
   GOOGLE_GENAI_MODEL=gemini-2.0-flash

6. Run database migrations:
   python manage.py migrate

7. Create superuser (admin account):
   python manage.py createsuperuser

8. Collect static files (for production):
   python manage.py collectstatic

9. Run development server:
   python manage.py runserver

10. Access the system:
   Open browser and go to http://127.0.0.1:8000

PRODUCTION DEPLOYMENT:
- Use a production-ready web server (Nginx, Apache)
- Use Gunicorn or uWSGI as the application server
- Configure HTTPS with SSL certificate
- Set DEBUG=False in settings.py
- Use PostgreSQL or MySQL for production database
- Configure proper backup procedures

================================================================================
8. TROUBLESHOOTING
================================================================================

COMMON ISSUES:

Problem: Cannot login
Solutions:
- Verify email and password are correct
- Check if account is active (not deactivated)
- Clear browser cache and cookies
- Try incognito/private browsing mode

Problem: File upload fails
Solutions:
- Check file size (max 10 MB)
- Verify file format is supported
- Try a different browser
- Check internet connection stability

Problem: Charts not loading
Solutions:
- Refresh the page
- Clear browser cache
- Check if JavaScript is enabled
- Try a different browser

Problem: Export not downloading
Solutions:
- Check popup blocker settings
- Allow downloads from the site
- Check available disk space
- Try a different browser

Problem: Map not displaying
Solutions:
- Check internet connection (maps require online access)
- Verify browser location permissions
- Clear browser cache
- Try a different browser

Problem: Session expired unexpectedly
Solutions:
- This is a security feature after inactivity
- Login again to continue working
- Save work frequently

ERROR MESSAGES:

"Access Denied"
- You don't have permission for this action
- Contact administrator if you need access

"Insufficient Budget"
- The selected budget doesn't have enough funds
- Choose a different budget or reduce amount

"Validation Error"
- Required fields are missing or invalid
- Check all fields and try again

"File Too Large"
- The uploaded file exceeds the size limit
- Compress the file and try again

================================================================================
9. CONTACT & SUPPORT
================================================================================

For technical support or system issues:
- Contact your System Administrator
- Email: [Your IT Support Email]
- Phone: [Your IT Support Phone]

For training and user guides:
- Access the Help section in the system
- Contact your Department Head

For feature requests or feedback:
- Submit through the system's feedback form
- Email: [Feedback Email]

================================================================================
                           END OF USER GUIDE
================================================================================

Version: 1.0
Last Updated: January 2026
System: DOST Project Management System
Developed for: DOST Biliran Province

================================================================================
