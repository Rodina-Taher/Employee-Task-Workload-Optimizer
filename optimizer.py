def find_suitable_employee(employees,task):
    suitable_employees=[]
    for employee in employees:
        if employee.can_take_task(task) and employee.has_required_skills(task):
            suitable_employees.append(employee)
    if suitable_employees:
        return min(suitable_employees,key=lambda employee: employee.current_workload/employee.available_hours)
    return None
def explain_task_assignment(employees,task):
    reasons=[]
    for employee in employees:
        if not employee.has_required_skills(task):
            reasons.append(employee.name+" -Missing required skills")
        elif not employee.can_take_task(task):
            reasons.append(employee.name+" -Not enough capacity")
        else:
            reasons.append(employee.name+"- Suitable")
    return reasons