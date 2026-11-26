# School Marketing Management System

**Course:** PROG211 — Object-Oriented Programming 1  
**Language:** Python 3  
**Database:** SQLite

## Overview
This console application helps a school's marketing/admissions team manage prospective student enquiries (student leads). It stores contact details, programme interest, and how each lead heard about the school.

## Features
- Register a prospective student
- Display all leads
- Search by unique lead ID
- Update existing details
- Delete a record after confirmation
- Save data in SQLite so records remain after the program closes
- Validate required fields and age; prevent duplicate IDs

## Files
- `main.py` — menu, validation, `StudentLead` class and user interaction
- `database.py` — SQLite connection and CRUD functions
- `REPORT.md` — technical report and test plan
- `sample_data.txt` — fictional sample data
- `.gitignore` — excludes database/cache files

The `school_marketing.db` database is created automatically the first time the program runs. It is generated locally and is not included in Git.

## Requirements
Python 3.10 or later recommended. No third-party packages are needed.

## Run
Open a terminal in this folder and run:
```bash
python main.py
```
On Windows, `py main.py` may also work.

## Sample data
Use fictional data only. Example: `LEAD001`, Amina Kamara, age 19, Software Engineering, source `School open day`. Avoid putting real private student information into a public repository.

## OOP concepts
`StudentLead` models a prospective student. `__init__()` initializes an object, `summary()` is an instance method, and `from_database_row()` is a class method.

## Limitations
This is an educational local prototype, not a production admissions system. It has no login, role permissions, campaign analytics, encrypted storage, or multi-user network access.
