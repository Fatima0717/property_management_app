from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'address')
    search_fields = ('name', 'address')
    list_filter = ('type',)  # Assuming you have a 'type' field
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'address', 'description', 'type', 'available'),
        }),
    )
    
    actions = ['mark_as_sold']

    def mark_as_sold(self, request, queryset):
        queryset.update(status='sold')
    mark_as_sold.short_description = "Mark selected properties as sold"
