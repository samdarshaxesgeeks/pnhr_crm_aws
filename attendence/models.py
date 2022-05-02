# from django.db import models
# from employees.models import Employee
# from datetime import datetime

# # Create your models here.


# def cal_time(time1, time2):

#     return time2 - time1



# class Attendence(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
 
#     time1 = models.DateTimeField()

#     time2 = models.DateTimeField()

#     cal_time = cal_time(time1, time2)
    
#     def __str__(self):
#         return self.employee.name