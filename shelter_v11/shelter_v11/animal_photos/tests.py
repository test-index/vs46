# from django.test import TestCase
#
# # Create your tests here.
#
#
# class PayrollSystem:
#     def calculate_payroll(self, employees):
#         print('Calculating Payroll')
#         print('===================')
#         for employee in employees:
#             print(f'Payroll for: {employee.id} - {employee.name}')
#             print(f'- Check amount: {employee.calculate_payroll()}')
#             print('')
#
#
# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#
# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
# empl = SalaryEmployee(123,'smbd', 123)
# empl_2 = SalaryEmployee(456, 'smn', 789)
# empl_3 = Employee(123, 'smmmb')
# p_sys = PayrollSystem()
# print(p_sys.calculate_payroll([empl, empl_2]))
#
# class HourlyEmployee(Employee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
# class Secretary(SalaryEmployee):
#     def work(self, hours):
#         print(f'{self.name} expends {hours} hours doing office paperwork.')
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
#
# class VolumeMixin:
#     def volume(self):
#         return self.area() * self.height
#
# class Cube(VolumeMixin, Square):
#     def __init__(self, length):
#         super().__init__(length)
#         self.height = length
#
#     def face_area(self):
#         return super().area()
#
#     def surface_area(self):
#         return super().area() * 6
#
# zz =1
# square = Square(4)
# cube = Cube(2)
# print(cube.surface_area())
# print(cube.volume())