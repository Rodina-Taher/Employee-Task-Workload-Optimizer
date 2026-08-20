class Employee:
    def __init__(self,name,skills,available_hours):
        self.name=name
        self.skills=skills
        self.available_hours=available_hours
        self.current_workload=0
    def add_task(self,task):
        self.current_workload+=task.estimated_hours
    def can_take_task(self,task):
        return self.current_workload+task.estimated_hours<=self.available_hours
    def has_required_skills(self,task):
        employee_skills=[skill.lower() for skill in self.skills]
        required_skills=[skill.lower() for skill in task.required_skills]
        return all(skill in self.skills for skill in task.required_skills)
    def get_workload_precentage(self):
        return (self.current_workload/self.available_hours)*100
    def get_status(self):
        precentage=self.get_workload_precentage()
        if precentage>=100:
            return "Full"
        elif precentage>=75:
            return "Busy"
        else:
            return "Available"
    def display_summary(self):
        print(self.name,"| Workload:",round(self.get_workload_precentage(),1),"%","| Status",self.get_status())