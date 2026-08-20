class Task:
    def __init__(self,title, required_skills,estimated_hours,priority,deadline):
        self.title=title
        self.required_skills=required_skills
        self.estimated_hours=estimated_hours
        self.priority=priority
        self.deadline=deadline
        self.assigned_employee=None