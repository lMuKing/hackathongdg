
from .models import Employee



                                                                       
def calculateCNS():
    cns = 0 
    if (Employee.cns_1 == True):
        cns  = cns + Employee.prime_value_1
    if (Employee.cns_2 == True):
        cns  = cns + Employee.prime_value_2
    if (Employee.cns_3 == True):
        cns  = cns + Employee.prime_value_3
    if (Employee.cns_4 == True):
        cns  = cns + Employee.prime_value_4
    if (Employee.cns_5 == True):
        cns  = cns + Employee.prime_value_5
    if (Employee.cns_6 == True):
        cns  = cns + Employee.prime_value_6
    if (Employee.cns_7 == True):
        cns  = cns + Employee.prime_value_7
    if (Employee.cns_8 == True):
        cns  = cns + Employee.prime_value_8    
        return cns


def calculateirg():
    irg = 0 
    if (Employee.irg_1 == True):
        irg  = irg + Employee.prime_value_1
    if (Employee.irg_2 == True):
        irg  = irg + Employee.prime_value_2
    if (Employee.irg_3 == True):
        irg  = irg + Employee.prime_value_3
    if (Employee.irg_4 == True):
        irg  = irg + Employee.prime_value_4
    if (Employee.irg_5 == True):
        irg  = irg + Employee.prime_value_5
    if (Employee.irg_6 == True):
        irg  = irg + Employee.prime_value_6
    if (Employee.irg_7 == True):
        irg  = irg + Employee.prime_value_7
    if (Employee.irg_8 == True):
        irg  = irg + Employee.prime_value_8
        return irg    



def calculate_NET(irg,cns):
    SB = Employee.base_salary
    SB = SB - irg - cns
    SB = SB + (Employee.prime_value_1) + (Employee.prime_value_2) + (Employee.prime_value_3) + (Employee.prime_value_4) + (Employee.prime_value_5)
    + (Employee.prime_value_6)+ (Employee.prime_value_7) + (Employee.prime_value_8)
    return SB





