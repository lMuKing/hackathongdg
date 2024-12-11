
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import CustomUser, Employee, LeaveRequest
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import Employee
from .serializers import CustomUserSerializer,EmployeeSerializer,LeaveRequestSerializer 

class LoginAPIView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Try to authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user:
            # Ensure that the token is created only once
            token, created = Token.objects.get_or_create(user=user)

            # Serialize the user object
            user_data = CustomUserSerializer(user).data

            if user.is_superuser:
                return Response(
                    {
                        'message': 'Admin login successful',
                        'token': token.key,
                        'role': 'admin',
                        'redirect_url': '/admin/',
                        'user': user_data,  # Include user data in the response
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                # Ensure the employee is linked to the user
                try:
                    employee = get_object_or_404(Employee, user=user)
                    return Response(
                        {
                            'message': 'Employee login successful',
                            'token': token.key,
                            'role': 'employee',
                            'redirect_url': '/dashboard/',
                            'details': {
                                'Full_Name': employee.user.full_name,
                                'Grade': employee.job,  # Assuming 'Grade' is related to 'job'
                                'Base_Salary': employee.base_salary,
                            },
                            'user': user_data,  # Include user data in the response
                        },
                        status=status.HTTP_200_OK,
                    )
                except Employee.DoesNotExist:
                    return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


class EmployeeDashboardAPIView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Get employee linked to the authenticated user
            employee = get_object_or_404(Employee, user=request.user)
            
            # Serialize the employee data
            employee_serializer = EmployeeSerializer(employee)
            
            # Return serialized data
            return Response(employee_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
    
class LeaveRequestAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        employee = get_object_or_404(Employee, user=request.user)
        leave_requests = LeaveRequest.objects.filter(employee=employee)
        
        # Serialize leave requests
        leave_requests_serializer = LeaveRequestSerializer(leave_requests, many=True)
        return Response(leave_requests_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        employee = get_object_or_404(Employee, user=request.user)

        # Add employee ID to the request data
        request.data['employee'] = employee.id

        # Serialize the request data
        leave_request_serializer = LeaveRequestSerializer(data=request.data)

        if leave_request_serializer.is_valid():
            leave_request_serializer.save()
            return Response(
                {'message': 'Leave request submitted successfully!'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            leave_request_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

 


