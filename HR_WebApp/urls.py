from django.urls import path
from .views import LoginAPIView, EmployeeDashboardAPIView, LeaveRequestAPIView

urlpatterns = [
    path('api/login/', LoginAPIView.as_view(), name='api_login'),
    path('api/dashboard/', EmployeeDashboardAPIView.as_view(), name='employee_dashboard'),
    path('api/leave-requests/', LeaveRequestAPIView.as_view(), name='leave_requests'),
]


