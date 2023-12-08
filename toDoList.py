import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Create and set up the task list
        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
        self.task_list.pack(pady=10)

        # Create and set up the entry widget for new tasks
        self.new_task_entry = tk.Entry(root, width=40)
        self.new_task_entry.pack(pady=5)

        # Create and set up buttons
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack(pady=5)

    def add_task(self):
        new_task = self.new_task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.task_list.insert(tk.END, new_task)
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.task_list.delete(selected_task_index)
            del self.tasks[selected_task_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()
