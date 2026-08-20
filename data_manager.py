import json
from employee import Employee
from task import Task

def save_employees(employees):
    data=[]
    for employee in employees:
        data.append({"name": employee.name,"skills": employee.skills,"available_hours": employee.available_hours,"current_workload" : employee.current_workload})
    with open("employees.json","w") as file:
        json.dump(data,file, indent=4)

def load_employees():
    try:
        with open("employees.json","r") as file:
            data=json.load(file)
        employees=[]
        for item in data:
            employee=Employee(item["name"],item["skills"],item["available_hours"])
            employees.append(employee)
        return employees
    except FileNotFoundError:
        return []
# task
def save_tasks(tasks):
    data=[]
    for task in tasks:
        data.append({"title": task.title,"required_skills": task.required_skills,"estimated_hours":task.estimated_hours,"priority":task.priority,"deadline":task.deadline,"assigned_employess":(task.assigned_employee.name if task.assigned_employee else None)})
    with open("tasks.json","w") as file:
        json.dump(data,file, indent=4)

def load_tasks(employees):
    try:
        with open("tasks.json","r") as file:
            data=json.load(file)
        tasks=[]
        for item in data:
            task=Task(item["title"],item["required_skills"],item["estimated_hours"],item["priority"],item["deadline"])
            if item.get("assigned_employee"):
                for employee in employees:
                    if employee.name == item.get("assigned_employee"):
                        task.assigned_employee=employee
                        employee.add_task(task)
                        break
            tasks.append(task)
        return tasks
    except FileNotFoundError:
        return []