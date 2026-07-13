# Productivity Suite

A multi-feature productivity desktop application built in Python. It integrates a focus timer, task manager, budget tracker, and calendar into a single cohesive tool, utilizing gamification elements to make personal organization more engaging.

## Features

* **Focus Timer:** A countdown timer utilizing Python's `time` module to manage focused work sessions.
* **Task Manager:** Allows users to add, remove, and view tasks, complete with category classification and difficulty ratings.
* **Budget Tracker:** Logs income and expenses, tracks monthly budgets, and generates spending summaries.
* **Interactive Calendar:** A month-view calendar interface built with CustomTkinter featuring dynamic month-to-month navigation.
* **Gamification System:** Features an underlying points economy where users earn points for completing tasks (scaled by difficulty) and lose/receive reduced points for exceeding budget limits.

## Tech Stack
* **Language:** Python 3
* **GUI Framework:** CustomTkinter
* **Data Persistence:** JSON file storage (for tasks, financial logs, budgets, and user points)
* **Core Modules:** `datetime`, `calendar`, `json`, `time`

## Installation & Setup

1. **Prerequisites:** Ensure you have Python 3 installed on your system.
2. **Install Dependencies:** Install the required GUI library via pip:
   ```
   pip install customtkinter
   ```
3. Run the Application: Execute the main script from your terminal:
   ```
   python "main.py"
   ```

## Project Status
Active development.

## What I Learned & Key Technical Challenges
•	Architecture & State Management: Evaluated the trade-offs between class-based and function-based structures to properly manage state persistence across multiple sub-applications.
•	Data Persistence & Serialization: Managed file I/O operations using nested JSON structures. Handled the serialization and deserialization of datetime objects to strings and back.
•	Defensive Programming: Implemented deep copies instead of mutating original data structures directly to prevent live data corruption during runtime.
•	GUI Development: Built dynamic layouts in CustomTkinter, mastering the process of clearing and redrawing widgets dynamically (specifically for the calendar month transitions).
•	Control Flow Debugging: Solved complex loop control challenges by properly utilizing flags and breaking out of multi-level application menus.
