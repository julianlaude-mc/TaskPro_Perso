#!/usr/bin/env python3
"""Batch convert remaining staff module tables to compact expandable format"""

import re
import os

os.chdir('DOST_TaskPro')

# Update tasks.html
print("Updating tasks.html...")
with open('templates/staff/tasks.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add tasksExpanded to Alpine data
content = content.replace(
    'openViewMap: false,',
    'openViewMap: false,\n        tasksExpanded: false,'
)

# Replace the main table
old = '''<table id="tasksTable" class="data-table">
            <thead>
                <tr>
                    <th class="px-4 py-2">#</th>
                    <th class="px-4 py-2">Project</th>
                    <th class="px-4 py-2">Task Description</th>
                    <th class="px-4 py-2">Due Date</th>
                    <th class="px-4 py-2">Status</th>
                    <th class="px-4 py-2 text-center">Actions</th>
                </tr>
            </thead>'''

new = '''<table class="table-compact" id="tasksTableCompact">
            <thead>
                <tr>
                    <th class="px-4 py-2">#</th>
                    <th class="px-4 py-2">Project</th>
                    <th class="px-4 py-2">Status</th>
                </tr>
            </thead>'''

if old in content:
    content = content.replace(old, new)
    print("  ✓ Converted table header and columns")

# Replace tbody
old_tbody = '''<tbody>
                {% for task in tasks %}
                <tr class="hover:bg-gray-50">
                    <td data-label="#" class="px-4 py-2">{{ forloop.counter }}</td>
                    <td data-label="Project" class="px-4 py-2 font-medium">{{ task.project.project_title|truncatewords:5 }}</td>
                    <td data-label="Task Description" class="px-4 py-2">{{ task.description|truncatewords:10 }}</td>
                    <td data-label="Due Date" class="px-4 py-2">
                        {% if task.due_date %}
                            {{ task.due_date|date:"M d, Y" }}
                        {% else %}
                            <span class="text-gray-400">No due date</span>
                        {% endif %}
                    </td>
                    <td data-label="Status" class="px-4 py-2 text-center">
                        {% if task.status == 'pending' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-yellow-100 text-yellow-800 font-medium">Pending</span>
                        {% elif task.status == 'in_progress' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-blue-100 text-blue-800 font-medium">In Progress</span>
                        {% elif task.status == 'completed' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-green-100 text-green-800 font-medium">Completed</span>
                        {% elif task.status == 'delayed' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-red-100 text-red-800 font-medium">Delayed</span>
                        {% endif %}
                    </td>
                    <td data-label="Actions" class="px-4 py-2 text-center">
                        <div class="flex gap-2 justify-center">
                            {% if task.project.latitude and task.project.longitude %}
                            <button type="button"
                                    class="px-3 py-1 text-xs text-white bg-green-500 rounded hover:bg-green-600"
                                    @click="openViewMapModal('{{ task.title|escapejs }}', {{ task.project.latitude }}, {{ task.project.longitude }})">
                                <span class="material-icons text-sm align-middle">location_on</span> View Map
                            </button>
                            {% else %}
                            <span class="text-gray-400 text-xs">No location</span>
                            {% endif %}

                            <button type="button"
                                    @click="editTask = {id: {{ task.id }}, title: '{{ task.title|escapejs }}', description: '{{ task.description|escapejs }}', status: '{{ task.status }}', due_date: '{{ task.due_date|date:"Y-m-d" }}'}; openEdit = true"
                                    class="px-3 py-1 text-xs text-white bg-blue-500 rounded hover:bg-blue-600">
                                <span class="material-icons text-sm align-middle">edit</span> Edit Status
                            </button>

                            {% if task.status != 'completed' %}
                            <form method="POST" action="{% url 'mark_task_completed' task.id %}" class="inline">
                                {% csrf_token %}
                                <button type="submit"
                                        class="px-3 py-1 text-xs text-white bg-green-500 rounded hover:bg-green-600"
                                        onclick="return confirm('Mark this task as completed?')">
                                    <span class="material-icons text-sm align-middle">check_circle</span> Complete
                                </button>
                            </form>
                            {% endif %}
                        </div>
                    </td>
                </tr>
                {% endfor %}
            </tbody>'''

new_tbody = '''<tbody>
                {% for task in tasks %}
                <tr class="hover:bg-gray-50">
                    <td data-label="#" class="px-4 py-2">{{ forloop.counter }}</td>
                    <td data-label="Project" class="px-4 py-2 font-medium">{{ task.project.project_title|truncatewords:5 }}</td>
                    <td data-label="Status" class="px-4 py-2 text-center">
                        {% if task.status == 'pending' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-yellow-100 text-yellow-800 font-medium">Pending</span>
                        {% elif task.status == 'in_progress' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-blue-100 text-blue-800 font-medium">In Progress</span>
                        {% elif task.status == 'completed' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-green-100 text-green-800 font-medium">Completed</span>
                        {% elif task.status == 'delayed' %}
                            <span class="px-2 py-1 rounded-full text-xs bg-red-100 text-red-800 font-medium">Delayed</span>
                        {% endif %}
                    </td>
                </tr>
                {% endfor %}
            </tbody>'''

if old_tbody in content:
    content = content.replace(old_tbody, new_tbody)
    print("  ✓ Converted table body to compact format")

# Add expand button and modal before View Map Modal
expand_section = '''
    </div>

    <!-- View All Tasks Button -->
    {% if tasks|length > 5 %}
    <button @click="tasksExpanded = true" class="expand-btn">
        <span class="material-icons">expand</span>
        View All Tasks ({{ tasks|length }})
    </button>
    {% endif %}

    <!-- Expanded Tasks Modal -->
    <div class="expand-modal-overlay" :class="{ active: tasksExpanded }">
        <div class="expand-modal-content" @click.stop="">
            <div class="expand-modal-header">
                <h2>All Assignment Items</h2>
                <button class="expand-modal-close" @click="tasksExpanded = false">
                    <span class="material-icons">close</span>
                </button>
            </div>
            <div class="expand-modal-body">
                <table class="table-compact expanded">
                    <thead>
                        <tr>
                            <th class="px-4 py-2">#</th>
                            <th class="px-4 py-2">Project</th>
                            <th class="px-4 py-2">Task Description</th>
                            <th class="px-4 py-2">Due Date</th>
                            <th class="px-4 py-2">Status</th>
                            <th class="px-4 py-2 text-center">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for task in tasks %}
                        <tr class="hover:bg-gray-50">
                            <td data-label="#" class="px-4 py-2">{{ forloop.counter }}</td>
                            <td data-label="Project" class="px-4 py-2 font-medium">{{ task.project.project_title }}</td>
                            <td data-label="Task Description" class="px-4 py-2">{{ task.description }}</td>
                            <td data-label="Due Date" class="px-4 py-2">
                                {% if task.due_date %}{{ task.due_date|date:"M d, Y" }}{% else %}<span class="text-gray-400">-</span>{% endif %}
                            </td>
                            <td data-label="Status" class="px-4 py-2 text-center">
                                {% if task.status == 'pending' %}<span class="px-2 py-1 rounded-full text-xs bg-yellow-100 text-yellow-800 font-medium">Pending</span>
                                {% elif task.status == 'in_progress' %}<span class="px-2 py-1 rounded-full text-xs bg-blue-100 text-blue-800 font-medium">In Progress</span>
                                {% elif task.status == 'completed' %}<span class="px-2 py-1 rounded-full text-xs bg-green-100 text-green-800 font-medium">Completed</span>
                                {% elif task.status == 'delayed' %}<span class="px-2 py-1 rounded-full text-xs bg-red-100 text-red-800 font-medium">Delayed</span>{% endif %}
                            </td>
                            <td data-label="Actions" class="px-4 py-2 text-center">
                                <div class="flex gap-1 justify-center">
                                    {% if task.project.latitude and task.project.longitude %}<button type="button" class="px-2 py-1 text-xs text-white bg-green-500 rounded" @click="openViewMapModal('{{ task.title|escapejs }}', {{ task.project.latitude }}, {{ task.project.longitude }})"><span class="material-icons text-sm">location_on</span></button>{% endif %}
                                    <button type="button" class="px-2 py-1 text-xs text-white bg-blue-500 rounded" @click="editTask = {id: {{ task.id }}, title: '{{ task.title|escapejs }}', description: '{{ task.description|escapejs }}', status: '{{ task.status }}', due_date: '{{ task.due_date|date:"Y-m-d" }}'}; openEdit = true"><span class="material-icons text-sm">edit</span></button>
                                </div>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- View Map Modal -->'''

content = content.replace(
    '''    </div>
    {% else %}
    <!-- No Tasks Message -->
    <div class="bg-white rounded-xl shadow-lg p-12 text-center">
        <span class="material-icons text-6xl text-gray-300 mb-4">assignment_turned_in</span>
        <h3 class="text-xl font-semibold text-gray-700 mb-2">No tasks assigned to you yet</h3>
        <p class="text-gray-500">When the administrator assigns tasks to you, they will appear here.</p>
    </div>
    {% endif %}

    <!-- View Map Modal -->''',
    expand_section
)

with open('templates/staff/tasks.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("✓ Completed tasks.html\n")

print("All module tables converted to compact+expandable format!")
