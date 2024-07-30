import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Error", "Please enter a task")

def remove_task():
    task_listbox.delete(tk.ANCHOR)

root = tk.Tk()
root.geometry("520x470+520+220")
root.title("Task Manager")
root.config(bg="#87CEEB")
root.resizable(width=True, height=True)

main_frame = tk.Frame(root, bg="#87CEEB")
main_frame.pack(pady=20, expand=True, fill=tk.BOTH)

task_listbox = tk.Listbox(
    main_frame, 
    width=30, 
    height=10, 
    font=('Arial', 16), 
    bd=0, 
    fg='#1E90FF', 
    highlightthickness=0, 
    selectbackground='#4682B4', 
    activestyle="none"
)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tasks = [ 'Exercise', 'Meditate','Study']
for t in tasks:
    task_listbox.insert(tk.END, t)

scrollbar = tk.Scrollbar(main_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

task_entry = tk.Entry(root, font=('Arial', 20))
task_entry.pack(pady=25, fill=tk.X, padx=20)

button_frame = tk.Frame(root, bg="#87CEEB")
button_frame.pack(pady=25)

add_btn = tk.Button(
    button_frame, 
    text='Add Task', 
    font=('Arial', 14), 
    bg='#4682B4', 
    padx=20, 
    pady=5, 
    command=add_task
)
add_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=10)

remove_btn = tk.Button(
    button_frame, 
    text='Remove Task', 
    font=('Arial', 14), 
    bg='#4682B4', 
    padx=20, 
    pady=5, 
    command=remove_task
)
remove_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT, padx=10)

root.mainloop()
