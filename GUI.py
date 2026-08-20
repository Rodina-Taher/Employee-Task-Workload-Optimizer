import tkinter as tk
from tkinter import ttk
from employee import Employee
from task import Task
from optimizer import find_suitable_employee
from data_manager import save_employees
from data_manager import save_employees, save_tasks
from tkinter import messagebox

def create_gui(employees,tasks):
    window=tk.Tk()
    window.title("Employee Task & Workload Optimizer")
    window.geometry("1000x850")
    canvas=tk.Canvas(window)
    scrollbar=tk.Scrollbar(window,orient="vertical",command=canvas.yview)
    content_frame=tk.Frame(canvas)
    content_frame.bind("<Configure>",lambda event:canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0,0),window=content_frame,anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left",fill="both",expand=True)
    scrollbar.pack(side="right",fill="y")
    title_label=tk.Label(content_frame,text="Employee Task & Workload Optimizer",font=("Arial",24,"bold"))
    title_label.pack(pady=20)
    assigned_count=sum(1 for task in tasks if task.assigned_employee)
    unassigned_count=len(tasks)-assigned_count
    summary_label=tk.Label(content_frame,text=("Employees: "+str(len(employees))+"   |   Tasks:"+str(len(tasks))+"   |   Assigned: "+str(assigned_count)+"   |   Unassigned: "+str(unassigned_count)),font=("Arial",12,"bold"))
    summary_label.pack(pady=5)
    employee_label=tk.Label(content_frame,text="Employee Workload",font=("Arial",18,"bold"))
    employee_label.pack(pady=10)
    employee_frame=tk.Frame(content_frame, relief="groove",borderwidth=2)
    employee_frame.pack(pady=10)
    def refresh_employees():
        for widget in employee_frame.winfo_children():
            widget.destroy()
        for employee in employees:
            employee_card=tk.Label(employee_frame,relief="groove",borderwidth=1,padx=20,pady=8)
            employee_card.pack(pady=5)
            employee_info=tk.Label(employee_card,text=(employee.name + " | Workload:" + str(round(employee.get_workload_precentage(),1)) + "%"),font=("Arial",12))
            employee_info.pack(side="left",padx=10)
            workload_bar=ttk.Progressbar(employee_card, orient="horizontal",length=150,mode="determinate",maximum=100,value=min(employee.get_workload_precentage(),100))
            workload_bar.pack(side="left",padx=10)
            status_label=tk.Label(employee_card,text="Status:"+ employee.get_status(),font=("Arial",12,"bold"),padx=10)
            status_label.pack(side="left",padx=10)
    refresh_employees()
    add_employee_frame=tk.Frame(content_frame,relief="groove",borderwidth=2,padx=15,pady=10)
    add_employee_frame.pack(pady=10)
    add_employee_label=tk.Label(add_employee_frame,text="Add Employee",font=("Arial",14,"bold"))
    add_employee_label.pack()
    input_frame=tk.Frame(add_employee_frame)
    input_frame.pack(pady=10)
    name_label=tk.Label(add_employee_frame,text="Name")
    name_label.pack(side="left",padx=5)
    name_entry=tk.Entry(add_employee_frame,width=15)
    name_entry.pack(side="left",padx=10)
    skills_label = tk.Label(add_employee_frame, text="Skills (please seperate with commas)")
    skills_label.pack(side="left",padx=5)
    skills_entry=tk.Entry(add_employee_frame,width=30)
    skills_entry.pack(side="left",pady=10)
    hours_label = tk.Label(add_employee_frame, text="Available Hours")
    hours_label.pack(side="left",padx=5)
    hours_entry=tk.Entry(add_employee_frame,width=10)
    hours_entry.pack(side="left",padx=10)
    def add_employee():
        name=name_entry.get().strip()
        skills_text=skills_entry.get().strip()
        hours_text=hours_entry.get().strip()
        if not name or not skills_text or not hours_text:
            messagebox.showwarning("Missing Information", "Please fill in all employee fields.")
            return
        try:
            available_hours=int(hours_text)
        except ValueError:
            messagebox.showerror("Invalid Hours","Available hours must be a number.")
            return
        if available_hours <= 0:
            messagebox.showerror("Invalid Hours","Available hours must be greater than 0.")
            return
        skills=[skill.strip() for skill in skills_text.split(",")]
        new_employee=Employee(name,skills,available_hours)
        employees.append(new_employee)
        save_employees(employees)
        refresh_employees()
        print("Employee added:",new_employee.name)
    add_employee_button=tk.Button(add_employee_frame,text="Add Employee",command=add_employee)
    add_employee_button.pack(pady=5)
    add_task_frame=tk.Frame(content_frame,relief="groove",borderwidth=2,padx=15,pady=10)
    add_task_frame.pack(pady=10)
    add_task_label=tk.Label(add_task_frame,text="Add Task", font=("Arial",14,"bold"))
    add_task_label.pack()
    task_input_frame=tk.Frame(add_task_frame)
    task_input_frame.pack(pady=10)
    title_label=tk.Label(task_input_frame,text="Title")
    title_label.pack(side="left",padx=10)
    title_entry=tk.Entry(task_input_frame,width=20)
    title_entry.pack(side="left",padx=10)
    required_skills_label=tk.Label(task_input_frame,text="Required Skills")
    required_skills_label.pack(side="left",padx=5)
    required_skills_entry=tk.Entry(task_input_frame,width=25)
    required_skills_entry.pack(side="left",padx=10)
    task_hours_label=tk.Label(task_input_frame,text="Hours")
    task_hours_label.pack(side="left",padx=5)
    task_hours_entry=tk.Entry(task_input_frame,width=8)
    task_hours_entry.pack(side="left",padx=10)
    priority_label=tk.Label(task_input_frame,text="Priority")
    priority_label.pack(side="left",padx=5)
    priority_var=tk.StringVar(value="Medium")
    priority_menu=tk.OptionMenu(task_input_frame,priority_var,"High","Medium","Low")
    priority_menu.pack(side="left",padx=10)
    deadline_label=tk.Label(task_input_frame,text="Deadline")
    deadline_label.pack(side="left",padx=5)
    deadline_entry=tk.Entry(task_input_frame,width=12)
    deadline_entry.pack(side="left",padx=10)
    def add_task():
        title=title_entry.get().strip()
        skills_text=required_skills_entry.get().strip()
        hours_text=task_hours_entry.get().strip()
        priority=priority_var.get()
        deadline=deadline_entry.get().strip()
        if not title or not skills_text or not hours_text or not deadline:
            messagebox.showwarning("Missing Information","Please fill in all task fields.")
        try:
            estimated_hours=int(hours_text)
        except ValueError:
            messagebox.showerror("Invalid Hours","Estimated hours must be a number.")
            return
        if estimated_hours <= 0:
            messagebox.showerror("Invalid Hours","Estimated hours must be greater than 0.")
            return
        required_skills=[skill.strip() for skill in skills_text.split(",")]
        new_task=Task(title,required_skills,estimated_hours,priority,deadline)
        tasks.append(new_task)
        save_tasks(tasks)
        refresh_tasks()
        print("Task added:",new_task.title)
    add_task_button=tk.Button(add_task_frame,text="Add Task",command=add_task)
    add_task_button.pack(pady=5)
    #run_optimizer
    priority_order={"High": 1,"Medium": 2,"Low": 3}

    def run_optimizer():
        unassigned_tasks=[task for task in tasks if task.assigned_employee is None]
        unassigned_tasks.sort(key=lambda task: priority_order[task.priority])
        for task in unassigned_tasks:
            suitable_employee=find_suitable_employee(employees,task)
            if suitable_employee:
                suitable_employee.add_task(task)
                task.assigned_employee=suitable_employee
        save_employees(employees)
        save_tasks(tasks)
        refresh_employees()
        refresh_tasks()

    run_button = tk.Button(content_frame, text="Run Optimizer", command=run_optimizer, font=("Arial", 12, "bold"))
    run_button.pack(pady=15)
    #task_assignment
    task_label=tk.Label(content_frame,text="Task Assignments",font=("Arial",18,"bold"))
    task_label.pack(pady=15)
    task_frame=tk.Frame(content_frame,relief='groove',borderwidth=2,padx=20,pady=10)
    task_frame.pack(pady=5)
    def refresh_tasks():
        for widget in task_frame.winfo_children():
            widget.destroy()
        for task in tasks:
            task_card=tk.Frame(task_frame,relief="groove",borderwidth=1,padx=15,pady=8)
            task_card.pack(pady=5, fill="x")
            task_title=tk.Label(task_card,text=task.title,font=("Arial",12,"bold"))
            task_title.pack(anchor="w")
            assigned_name=(task.assigned_employee.name if task.assigned_employee else "No suitable employee")
            task_details=tk.Label(task_card,text=("Priority:"+ task.priority+ " | Hours:"+ str(task.estimated_hours)+ " | Assigned to:"+ assigned_name),font=("Arial",10))
            task_details.pack(anchor="w")
    refresh_tasks()

    window.mainloop()