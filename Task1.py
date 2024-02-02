import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import json
import os

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.load_tasks()

        # Create GUI elements
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=15, width=40)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=5)

        # Display tasks in the listbox
        self.display_tasks()

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task['title'])

    def add_task(self):
        title = simpledialog.askstring("Input", "Enter task title:")
        if title:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_task = {"title": title, "date": date}
            self.tasks.append(new_task)
            self.save_tasks()
            self.display_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            new_title = simpledialog.askstring("Input", "Enter the new task title:")
            if new_title:
                self.tasks[task_index]["title"] = new_title
                self.save_tasks()
                self.display_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            deleted_task = self.tasks.pop(task_index)
            self.save_tasks()
            self.display_tasks()
            messagebox.showinfo("Task Deleted", f"Task '{deleted_task['title']}' deleted successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
