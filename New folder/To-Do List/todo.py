import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.root.configure(bg="#e0f7fa")  # Light cyan background

        # Title Label
        self.title_label = tk.Label(self.root, text="My To-Do List", bg="#e0f7fa", font=("Arial", 20, "bold"), fg="#00796b")
        self.title_label.pack(pady=10)

        # Create the Listbox
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12), bg="#ffffff", selectbackground="#80deea")
        self.task_listbox.pack(pady=10)

        # Create the Entry widget
        self.task_entry = tk.Entry(self.root, width=52, font=("Arial", 12), bg="#ffffff", borderwidth=2)
        self.task_entry.pack(pady=10)

        # Create Buttons Frame
        self.button_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.button_frame.pack(pady=10)

        # Create the Add Task button
        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, bg="#4caf50", fg="white", font=("Arial", 12))
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        # Create the Remove Task button
        self.remove_task_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task, bg="#f44336", fg="white", font=("Arial", 12))
        self.remove_task_button.pack(side=tk.LEFT, padx=5)

        # Create the Clear List button
        self.clear_list_button = tk.Button(self.button_frame, text="Clear List", command=self.clear_list, bg="#ff9800", fg="white", font=("Arial", 12))
        self.clear_list_button.pack(side=tk.LEFT, padx=5)

        # Footer Label
        self.footer_label = tk.Label(self.root, text="Stay organized!", bg="#e0f7fa", font=("Arial", 10, "italic"), fg="#004d40")
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Clear the entry box
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def clear_list(self):
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()