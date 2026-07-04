# Productivity Suite
A multi-feature productivity app built in Python, combining a focus timer, task manager, budget tracker, and calendar into one tool — with RPG-style gamification layered on top to make tracking productivity more engaging.


## Features
Focus Timer — countdown timer for focused work sessions, built with time
Task Manager — add, remove, and view tasks with category and difficulty ratings
Budget Tracker — log income and expenses, set monthly budgets, and view spending summaries against your budget
Calendar — month-view calendar built with CustomTkinter, with navigation between months
RPG Gamification — [add a short description of this once it's finalised, e.g. "earn points/XP for completing tasks based on difficulty"]


## Tech Stack
Language: Python
GUI: CustomTkinter
Libraries: datetime, calendar, json, time
Data persistence: JSON file storage for tasks, completed tasks, income/expenses, and budgets


## How to Run
Make sure Python 3 is installed
Install CustomTkinter:

   pip install customtkinter

Run the main script:

   python draft 3.py

## Status
Actively evolving as a personal project.

## What I Learned
Structuring related features (timer, tasks, budget, calendar) using classes vs. functions depending on whether state needs to persist
Managing file I/O and JSON for saving/loading data between sessions
Building GUI layouts with CustomTkinter, including dynamic redrawing of widgets (e.g. calendar view on month change)
Debugging loop control issues (break vs. continue vs. flag variables) in multi-level menus
