import time
import json
import os

TASK_FILE = "tasks.json"

def display_header():
    print("=" * 50)
    print("Time Tracking Application - Manage your tasks and time")
    print("Start, stop, edit, and track time spent on your tasks.")
    print("=" * 50)

# manage reading and writing tasks
def load_tasks():
    # check if file exists, if so read content
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return {}

# save tasks to json file
def save_tasks(tasks):
    # write to file, overwrite if exists
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# track time of given tasks
def start_task(task_name):
    # load task
    tasks = load_tasks()
    # check if task already exists
    if task_name not in tasks:
        tasks[task_name] = {"time_spent": 0, "start_times": []}
    # add a new start time
    tasks[task_name]["start_times"].append(time.time())
    save_tasks(tasks)
    print(f"Started task: {task_name}")

# stop running task and calculate time elipsed
def stop_task(task_name):
    # load given task
    tasks = load_tasks()
    # check if task exists and is running
    if task_name not in tasks or not tasks[task_name].get("start_times"):
        print(f"Error: Task '{task_name}' is not running.")
        return
    # stop the most recent start time
    start_time = tasks[task_name]["start_times"].pop(0)
    elapsed_time = time.time() - start_time
    tasks[task_name]["time_spent"] += elapsed_time
    
    save_tasks(tasks)
    print(f"Stopped task: {task_name}. Time logged: {elapsed_time:.2f} seconds")

# print summary of tasks
def show_summary():
    # retrieve data and print title
    tasks = load_tasks()
    print("Time Sheet Summary:")
    # loop through tasks and print data
    for task, data in tasks.items():
        time_spent = data["time_spent"] if isinstance(data, dict) and "time_spent" in data else 0
        print(f"{task}: {time_spent:.2f} seconds")

# display list of current running tasks
def show_running_tasks():
    # load task
    tasks = load_tasks()
    # find running tasks
    running_tasks = [task for task, data in tasks.items() if isinstance(data, dict) and data.get("start_times")]
    # print running tasks
    if running_tasks:
        print("Currently running tasks:")
        for task in running_tasks:
            print(f"- {task} ({len(tasks[task]['start_times'])} instance(s) running)")
    else:
        print("No tasks are currently running.")

# edit specific tasks
def edit_timesheet():
    tasks = load_tasks()
    # print summary of task
    show_summary()
    # ask user if they want to edit task
    task_name = input("Enter the task you want to edit: ").strip()
    if task_name not in tasks:
        print("Error: Task not found.")
        return
    # have user change time for given task
    new_time = input(f"Enter new time for '{task_name}': ").strip()
    if not new_time.isdigit():
        print("Error: Please enter a valid number.")
        return
    # update information
    tasks[task_name]["time_spent"] = float(new_time)
    save_tasks(tasks)
    print(f"Updated time for '{task_name}' to {new_time} seconds.")

# command line interface
def main():
    display_header()
    # loop until user manually exits
    while True:
        # give prompts for function
        command = input("Enter command (start, stop, summary, running, edit, exit): ").strip().lower()
        if command == "start":
            task_name = input("Enter task name: ").strip()
            start_task(task_name)
        elif command == "stop":
            task_name = input("Enter task name: ").strip()
            stop_task(task_name)
        elif command == "summary":
            show_summary()
        elif command == "running":
            show_running_tasks()
        elif command == "edit":
            edit_timesheet()
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
