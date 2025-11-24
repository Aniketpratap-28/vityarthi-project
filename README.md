**Project Overview**

- **Project Name**
  - Personal Health Logger (Python CLI)
- **Purpose**
  - A simple command-line interface application written in Python to help users log daily health metrics, including water intake, sleep, exercise, and mood.
- **Persistence**
  - All data is persistently saved in a local text file.

**Core Features**

- **Main Menu Options**
  - 1. **Add Health Entry**
  - 2. **View All Entries**
  - 3. **Exit**
- **Add Health Entry**
  - Records new data for the current day.
  - Prompts for date, water consumption, sleep duration, exercise time, and overall mood sequentially.
- **View All Entries**
  - Displays all historical health entries saved in the log file (`health_log.txt`).
  - Gracefully handles the error if the log file has not yet been created, printing "No entries found. Please add some first."

**Prerequisites and Execution**

- **Prerequisite**
  - Python 3.x is required.
- **How to Run**
  - Save the code into a Python file (e.g., `health_logger.py`).
  - Open the terminal and navigate to the file directory.
  - Execute the script using the command: `python health_logger.py`.

**Input Details**

- **Date Format**
  - Follows the `DD/MM/YYYY` format (e.g., `24/11/2025`).
- **Water Intake Unit**
  - Volume is entered in liters (L).
- **Sleep Hours Unit**
  - Duration is entered in hours.
- **Exercise Minutes Unit**
  - Duration is entered in minutes.
- **Mood Input**
  - A free-form text entry to describe the state (e.g., `Energetic`).

**Data Storage Details**

- **File Used**
  - `health_log.txt`.
- **Location**
  - Located in the same directory as the Python script.
- **Entry Format**
  - Each entry is saved on a new line in the format: `Date: DD/MM/YYYY, Water: X.XL, Sleep: Y.Yhrs, Exercise: Zmins, Mood: [Text]`.

**Potential Enhancements**

- **Data Validation**
  - Add checks to ensure that water, sleep, and exercise inputs are valid numbers.
- **Data Structure Improvement**
  - Switch from saving to a flat text file to a structured format like **CSV** or **JSON** for easier data analysis.
- **Advanced Features**
  - Implement features to **search** for entries by date.
  - Add functionality to **edit** existing entries.
  - Allow users to **calculate averages** (e.g., average sleep over the last week).
- **Error Handling Optimization**
  - Use `with open(...)` statements to ensure files are closed automatically, even if errors occur.
