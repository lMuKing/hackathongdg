from django.contrib import admin
from .models import CustomUser, Employee, LeaveRequest

# Register your models here
admin.site.register(CustomUser)
admin.site.register(Employee)

class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status', 'request_date', 'decision_date')
    list_filter = ('status', 'leave_type', 'employee')

    # Ndir the 'status' field to make it editable only by admin users
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        
        # Make the 'status' field read-only for non-admin users
        if not request.user.is_superuser:  # Only admins can edit 'status'
            form.base_fields['status'].disabled = True
        
        return form

admin.site.register(LeaveRequest, LeaveRequestAdmin)

            