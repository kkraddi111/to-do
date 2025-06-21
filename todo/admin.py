from django.contrib import admin
from django.utils.html import format_html
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title_with_status', 'description_preview', 'status_colored', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description')
        }),
        ('Status', {
            'fields': ('completed',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

    def title_with_status(self, obj):
        icon = '✓' if obj.completed else '○'
        return format_html('{} {}', icon, obj.title)
    title_with_status.short_description = 'Task'

    def description_preview(self, obj):
        if obj.description:
            return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
        return '-'
    description_preview.short_description = 'Description'

    def status_colored(self, obj):
        color = 'green' if obj.completed else 'orange'
        status = obj.get_status_display()
        return format_html('<span style="color: {};">{}</span>', color, status)
    status_colored.short_description = 'Status'
