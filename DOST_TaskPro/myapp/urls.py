# urls.py
from django.urls import path
from . import views
urlpatterns = [

# Add this line for the index page
    path('', views.index_view, name='index_url'),
    path('auth/splash/', views.auth_splash_view, name='auth_splash_url'),

# Logout
    path('logout/', views.logout_view, name='logout_url'),





# Administrator

path('administrator/dashboard/', views.administrator_dashboard_view, name='administrator_dashboard_url'),
path('administrator/quick-actions/', views.administrator_quick_actions_view, name='administrator_quick_actions_url'),
path('administrator/assistant/chat/', views.assistant_ai_chat_view, name='assistant_ai_chat_url'),

# Users
path('administrator/users/', views.administrator_users_view, name='administrator_users_url'),
path('administrator/users/add/', views.administrator_users_add_view, name='administrator_users_add_url'),
path('administrator/users/update/<int:user_id>/', views.administrator_users_update_view, name='administrator_users_update_url'),
path('administrator/users/delete/<int:user_id>/', views.administrator_users_delete_view, name='administrator_users_delete_url'),
path('administrator/users/mass-delete/', views.administrator_users_mass_delete_view, name='administrator_users_mass_delete_url'),



path('administrator/budgets/', views.administrator_budgets_view, name='administrator_budgets_url'),
path('administrator/budgets/add/', views.administrator_budgets_add_view, name='administrator_budgets_add_url'),
path('administrator/budgets/update/<int:budget_id>/', views.administrator_budgets_update_view, name='administrator_budgets_update_url'),
path('administrator/budgets/delete/<int:budget_id>/', views.administrator_budgets_delete_view, name='administrator_budgets_delete'),

# Document deletion URLs
path('delete-document/budget/<int:document_id>/', views.delete_budget_document, name='delete_budget_document'),
path('delete-document/proposal/<int:document_id>/', views.delete_proposal_document, name='delete_proposal_document'),
path('delete-document/project/<int:document_id>/', views.delete_project_document, name='delete_project_document'),
path('delete-document/expense/<int:document_id>/', views.delete_expense_document, name='delete_expense_document'),



path('administrator/proposals/', views.administrator_proposals_view, name='administrator_proposals_url'),
path('administrator/proposals/add/', views.administrator_proposals_add_view, name='administrator_proposals_add_url'),
path('administrator/proposals/update/<int:pk>/', views.administrator_proposals_update_view, name='administrator_proposals_update_url'),
path('administrator/proposals/delete/<int:pk>/', views.administrator_proposals_delete_view, name='administrator_proposals_delete_url'),
path('administrator/proposals/mass-delete/', views.administrator_proposals_mass_delete_view, name='administrator_proposals_mass_delete_url'),


path('administrator/proposals/approve/<int:pk>/', 
     views.administrator_proposals_approve_view, 
     name='administrator_proposals_approve_url'),

# Decline proposal (POST only, ID via hidden input)
path(
    'administrator/proposals/decline/',
    views.administrator_proposals_decline_view,
    name='administrator_proposals_decline_url'
),


path('projects/', views.administrator_projects_view, name='administrator_projects_url'),
path('projects/<int:pk>/', views.administrator_projects_detail_view, name='administrator_projects_detail_url'),
path('projects/add/', views.administrator_projects_add_view, name='administrator_projects_add_url'),
path('projects/update/<int:pk>/', views.administrator_projects_update_view, name='administrator_projects_update_url'),
path('projects/delete/<int:pk>/', views.administrator_projects_delete_view, name='administrator_projects_delete_url'),
path('projects/mass-delete/', views.administrator_projects_mass_delete_view, name='administrator_projects_mass_delete_url'),
path('projects/equipment-delivery/', views.administrator_equipment_delivery_add_view, name='administrator_equipment_delivery_add'),

path('notifications/read/<int:pk>/', views.mark_notification_read_view, name='mark_notification_read'),
path('notifications/delete/<int:pk>/', views.delete_notification_view, name='delete_notification'),
path('notifications/clear-all/', views.clear_all_notifications_view, name='clear_all_notifications'),
path('notifications/count/', views.get_notification_count_view, name='get_notification_count'),
path('notifications/stream/', views.notifications_stream_view, name='notifications_stream'),


# Administrator Task Management
path('administrator/tasks/', views.administrator_task_list_view, name='administrator_task_list_url'),
path('administrator/tasks/create/', views.administrator_task_create_view, name='administrator_task_create_url'),
path('administrator/tasks/edit/', views.administrator_task_edit_view, name='administrator_task_edit_url'),
path('administrator/tasks/delete/<int:task_id>/', views.administrator_task_delete_view, name='administrator_task_delete_url'),



# Administrator Reports
path('administrator/reports/', views.administrator_reports_view, name='administrator_reports_url'),

# Administrator Settings
path('administrator/settings/', views.administrator_settings_view, name='administrator_settings_url'),

path('administrator/change-password/', views.administrator_change_password_view, name='administrator_change_password_url'),

path('administrator/audit-logs/', views.administrator_audit_logs_view, name='administrator_audit_logs_url'),

# Administrator Forms
path('administrator/forms/', views.administrator_forms_view, name='administrator_forms_url'),
path('administrator/forms/add/', views.administrator_forms_add_view, name='administrator_forms_add_url'),
path('administrator/forms/edit/<int:form_id>/', views.administrator_forms_edit_view, name='administrator_forms_edit_url'),
path('administrator/forms/delete/<int:form_id>/', views.administrator_forms_delete_view, name='administrator_forms_delete_url'),

# Form Download (shared across all roles)
path('forms/download/<int:form_id>/', views.form_download_view, name='form_download_url'),

# Administrator Extension Requests
path('administrator/extension-requests/', views.administrator_extension_requests_view, name='administrator_extension_requests_url'),
path('administrator/extension-requests/approve/<int:pk>/', views.administrator_extension_requests_approve_view, name='administrator_extension_requests_approve_url'),
path('administrator/extension-requests/reject/<int:pk>/', views.administrator_extension_requests_reject_view, name='administrator_extension_requests_reject_url'),
path('administrator/extension-requests/edit/<int:pk>/', views.administrator_extension_requests_edit_view, name='administrator_extension_requests_edit_url'),
path('administrator/extension-requests/delete/<int:pk>/', views.administrator_extension_requests_delete_view, name='administrator_extension_requests_delete_url'),
path('administrator/extension-requests/bulk-approve/', views.administrator_extension_requests_bulk_approve_view, name='administrator_extension_requests_bulk_approve_url'),
path('administrator/extension-requests/bulk-reject/', views.administrator_extension_requests_bulk_reject_view, name='administrator_extension_requests_bulk_reject_url'),

path('administrator/reports/export-financial/', views.financial_summary_pdf, name='export_financial_pdf'),

path('administrator/reports/export-full/', views.export_full_report_pdf, name='export_full_report_pdf'),

path('reports/proposal-status/pdf/', views.proposal_status_pdf, name='proposal_status_pdf'),

path('reports/approved-projects/pdf/<int:report_year>/', 
         views.approved_projects_pdf, 
         name='approved_projects_pdf'),

# Excel Export URLs
path('export/projects/excel/', views.export_projects_excel, name='export_projects_excel'),
path('export/budgets/excel/', views.export_budgets_excel, name='export_budgets_excel'),
path('export/proposals/excel/', views.export_proposals_excel, name='export_proposals_excel'),
path('export/tasks/excel/', views.export_tasks_excel, name='export_tasks_excel'),
path('export/master-report/excel/', views.export_master_report_excel, name='export_master_report_excel'),

# Report Export URLs
path('administrator/reports/user-productivity/export/pdf/', views.export_user_productivity_pdf, name='export_user_productivity_pdf'),
path('administrator/reports/project-progress/export/excel/', views.export_project_progress_excel, name='export_project_progress_excel'),

#Staff
path('staff/dashboard/', views.staff_dashboard_view, name='staff_dashboard_url'),
path('staff/quick-actions/', views.staff_quick_actions_view, name='staff_quick_actions_url'),


# Users
path('staff/users/', views.staff_users_view, name='staff_users_url'),


path('staff/budgets/', views.staff_budgets_view, name='staff_budgets_url'),


path('staff/proposals/', views.staff_proposals_view, name='staff_proposals_url'),

path('staff/proposals/add/', views.staff_proposals_add_view, name='staff_proposals_add_url'),

path('staff/proposals/update/<int:pk>/', views.staff_proposals_update_view, name='staff_proposals_update_url'),

path('staff/<int:task_id>/mark-completed/', views.mark_task_completed_view, name='mark_task_completed'),


path('staff/projects/', views.staff_projects_view, name='staff_projects_url'),

# Staff Messages
path('staff/messages/', views.staff_messages_view, name='staff_messages_url'),
path('staff/messages/conversation/<int:partner_id>/', views.staff_conversation_view, name='staff_conversation_url'),
path('staff/messages/compose/', views.staff_compose_message_view, name='staff_compose_message_url'),
path('staff/messages/<int:message_id>/', views.staff_message_detail_view, name='staff_message_detail_url'),
path('staff/announcements/', views.staff_announcements_view, name='staff_announcements_url'),

# Staff Task Management
path('staff/tasks/', views.staff_task_list_view, name='staff_task_list_url'),
path('staff/tasks/edit/', views.staff_task_edit_view, name='staff_task_edit_url'),

# Staff Personal Task Management
path('staff/personal-tasks/', views.staff_personal_tasks_view, name='staff_personal_tasks_url'),
path('staff/personal-tasks/create/', views.staff_personal_task_create_view, name='staff_personal_task_create_url'),
path('staff/personal-tasks/<int:task_id>/toggle/', views.staff_personal_task_toggle_view, name='staff_personal_task_toggle_url'),
path('staff/personal-tasks/<int:task_id>/toggle-checklist-item/', views.staff_personal_task_toggle_checklist_item_view, name='staff_personal_task_toggle_checklist_item_url'),
path('staff/personal-tasks/<int:task_id>/edit/', views.staff_personal_task_edit_view, name='staff_personal_task_edit_url'),
path('staff/personal-tasks/<int:task_id>/delete/', views.staff_personal_task_delete_view, name='staff_personal_task_delete_url'),


# Mark project as completed
    path('project/<int:project_id>/complete/', 
            views.mark_project_completed, 
            name='mark_project_completed'),


# staff Reports
path('staff/reports/', views.staff_reports_view, name='staff_reports_url'),

# staff Settings
path('staff/settings/', views.staff_settings_view, name='staff_settings_url'),

path('staff/change-password/', views.staff_change_password_view, name='staff_change_password_url'),

path('staff/audit-logs/', views.staff_audit_logs_view, name='staff_audit_logs_url'),

# Staff Forms
path('staff/forms/', views.staff_forms_view, name='staff_forms_url'),




















#proponent
path('proponent/dashboard/', views.proponent_dashboard_view, name='proponent_dashboard_url'),


# Users
# path('proponent/users/', views.proponent_users_view, name='proponent_users_url'),


path('proponent/budgets/', views.proponent_budgets_view, name='proponent_budgets_url'),


path('proponent/proposals/', views.proponent_proposals_view, name='proponent_proposals_url'),

path('proponent/proposals/add/', views.proponent_proposals_add_view, name='proponent_proposals_add_url'),

path('proponent/proposals/update/<int:pk>/', views.proponent_proposals_update_view, name='proponent_proposals_update_url'),



path('proponent/projects/', views.proponent_projects_view, name='proponent_projects_url'),

# proponent Task Management
path('proponent/tasks/', views.proponent_task_list_view, name='proponent_task_list_url'),

# proponent Reports
path('proponent/reports/', views.proponent_reports_view, name='proponent_reports_url'),

# proponent Settings
path('proponent/settings/', views.proponent_settings_view, name='proponent_settings_url'),

path('proponent/change-password/', views.proponent_change_password_view, name='proponent_change_password_url'),

path('proponent/audit-logs/', views.proponent_audit_logs_view, name='proponent_audit_logs_url'),

# Proponent Forms
path('proponent/forms/', views.proponent_forms_view, name='proponent_forms_url'),



















#proponent
path('proponent/dashboard/', views.proponent_dashboard_view, name='proponent_dashboard_url'),


# Users
# path('proponent/users/', views.proponent_users_view, name='proponent_users_url'),


path('proponent/budgets/', views.proponent_budgets_view, name='proponent_budgets_url'),


path('proponent/proposals/', views.proponent_proposals_view, name='proponent_proposals_url'),

path('proponent/proposals/add/', views.proponent_proposals_add_view, name='proponent_proposals_add_url'),

path('proponent/proposals/update/<int:pk>/', views.proponent_proposals_update_view, name='proponent_proposals_update_url'),



path('proponent/projects/', views.proponent_projects_view, name='proponent_projects_url'),

# proponent Task Management
path('proponent/tasks/', views.proponent_task_list_view, name='proponent_task_list_url'),

# proponent Reports
path('proponent/reports/', views.proponent_reports_view, name='proponent_reports_url'),

# proponent Settings
path('proponent/settings/', views.proponent_settings_view, name='proponent_settings_url'),

path('proponent/change-password/', views.proponent_change_password_view, name='proponent_change_password_url'),

path('proponent/audit-logs/', views.proponent_audit_logs_view, name='proponent_audit_logs_url'),






# proponent Extension Requests
path('proponent/extension-requests/', views.proponent_extension_requests_view, name='proponent_extension_requests_url'),
path('proponent/extension-requests/add/', views.proponent_extension_requests_add_view, name='proponent_extension_requests_add_url'),





#beneficiary
path('beneficiary/dashboard/', views.beneficiary_dashboard_view, name='beneficiary_dashboard_url'),

path('beneficiary/proposals/', views.beneficiary_proposals_view, name='beneficiary_proposals_url'),

path('beneficiary/projects/', views.beneficiary_projects_view, name='beneficiary_projects_url'),

# beneficiary Task Management
path('beneficiary/tasks/', views.beneficiary_task_list_view, name='beneficiary_task_list_url'),

# beneficiary Reports
path('beneficiary/reports/', views.beneficiary_reports_view, name='beneficiary_reports_url'),

# beneficiary Settings
path('beneficiary/settings/', views.beneficiary_settings_view, name='beneficiary_settings_url'),

path('beneficiary/change-password/', views.beneficiary_change_password_view, name='beneficiary_change_password_url'),

path('beneficiary/audit-logs/', views.beneficiary_audit_logs_view, name='beneficiary_audit_logs_url'),

# Beneficiary Forms
path('beneficiary/forms/', views.beneficiary_forms_view, name='beneficiary_forms_url'),







































# Administrator Communication Hub
path('administrator/communication-hub/', views.administrator_communication_hub_view, name='administrator_communication_hub_url'),

# Administrator Messages
path('administrator/messages/', views.administrator_messages_view, name='administrator_messages_url'),
path('administrator/messages/conversation/<int:partner_id>/', views.administrator_conversation_view, name='administrator_conversation_url'),
path('administrator/messages/compose/', views.administrator_compose_message_view, name='administrator_compose_message_url'),
path('administrator/messages/<int:message_id>/', views.administrator_message_detail_view, name='administrator_message_detail_url'),

# One-Sided Delete Endpoints (works for all roles)
path('messages/delete-conversation/<int:partner_id>/', views.delete_conversation_view, name='delete_conversation_url'),
path('messages/delete/<int:message_id>/', views.delete_message_view, name='delete_message_url'),
path('group-chats/delete/<int:chat_id>/', views.delete_group_chat_view, name='delete_group_chat_url'),
path('group-chats/delete-message/<int:message_id>/', views.delete_group_message_view, name='delete_group_message_url'),

# Administrator Group Chats
path('administrator/group-chats/', views.administrator_group_chats_view, name='administrator_group_chats_url'),
path('administrator/group-chats/create/', views.administrator_create_group_chat_view, name='administrator_create_group_chat_url'),
path('administrator/group-chats/<int:chat_id>/', views.administrator_group_chat_detail_view, name='administrator_group_chat_detail_url'),
path('administrator/group-chats/<int:chat_id>/manage-members/', views.administrator_manage_group_chat_members_view, name='administrator_manage_group_chat_members_url'),
path('administrator/group-chats/<int:chat_id>/edit-settings/', views.administrator_edit_group_chat_settings_view, name='administrator_edit_group_chat_settings_url'),

# Staff Group Chats
path('staff/group-chats/', views.staff_group_chats_view, name='staff_group_chats_url'),
path('staff/group-chats/create/', views.staff_create_group_chat_view, name='staff_create_group_chat_url'),
path('staff/group-chats/<int:chat_id>/', views.staff_group_chat_detail_view, name='staff_group_chat_detail_url'),

# Administrator Announcements
path('administrator/announcements/', views.administrator_announcements_view, name='administrator_announcements_url'),
path('administrator/announcements/create/', views.administrator_create_announcement_view, name='administrator_create_announcement_url'),
path('administrator/announcements/update/<int:pk>/', views.administrator_update_announcement_view, name='administrator_update_announcement_url'),
path('administrator/announcements/delete/<int:pk>/', views.administrator_delete_announcement_view, name='administrator_delete_announcement_url'),

# Administrator System Health
path('administrator/system-health/', views.administrator_system_health_view, name='administrator_system_health_url'),
path('administrator/backup-management/', views.administrator_backup_management_view, name='administrator_backup_management_url'),
path('administrator/maintenance-schedule/', views.administrator_maintenance_schedule_view, name='administrator_maintenance_schedule_url'),
path('administrator/maintenance-schedule/create/', views.administrator_create_maintenance_task_view, name='administrator_create_maintenance_task_url'),

# Staff Messages
path('staff/messages/', views.staff_messages_view, name='staff_messages_url'),
path('staff/messages/compose/', views.staff_compose_message_view, name='staff_compose_message_url'),
path('staff/messages/<int:message_id>/', views.staff_message_detail_view, name='staff_message_detail_url'),
path('staff/announcements/', views.staff_announcements_view, name='staff_announcements_url'),

# Proponent Messages
path('proponent/messages/', views.proponent_messages_view, name='proponent_messages_url'),
path('proponent/messages/conversation/<int:partner_id>/', views.proponent_conversation_view, name='proponent_conversation_url'),
path('proponent/messages/compose/', views.proponent_compose_message_view, name='proponent_compose_message_url'),
path('proponent/messages/<int:message_id>/', views.proponent_message_detail_view, name='proponent_message_detail_url'),
path('proponent/announcements/', views.proponent_announcements_view, name='proponent_announcements_url'),

# Proponent Group Chats
path('proponent/group-chats/', views.proponent_group_chats_view, name='proponent_group_chats_url'),
path('proponent/group-chats/create/', views.proponent_create_group_chat_view, name='proponent_create_group_chat_url'),
path('proponent/group-chats/<int:chat_id>/', views.proponent_group_chat_detail_view, name='proponent_group_chat_detail_url'),

# Beneficiary Messages
path('beneficiary/messages/', views.beneficiary_messages_view, name='beneficiary_messages_url'),
path('beneficiary/messages/conversation/<int:partner_id>/', views.beneficiary_conversation_view, name='beneficiary_conversation_url'),
path('beneficiary/messages/compose/', views.beneficiary_compose_message_view, name='beneficiary_compose_message_url'),
path('beneficiary/messages/<int:message_id>/', views.beneficiary_message_detail_view, name='beneficiary_message_detail_url'),
path('beneficiary/announcements/', views.beneficiary_announcements_view, name='beneficiary_announcements_url'),

# Beneficiary Group Chats
path('beneficiary/group-chats/', views.beneficiary_group_chats_view, name='beneficiary_group_chats_url'),
path('beneficiary/group-chats/create/', views.beneficiary_create_group_chat_view, name='beneficiary_create_group_chat_url'),
path('beneficiary/group-chats/<int:chat_id>/', views.beneficiary_group_chat_detail_view, name='beneficiary_group_chat_detail_url'),

# ===============================
# CALENDAR FEATURE (#17)
# ===============================
path('administrator/calendar/', views.administrator_calendar_view, name='administrator_calendar_url'),
path('administrator/calendar/events/', views.administrator_calendar_events_api, name='administrator_calendar_events_api'),
path('administrator/calendar/event/add/', views.administrator_calendar_event_add, name='administrator_calendar_event_add'),
path('administrator/calendar/event/<int:event_id>/edit/', views.administrator_calendar_event_edit, name='administrator_calendar_event_edit'),
path('administrator/calendar/event/<int:event_id>/delete/', views.administrator_calendar_event_delete, name='administrator_calendar_event_delete'),

# Staff Calendar
path('staff/calendar/', views.staff_calendar_view, name='staff_calendar_url'),

# ===============================
# PROJECT CLONING (#14)
# ===============================
path('projects/<int:pk>/clone/', views.administrator_project_clone_view, name='administrator_project_clone_url'),

# ===============================
# DIGITAL SIGNATURES (#24)
# ===============================
path('signature/create/', views.create_digital_signature_view, name='create_digital_signature_url'),
path('signature/verify/<int:signature_id>/', views.verify_digital_signature_view, name='verify_digital_signature_url'),
path('api/signatures/<str:content_type>/<int:object_id>/', views.get_signatures_api, name='get_signatures_api'),
path('api/signatures/delete/<int:signature_id>/', views.delete_signature_api, name='delete_signature_api'),

# ===============================
# GANTT CHART (#18)
# ===============================
path('projects/<int:pk>/gantt/', views.project_gantt_view, name='project_gantt_url'),
path('projects/<int:pk>/milestones/', views.project_milestones_api, name='project_milestones_api'),
path('projects/<int:pk>/milestones/add/', views.project_milestone_add, name='project_milestone_add'),
path('milestones/<int:milestone_id>/update/', views.project_milestone_update, name='project_milestone_update'),

# ===============================
# LANGUAGE TOGGLE (#21)
# ===============================
path('set-language/', views.set_language_view, name='set_language_url'),

# ===============================
# GLOBAL SEARCH API
# ===============================
path('api/search/', views.global_search_api, name='global_search_api'),

# ===============================
# MENTIONS API
# ===============================
path('api/mentions/search/', views.mentions_search_api, name='mentions_search_api'),
path('api/mentions/create/', views.create_mention_view, name='create_mention_url'),

]