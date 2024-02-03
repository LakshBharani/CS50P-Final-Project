# FINAL PROJECT
# Name            : LAKSH BHARANI
# Course          : CS50P
# Project Title   : Todo List Manager
# From            : Bengaluru, Karnatak, India
# Submission date : January 3rd 2024
# Linkedin        : https://www.linkedin.com/in/laksh-bharani-41953b210/

# import tabulate module to neatly tabulate data
from tabulate import tabulate

# initialize tasks list with headers
tasks = [["Task ID", "Task Label", "Task Description", "Task Priority", "Task Status"]]

# main fucntion of the program
def main():
    print("\n============================\nWelcome to the Todo List App\n============================")
    print(tabulate(tasks,headers='firstrow',tablefmt='fancy_grid'), "\n")
    while True:
        print("[1] Add task")
        print("[2] View tasks")
        print("[3] Update task")
        print("[4] Delete task")
        print("[5] Quit")
        choice = input("Enter your choice: ")
        show_menu(choice)

# function to show menu
def show_menu(choice):
    # add task
    if choice == "1":
        print("\nAdd Task\n")
        task_id = len(tasks)
        task_label = ""
        while task_label == "":
            task_label = input("Task Label: ").title()
            if task_label == "":
                print("Label cannot be empty.")
        task_description = input("Task Description: ")
        if len(task_description) > 0:
            task_description = task_description[0].upper() + task_description[1:]
        task_priority = input("Task Priority (H/M/L): ").upper()
        task_status = "N"
        add_task(task_id, task_label, task_description, task_priority, task_status)
        print("\nTask added.\n")
        # using tabulate module to neatly tabulate data
        print(tabulate(tasks,headers='firstrow',tablefmt='fancy_grid'), "\n")

    # view tasks
    elif choice == "2":
        view_tasks()

    # update task
    elif choice == "3":
        print("\nUpdate Task\n")
        print(tabulate(tasks,headers='firstrow',tablefmt='fancy_grid'), "\n")
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("\nInvalid task ID. Try again.\n")
            return False
        task_status = input("Task Status (Y/N): ").upper()
        if task_status not in ["Y", "N"]:
            print("Invalid choice. Try again.")
            return False
        update_task(task_id, task_status)
        print("\nTask updated.\n")
        print(tabulate(tasks,headers='firstrow',tablefmt='fancy_grid'), "\n")

    # delete task
    elif choice == "4":
        print("\nDelete Task\n")
        print(tabulate(tasks,headers='firstrow',tablefmt='fancy_grid'), "\n")
        task_id = int(input("Enter task ID: "))
        delete_task(tasks, task_id)
        print("\nTask deleted.\n")
        print(tabulate(tasks,headers='firstrow',tablefmt='fancy_grid'), "\n")

    elif choice == "5":
        print("\nThank you for using the Todo List App.\n")
        quit()
    else:
        print("\nInvalid choice. Try again.\n")

# function to add task
def add_task(task_id, task_label, task_description, task_priority, task_status):
    # check if task id, label, priority and status are not empty
    if str(task_id) != "" and task_label != "" and task_priority != "" and task_status != "":
        tasks.append([task_id, task_label, task_description, task_priority, task_status])
        return True
    else:
        return False

# function to view tasks
def view_tasks():
    print("\nViewing Tasks\n")
    view_priority_wise = input("View priority (H/M/L): ").upper()
    if view_priority_wise == "H":
        print(tabulate([tasks[0], *[task for task in tasks if task[3] == "H"]],headers='firstrow',tablefmt='fancy_grid'), "\n")
    elif view_priority_wise == "M":
        print(tabulate([tasks[0], *[task for task in tasks if task[3] == "M"]],headers='firstrow',tablefmt='fancy_grid'), "\n")
    elif view_priority_wise == "L":
        print(tabulate([tasks[0], *[task for task in tasks if task[3] == "L"]],headers='firstrow',tablefmt='fancy_grid'), "\n")
    else:
        print("\nInvalid choice. Try again.\n")

# function to update task
def update_task(task_id, task_status):
    # check if task id and status are not empty
    if str(task_id) != "" and task_status != "":
        tasks[task_id][4] = task_status
        return True
    else:
        return False

# function to delete task
def delete_task(tasks, task_id):
    try:
        tasks.pop(task_id)
    except IndexError:
        print("\nInvalid task ID. Try again.\n")
    return tasks

# call main function
if __name__ == "__main__":
    main()

