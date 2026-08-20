from employee import Employee
from task import Task
from GUI import create_gui
from data_manager import load_employees, load_tasks

#employees
employee1=Employee("Sarah",["Python","Data Analysis"],8)
employee2=Employee("Ahmed",["Python","Machine Learning"],10)
employee3=Employee("Maya",["Python","Data Analysis","Machine Learning"],12)

#tasks
task1=Task("Analyze Sales Data",["Python","Data Analysis"],6,"High","2026-8-18")
task2=Task("Build Machine Learing Model", ["Python","Machine Learning"],5,"High","2026-08-19")
task3=Task("Prepare Sales Report",["Python","Data Analysis"],4,"Medium","2026-08-20")
task4=Task("Fix Critical Database Issue",["Python"],3,"High","2026-08-15")
task5=Task("Develop AI Dashboard",["Python","Machine Learning"],10,"Medium","2026-08-22")

#tasks list
tasks=[task1,task2,task3,task4,task5]


#listofemployees
employees=load_employees()
if not employees:
    employees = [employee1,employee2,employee3]

tasks=load_tasks(employees)
if not tasks:
    tasks = [task1,task2,task3,task4,task5]
#creategui call function
create_gui(employees,tasks)

