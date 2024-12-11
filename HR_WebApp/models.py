from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password  # Import make_password

                
class CustomUser(AbstractUser):
    username = models.CharField(max_length=10, unique=True, null=False)  # Unique employee ID
    full_name = models.CharField(max_length=100)  # Full name of the user

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'password']

    def __str__(self):
        return f"{self.full_name}"

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password:
            self.password = make_password(self.password)  # Hash the password using make_password
        super().save(*args, **kwargs)




class Employee(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='employee')  # Link to CustomUser
    job = models.CharField(max_length=10)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, default=30000.00)

    prime_name_1 = models.CharField(max_length=50, blank=False, default='Risque')
    prime_value_1 = models.IntegerField(default=0)
    cns_1 = models.BooleanField(default=True)
    irg_1 = models.BooleanField(default=True)

    prime_name_2 = models.CharField(max_length=50, blank=True, default='Rendement_Collectif')
    prime_value_2 = models.IntegerField(default=0)
    cns_2 = models.BooleanField(default=True)
    irg_2 = models.BooleanField(default=True)

    prime_name_3 = models.CharField(max_length=50, blank=True, default='Productivity')
    prime_value_3 = models.IntegerField(default=0)
    cns_3 = models.BooleanField(default=True)
    irg_3 = models.BooleanField(default=True)

    prime_name_4 = models.CharField(max_length=50, blank=True, default='Assiduite')
    prime_value_4 = models.IntegerField(default=0)
    cns_4 = models.BooleanField(default=True)
    irg_4 = models.BooleanField(default=True)

    prime_name_5 = models.CharField(max_length=50, blank=True, default='Mession')
    prime_value_5 = models.IntegerField(default=0)
    cns_5 = models.BooleanField(default=False)
    irg_5 = models.BooleanField(default=False)

    prime_name_6 = models.CharField(max_length=50, blank=True, default='Transport')
    prime_value_6 = models.IntegerField(default=0)
    cns_6 = models.BooleanField(default=False)
    irg_6 = models.BooleanField(default=False)

    prime_name_7 = models.CharField(max_length=50, blank=True, default='Fin_Annee')
    prime_value_7 = models.IntegerField(default=0)
    cns_7 = models.BooleanField(default=False)
    irg_7 = models.BooleanField(default=False)

    prime_name_8 = models.CharField(max_length=50, blank=True, default='Occastionnelle')
    prime_value_8 = models.IntegerField(default=0)
    cns_8 = models.BooleanField(default=False)
    irg_8 = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class Month(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='months')
    month_name = models.CharField(max_length=20)  # Example: January, February, etc.
    Net_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
                                                                             
    prime_name_1 = models.CharField(max_length=50, blank=False, default='Risque')
    prime_value_1 = models.IntegerField(default=0)
    cns_1 = models.BooleanField(default=True)
    irg_1 = models.BooleanField(default=True)

    prime_name_2 = models.CharField(max_length=50, blank=True, default='Rendement_Collectif')
    prime_value_2 = models.IntegerField(default=0)
    cns_2 = models.BooleanField(default=True)
    irg_2 = models.BooleanField(default=True)

    prime_name_3 = models.CharField(max_length=50, blank=True, default='Productivity')
    prime_value_3 = models.IntegerField(default=0)
    cns_3 = models.BooleanField(default=True)
    irg_3 = models.BooleanField(default=True)

    prime_name_4 = models.CharField(max_length=50, blank=True, default='Assiduite')
    prime_value_4 = models.IntegerField(default=0)
    cns_4 = models.BooleanField(default=True)
    irg_4 = models.BooleanField(default=True)

    prime_name_5 = models.CharField(max_length=50, blank=True, default='Mession')
    prime_value_5 = models.IntegerField(default=0)
    cns_5 = models.BooleanField(default=False)
    irg_5 = models.BooleanField(default=False)

    prime_name_6 = models.CharField(max_length=50, blank=True, default='Transport')
    prime_value_6 = models.IntegerField(default=0)
    cns_6 = models.BooleanField(default=False)
    irg_6 = models.BooleanField(default=False)

    prime_name_7 = models.CharField(max_length=50, blank=True, default='Fin_Annee')
    prime_value_7 = models.IntegerField(default=0)
    cns_7 = models.BooleanField(default=False)
    irg_7 = models.BooleanField(default=False)

    prime_name_8 = models.CharField(max_length=50, blank=True, default='Occastionnelle')
    prime_value_8 = models.IntegerField(default=0)
    cns_8 = models.BooleanField(default=False)
    irg_8 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.month_name} - {self.employee.user.username}"



class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')

    leave_type_choices = [
        ('Sick', 'Sick Leave'),
        ('Casual', 'Casual Leave'),
        ('Annual', 'Annual Leave'),
        ('Maternity', 'Maternity Leave'),
        ('Paternity', 'Paternity Leave'),
        ('Unpaid', 'Unpaid Leave'),
    ]

    leave_type = models.CharField(max_length=20, choices=leave_type_choices, default='Sick')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(max_length=500, blank=True, null=True)

    status_choices = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    request_date = models.DateTimeField(auto_now_add=True)
    decision_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f" - {self.leave_type} from ({self.start_date} to {self.end_date})"
    




