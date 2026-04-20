# TaskPro - DOST Project Management System
## User Manual

### Version 1.1
### Department of Science and Technology - Biliran Province
### April 2026

---

## Table of Contents

1. [Introduction](#introduction)
2. [What's New in v1.1 (April 2026)](#whats-new-in-v11-april-2026)
3. [Getting Started](#getting-started)
4. [User Roles and Permissions](#user-roles-and-permissions)
5. [Administrator Guide](#administrator-guide)
6. [DOST Staff Guide](#dost-staff-guide)
7. [Proponent Guide](#proponent-guide)
8. [Beneficiary Guide](#beneficiary-guide)
9. [Common Features](#common-features)
10. [Troubleshooting](#troubleshooting)
11. [Contact Support](#contact-support)

---

## Introduction

TaskPro is a comprehensive web-based project management system designed specifically for the Department of Science and Technology (DOST) in Biliran Province. The system streamlines the management of technology transfer projects, from proposal submission to equipment delivery and project completion.

### Key Features
- **Multi-role user management** with role-based access control
- **Interactive GIS mapping** for project location tracking
- **Budget and financial management**
- **Proposal approval workflows**
- **Task assignment and monitoring**
- **Real-time notifications and communication**
- **Comprehensive reporting and analytics**
- **Document management and audit trails**

---

## What's New in v1.1 (April 2026)

### 1. Real-Time Notifications
- Notifications now update in near real-time across Administrator, Staff, Proponent, and Beneficiary modules.
- The system now uses a live notification stream with automatic fallback polling for reliability.
- Users should see unread badge and dropdown updates faster without waiting for long polling intervals.

### 2. Enhanced Quick Action Hubs
- Administrator and Staff Quick Actions were redesigned to look and behave like interactive action buttons.
- Cards now use role-appropriate color accents, stronger hover states, and clearer click cues.
- This improves visual hierarchy and speeds up frequent navigation workflows.

### 3. Dark Mode Consistency Improvements
- Theme persistence was standardized to reduce dark-mode resets when moving across modules.
- Contrast and readability were improved for cards, sidebar surfaces, filters, and active elements.

### 4. Milestone Input Reliability Improvements
- Project milestone add/update flows now include stronger date and progress validation.
- Invalid date values are handled safely with user-facing feedback instead of server errors.
- Planned date inputs include better constraints to reduce invalid entries.

### 5. Configuration and Environment Impact
- No new package installation is required for these updates.
- No additional `settings.py` changes are required for local development.
- Existing virtual environment setup remains supported.

---

## Getting Started

### System Access

1. **Open your web browser** (Chrome, Firefox, or Edge recommended)
2. **Navigate to the system URL** provided by your administrator
3. **Enter your credentials**:
   - **Username/Email**: Your assigned email address
   - **Password**: Your assigned password
4. **Click "Login"**

### First-Time Login

- After successful login, you'll be redirected to your role-specific dashboard
- **Important**: Change your password immediately for security
- Familiarize yourself with the navigation menu on the left sidebar

### Navigation Basics

- **Left Sidebar**: Main navigation menu
- **Top Bar**: User profile, notifications, and quick actions
- **Dashboard**: Overview of key metrics and activities
- **Profile Menu** (top-right): Settings, password change, logout

---

## User Roles and Permissions

### Administrator
**Full system access and control**
- User management (create, edit, delete users)
- Budget allocation and management
- Proposal approval/rejection
- Project creation and oversight
- Task assignment and monitoring
- System configuration and settings
- Audit log access
- Form template management

### DOST Staff (PSTO)
**Project oversight and technical management**
- View user information (read-only)
- Review and process proposals
- Project management and monitoring
- Task creation and assignment
- Report generation
- Communication with proponents and beneficiaries

### Proponent
**Project execution and proposal submission**
- Submit new project proposals
- View and update own proposals
- Manage assigned projects
- Task completion and updates
- Submit extension requests
- Communication with DOST staff

### Beneficiary
**Project tracking and equipment management**
- View assigned projects
- Track equipment delivery status
- Update TNA (Technology Needs Assessment) status
- Equipment receipt confirmation
- Communication with project team

---

## Administrator Guide

### 1. Dashboard Overview

After login, you'll see the main dashboard with:
- **Quick Statistics**: Total users, proposals, projects, pending tasks
- **GIS Map**: Interactive map showing all project locations
- **Charts**: Project status distribution, task completion rates
- **Recent Activities**: Latest system activities and notifications

### 2. Managing Users

#### Adding a New User
1. Navigate to **Users** in the sidebar
2. Click **"Add User"** button
3. Fill in the required information:
   - **Email**: User's email address (used as username)
   - **First Name** and **Last Name**
   - **Role**: Select from dropdown (admin, dost_staff, proponent, beneficiary)
   - **Address** and **Contact Number**
   - **Password**: Set initial password
4. Click **"Save"**

#### Editing User Information
1. Go to **Users** → Find the user in the list
2. Click the **"Edit"** (pencil) icon
3. Update the information as needed
4. Click **"Save Changes"**

#### Deactivating/Reactivating Users
1. In the Users list, find the user
2. Click the **"Deactivate"** or **"Activate"** button
3. Confirm the action

### 3. Budget Management

#### Creating a Budget
1. Navigate to **Budgets** in the sidebar
2. Click **"Add Budget"**
3. Enter budget details:
   - **Fiscal Year**: Select year
   - **Fund Source**: Description of funding source
   - **Total Equipment Value**: Budget amount
   - **Date Allocated**: When funds were allocated
4. Click **"Save"**

#### Managing Budget Allocations
- View budget utilization in the budget list
- Track delivered vs. allocated amounts
- Generate budget reports

### 4. Proposal Management

#### Reviewing Proposals
1. Go to **Proposals** in the sidebar
2. Review the proposal list with status indicators
3. Click on a proposal to view details

#### Approving a Proposal
1. Open the proposal details
2. Review all information and attached documents
3. Click **"Approve"** if satisfactory
4. Select appropriate budget allocation
5. Add approval remarks if needed

#### Rejecting a Proposal
1. Open the proposal details
2. Click **"Reject"**
3. Provide detailed rejection reasons
4. Click **"Submit"**

### 5. Project Management

#### Creating a Project from Approved Proposal
1. Navigate to **Projects**
2. Click **"Add Project"**
3. Select an **approved proposal** from dropdown
4. Fill in project details:
   - Project code (auto-generated)
   - Timeline and budget allocation
   - Beneficiary information
   - Technology details
5. Click **"Save"**

#### Monitoring Project Progress
- View project status in the projects list
- Click on projects to see detailed information
- Track completion percentages and timelines

### 6. Task Management

#### Creating Tasks
1. Go to **Tasks** in the sidebar
2. Click **"Create Task"**
3. Fill in task details:
   - **Title**: Clear, descriptive title
   - **Description**: Detailed task requirements
   - **Assigned To**: Select user from dropdown
   - **Due Date**: Set deadline
   - **Project**: Link to relevant project
   - **Location**: Task location coordinates
4. Click **"Save"**

#### Monitoring Task Completion
- View task status in the task list
- Update task status as work progresses
- Reassign tasks if needed

### 7. Reports and Analytics

#### Generating Reports
1. Navigate to **Reports**
2. Select report type:
   - **Project Reports**: Status, completion, budget utilization
   - **User Reports**: Activity summaries, role distribution
   - **Budget Reports**: Allocation and expenditure tracking
   - **Proposal Reports**: Submission and approval statistics
3. Set date ranges and filters
4. Click **"Generate Report"**
5. Export as PDF or Excel

### 8. System Settings

#### Managing Form Templates
1. Go to **Forms** in the sidebar
2. Upload new form templates
3. Edit existing templates
4. Set form requirements for different proposal types

#### Audit Logs
- Access **Audit Logs** to view system activity
- Filter by date, user, or action type
- Export audit reports for compliance

---

## DOST Staff Guide

### 1. Daily Workflow

#### Morning Routine
1. **Check Dashboard** for new notifications and pending tasks
2. **Review New Proposals** submitted overnight
3. **Check Task Updates** from proponents
4. **Monitor Project Progress** and deadlines

#### Processing Proposals
1. Navigate to **Proposals**
2. Filter by status: "For Review"
3. Open each proposal and review:
   - Technical feasibility
   - Budget requirements
   - Beneficiary needs
   - Documentation completeness
4. Provide recommendations or request additional information

#### Task Management
1. Go to **Tasks**
2. Create new tasks for approved projects
3. Assign tasks to appropriate proponents
4. Monitor task completion and follow up on overdue items

### 2. Communication

#### Sending Notifications
1. Use the **Communication Hub** to send messages
2. Select recipients (individual users or groups)
3. Choose notification type (email, in-system message)
4. Include clear instructions and deadlines

#### Responding to Inquiries
- Check notifications regularly
- Respond promptly to proponent and beneficiary questions
- Escalate complex issues to administrators

### 3. Field Work Coordination

#### Planning Site Visits
1. Create tasks for site inspections
2. Coordinate with proponents for scheduling
3. Prepare necessary checklists and forms
4. Document visit findings and recommendations

---

## Proponent Guide

### 1. Proposal Submission

#### Creating a New Proposal
1. Navigate to **Proposals** → **"Submit Proposal"**
2. Fill in proposal details:
   - **Title**: Clear, descriptive title
   - **Description**: Detailed project description
   - **Proposed Amount**: Requested budget
   - **Beneficiaries**: Target community/group
   - **Location**: Specific barangay and municipality
   - **Technology Type**: Equipment or technology needed
3. Upload supporting documents:
   - Community profile
   - Technical specifications
   - Budget breakdown
   - Endorsement letters
4. Click **"Submit"**

#### Tracking Proposal Status
- View proposal status in your dashboard
- Check for review comments and requirements
- Update proposal information if requested
- Receive notifications when status changes

### 2. Project Execution

#### Managing Assigned Projects
1. Go to **Projects** to see your assigned projects
2. Click on a project to view details and requirements
3. Update project information as work progresses
4. Report milestone achievements

#### Task Completion
1. Navigate to **Tasks**
2. View tasks assigned to you
3. Update task status regularly:
   - **Pending**: Not started
   - **In Progress**: Work has begun
   - **Completed**: Task finished
4. Add notes and documentation for completed tasks

### 3. Extension Requests

#### Requesting Project Extensions
1. Open the project that needs extension
2. Click **"Request Extension"**
3. Provide detailed justification:
   - Reasons for delay
   - Additional time needed
   - Impact on beneficiaries
   - Mitigation plans
4. Submit with supporting documentation

---

## Beneficiary Guide

### 1. Accessing Your Projects

#### Viewing Assigned Projects
1. After login, your dashboard shows assigned projects
2. Click **"View Details"** on any project card
3. Review project information:
   - Project description and objectives
   - Timeline and milestones
   - Equipment to be received
   - Contact information for project team

#### Tracking Equipment Delivery
1. Go to your project details
2. Check the **"Equipment Status"** section
3. View delivery schedule and tracking information
4. Confirm receipt when equipment arrives

### 2. TNA (Technology Needs Assessment)

#### Updating TNA Status
1. Navigate to **My Profile** or project details
2. Find the **TNA Status** section
3. Update your current status:
   - **TNA Not Started**: Initial assessment pending
   - **TNA In Progress**: Assessment underway
   - **Equipment Selection**: Choosing appropriate technology
   - **Under Procurement**: Equipment being purchased
   - **Delivery Pending**: Equipment on the way
   - **Delivered**: Equipment received
   - **Operational**: Equipment in use
4. Add notes about your progress or needs

### 3. Communication

#### Contacting Project Team
1. Use the **Messages** section in your dashboard
2. Send questions or updates to DOST staff and proponents
3. Report issues with equipment or project implementation
4. Request additional training or support

---

## Common Features

### 1. Dashboard Usage

#### Understanding Dashboard Widgets
- **Statistics Cards**: Quick overview of key metrics
- **GIS Map**: Visual representation of project locations
- **Charts**: Graphical representation of data
- **Notifications**: Recent system messages and alerts

#### Customizing Your Dashboard
- Most dashboards are role-specific and show relevant information
- Use filters and date ranges to focus on specific data
- Export charts and reports as needed

### 2. File Management

#### Uploading Documents
1. Look for **"Upload"** or **"Attach Files"** buttons
2. Supported formats: PDF, DOC, DOCX, XLS, XLSX, JPG, PNG
3. Maximum file size: Check system limits with administrator
4. Add descriptive filenames

#### Downloading Files
1. Click on document links in project or proposal details
2. Files open in new browser tabs
3. Right-click to save files locally

### 3. Search and Filtering

#### Using Search Functions
- Most list views have search boxes
- Search by keywords, names, or IDs
- Use advanced filters for more specific results

#### Filtering Data
- Use dropdown filters for status, date ranges, locations
- Combine multiple filters for precise results
- Save filter preferences where available

### 4. Notifications

#### Managing Notifications
1. Click the bell icon in the top navigation
2. View unread notifications
3. Mark as read or delete unwanted notifications
4. Click on notifications to go to relevant pages

#### Notification Types
- **System Alerts**: Important system messages
- **Task Assignments**: New tasks assigned to you
- **Status Updates**: Changes in proposals or projects
- **Deadline Reminders**: Upcoming due dates
- **Messages**: Direct communications from other users

### 5. Profile Management

#### Updating Your Profile
1. Click your profile picture in the top-right corner
2. Select **"Profile Settings"**
3. Update personal information:
   - Contact details
   - Address information
   - Profile picture
4. Click **"Save Changes"**

#### Changing Password
1. Go to **Settings** → **"Change Password"**
2. Enter current password
3. Enter new password twice for confirmation
4. Click **"Update Password"**

---

## Troubleshooting

### Login Issues

#### Forgot Password
- Contact your system administrator
- Provide your email address for password reset
- Temporary password will be provided

#### Account Locked
- Contact administrator to unlock your account
- Verify account status and permissions

### System Performance

#### Slow Loading
- Clear browser cache and cookies
- Try a different browser
- Check internet connection
- Contact IT support if persistent

#### Error Messages
- Note the exact error message
- Take screenshot if possible
- Report to system administrator with steps to reproduce

### File Upload Issues

#### Upload Failures
- Check file size limits
- Verify supported file formats
- Ensure stable internet connection
- Try smaller files or different formats

#### Permission Errors
- Verify you have appropriate permissions for the action
- Check if files are locked or in use by others
- Contact administrator for access issues

### GIS Map Issues

#### Map Not Loading
- Check internet connection
- Try refreshing the page
- Clear browser cache
- Contact support if map tiles don't load

#### Location Accuracy
- Verify GPS coordinates are correct
- Check coordinate format (latitude/longitude)
- Update location information if inaccurate

---

## Contact Support

### Technical Support
- **Email**: support@dost-biliran.gov.ph
- **Phone**: (053) 500-XXXX (Provincial Office)
- **Hours**: Monday-Friday, 8:00 AM - 5:00 PM

### Emergency Contact
- **System Administrator**: [Administrator Name]
- **Direct Line**: [Contact Number]
- **Emergency Hours**: 24/7 for critical system issues

### Reporting Issues
When reporting problems, please include:
1. **Your username and role**
2. **Date and time of issue**
3. **Exact steps to reproduce**
4. **Error messages or screenshots**
5. **Browser and device information**
6. **Expected vs. actual behavior**

### Feature Requests
- Use the **Feedback** section in your profile
- Describe the requested feature clearly
- Explain how it would improve your workflow
- Include examples from similar systems if possible

---

**Document Version**: 1.0
**Last Updated**: January 2026
**Prepared by**: DOST Biliran ICT Unit

*This manual is for TaskPro version 1.0. Please check for updates as new features are added.*