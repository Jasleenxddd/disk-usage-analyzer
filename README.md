# Disk Usage Analyzer (CLI Utility)

## Overview
This project is a small command-line utility built using Python that helps identify which files or sub-directories consume the most disk space within a given folder. It solves a real problem I face on my system—quickly understanding disk usage without manually inspecting each directory.

The tool uses only Python’s standard libraries and focuses on clean coding practices, error handling, and clear output formatting.

---

## a. Problem Being Solved

Over time, folders on a system accumulate large files and directories such as build artifacts, logs, dependencies, or downloaded media. Manually identifying which items consume the most storage is time-consuming and inefficient.

This utility automates that process by:
- Scanning a specified directory
- Calculating the total size of each file and sub-directory
- Sorting the results by size
- Displaying the largest items in a readable format

This helps users quickly locate storage-heavy items and manage disk space effectively.

---

## b. How to Run the Program

### Prerequisites
- Python 3 installed on the system

### Steps to Run

1. Download or clone the project and open the folder in a terminal or VS Code.
2. Ensure the file `disk_analyzer.py` is present.
3. Run the program using the following command:

```bash
python disk_analyzer.py <path_to_directory>
```
## Sample Output

Below is an example of the program output showing the largest files and directories in a folder.

### Command-Line Interface (CLI)
The screenshot below shows the output of the CLI version of the tool, displaying the largest files and directories within a specified folder.

<img width="638" height="163" alt="image" src="https://github.com/user-attachments/assets/f5f97a18-5373-4ea8-819b-94042a7b1766" />

### Graphical User Interface (GUI)
The screenshot below shows the GUI version of the tool, which provides a simple interface for selecting a directory and viewing disk usage results.

<img width="603" height="415" alt="image" src="https://github.com/user-attachments/assets/eeb575f4-e4a2-463d-b2ae-693194aac3fe" />

