from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee, LeaveRequest  # Ensure you import Employee and LeaveRequest models here

# Get the custom user model
CustomUser = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name']  # Adjust fields as needed

class EmployeeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Embed the CustomUser serializer to include user details

    class Meta:
        model = Employee
        fields = [
            'user',  # The CustomUser instance for this employee
            'job',
            'base_salary',
            'prime_name_1', 'prime_value_1', 'cns_1', 'irg_1',
            'prime_name_2', 'prime_value_2', 'cns_2', 'irg_2',
            'prime_name_3', 'prime_value_3', 'cns_3', 'irg_3',
            'prime_name_4', 'prime_value_4', 'cns_4', 'irg_4',
            'prime_name_5', 'prime_value_5', 'cns_5', 'irg_5',
            'prime_name_6', 'prime_value_6', 'cns_6', 'irg_6',
            'prime_name_7', 'prime_value_7', 'cns_7', 'irg_7',
            'prime_name_8', 'prime_value_8', 'cns_8', 'irg_8'
        ]  # Adjust the fields as necessary

class LeaveRequestSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())  # Employee ID reference

    class Meta:
        model = LeaveRequest
        fields = ['employee', 'leave_type', 'start_date', 'end_date', 'reason', 'status', 'request_date', 'decision_date']







