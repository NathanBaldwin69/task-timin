"""
Time Tracking Application

This script allows users to manage tasks and track the time spent on them. 
It includes functionality to start and stop tasks, view summaries of time spent, 
edit timesheet data, and display a list of currently running tasks. Data is stored 
in a JSON file for persistence across sessions.

Commands:
- start: Begin tracking a task.
- stop: Stop tracking a task and log the time.
- summary: View a summary of all tasks and time spent.
- running: Display currently active tasks.
- edit: Edit the time for a specific task.
- exit: Exit the application.

Author: Nathan Baldwin
Date: February 9, 2025
"""

import datetime
import json
import os

TASK_FILE = "tasks.json"

def display_header():
    """Display the program header with a brief description of the application."""
    print("=" * 50)
    print("Time Tracking Application - Manage your tasks and time")
    print("Start, stop, edit, and track time spent on your tasks.")
    print("=" * 50)

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns: dict: A dictionary containing all tasks and their time data.
    """
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return {}

def save_tasks(tasks):
    """
    Save the provided tasks to the JSON file.
    Args: tasks (dict): The dictionary containing task data to be saved.
    """
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def start_task(task_name):
    """
    Start tracking a task by adding a start time to the task.
    Args: task_name (str): The name of the task to start tracking.
    """
    tasks = load_tasks()

    if task_name not in tasks:
        tasks[task_name] = {"time_spent": 0, "start_times": []}
        
    tasks[task_name]["start_times"].append(datetime.datetime.now())
    save_tasks(tasks)

    print(f"Started task: {task_name}")

def stop_task(task_name):
    """
    Stop tracking a task and calculate the time spent on it.  
    Args: task_name (str): The name of the task to stop tracking.
    """
    tasks = load_tasks()
    
    if task_name not in tasks or not tasks[task_name].get("start_times"):
        print(f"Error: Task '{task_name}' is not running.")
        return
        
    start_time = tasks[task_name]["start_times"].pop(0)
    elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
    tasks[task_name]["time_spent"] += elapsed_time
    
    save_tasks(tasks)
    print(f"Stopped task: {task_name}. Time logged: {elapsed_time:.2f} seconds")

def show_summary():
    """Display a summary of all tasks and the time spent on them."""
    tasks = load_tasks()
    print("Time Sheet Summary:")
    
    for task, data in tasks.items():
        time_spent = data["time_spent"] if isinstance(data, dict) and "time_spent" in data else 0
        print(f"{task}: {time_spent:.2f} seconds")

def show_running_tasks():
    """Display a list of currently running tasks."""
    tasks = load_tasks() 
    running_tasks = [task for task, data in tasks.items() if isinstance(data, dict) and data.get("start_times")]
   
    if running_tasks:
        print("Currently running tasks:")
        for task in running_tasks:
            print(f"- {task} ({len(tasks[task]['start_times'])} instance(s) running)")
    else:
        print("No tasks are currently running.")

def edit_timesheet():
    """Allow the user to edit the time recorded for a specific task."""
    tasks = load_tasks()
    show_summary()
    task_name = input("Enter the task you want to edit: ").strip()
    
    if task_name not in tasks:
        print("Error: Task not found.")
        return
    
    new_time = input(f"Enter new time for '{task_name}': ").strip()
    
    if not new_time.isdigit():
        print("Error: Please enter a valid number.")
        return
    
    tasks[task_name]["time_spent"] = float(new_time)
    save_tasks(tasks)
    print(f"Updated time for '{task_name}' to {new_time} seconds.")

def main():
    """
    Run the time tracking application.
    Continuously prompt the user to input commands until 'exit' is entered.
    """
    display_header()
    
    while True:
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
