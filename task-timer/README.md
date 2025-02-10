# Time Tracking Application

This Python-based time tracking application allows users to manage and log time spent on various tasks. It includes features for starting and stopping tasks, viewing time summaries, and editing timesheets.

## Features

- **Start Task**: Begin tracking time for a specific task.
- **Stop Task**: End a running task and log the time spent.
- **Summary**: View a summary of all tasks and their accumulated time.
- **Running Tasks**: Display currently active tasks.
- **Edit Timesheet**: Modify the time logged for a specific task.
  
## Requirements

- Python 3.x
- `json` and `os` libraries (part of Python standard library)

## File Structure

- `tasks.json`: This file stores all the tasks and their associated data in JSON format. Each task has a `time_spent` field representing the total time spent on the task, and `start_times` to record each start time for ongoing sessions.
