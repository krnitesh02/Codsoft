import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Selected", command=remove_task)
task_list = tk.Listbox(root, selectmode=tk.SINGLE)

task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
task_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()