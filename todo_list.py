import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def delete_all_tasks():
    if messagebox.askquestion("Confirm", "Are you sure you want to delete all tasks?") == "yes":
        listbox.delete(0, tk.END)        


def update_task():
    try:
        selected_task_index = listbox.curselection()[0]
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def exit_app(root):
    if messagebox.askquestion("Confirm", "Are you sure you want to exit?") == "yes":
        root.destroy()        


def main():
    global entry, listbox
    root = tk.Tk()
    root.configure(background="dark grey")
    root.title("My To-Do List")
    root.geometry("400x450")  

    header_label = tk.Label(root, text="----- To-Do List -----", font=("Arial", 20, "bold"), bg="dark grey" , fg="black")
    header_label.pack(side=tk.TOP, pady=10)

    entry = tk.Entry(root, width=40, bg="#FAEBD7", fg="black")
    entry.pack(pady=10)

    listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg="#FAEBD7", fg="black")
    listbox.pack()
 
    add_button = tk.Button(root, text="Add Task" , command=add_task, bg="light green", fg="black" , width=20, height=1)
    add_button.pack(pady=5)

    update_button = tk.Button(root, text="Update Task", command=update_task, bg="light green", fg="black", width=20, height=1)
    update_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="light green", fg="black", width=20, height=1)
    delete_button.pack(pady=5)

    delete_all_button = tk.Button(root, text="Delete All Tasks", command=delete_all_tasks, bg="light green", fg="black", width=20, height=1)
    delete_all_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=lambda: exit_app(root), bg="light green", fg="black", width=20, height=1)
    exit_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
