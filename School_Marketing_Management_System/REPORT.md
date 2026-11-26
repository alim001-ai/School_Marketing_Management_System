# Technical Report: School Marketing Management System

## 1. Introduction
The School Marketing Management System is a Python console application for organizing prospective student enquiries. Schools may receive enquiries from social media, radio, referrals, open days, school visits, and other campaigns. This prototype stores those leads in one local database for easier record keeping and follow-up. Use fictional/sample information for demonstrations.

## 2. Aim and objectives
**Aim:** To build a simple system for storing and managing prospective student enquiries.

**Objectives:**
1. Register prospective students and their programme interests.
2. Display all saved records.
3. Search using a unique lead ID.
4. Update existing records.
5. Delete records with confirmation.
6. Persist information using SQLite.
7. Demonstrate a Python class, objects, an instance method, a class method, and modular design.

## 3. Main features
- **Register:** captures ID, full name, age, programme, optional phone, and enquiry source.
- **Display:** lists records alphabetically by name.
- **Search:** finds one record by ID.
- **Update:** changes selected fields while retaining fields left blank.
- **Delete:** asks the user to confirm before deleting.
- **Validation:** checks required fields and age (5–120).
- **Persistence:** stores records in a local SQLite database.

## 4. Object-oriented programming
The `StudentLead` class models one prospective student. Each object stores the lead ID, name, age, programme, phone, and enquiry source.
- `__init__()` initializes a new object.
- `summary()` is an instance method that uses the object's attributes to format a summary.
- `from_database_row()` is decorated with `@classmethod` and creates an object from a database row.

## 5. Database design
The project uses Python's built-in SQLite support. The `students` table contains:

| Field | Type | Purpose |
|---|---|---|
| `student_id` | TEXT primary key | Unique lead identifier |
| `full_name` | TEXT not null | Prospective student's name |
| `age` | INTEGER not null | Age constrained to 5–120 |
| `programme` | TEXT not null | Programme of interest |
| `phone` | TEXT | Optional phone number |
| `interest` | TEXT not null | Campaign/channel/source of enquiry |

Parameterized SQL statements use placeholders (`?`) for values. The primary key prevents duplicate IDs.

## 6. Program structure
- `main.py` provides the class, menu, prompts, validation, and user interaction.
- `database.py` handles database connections and create/read/update/delete operations.
- `README.md` documents setup and execution.
- `REPORT.md` explains the design and testing plan.

## 7. Testing plan
Perform these tests on the computer and record the actual outcomes before submission. These are expected results, not a claim that every test has already been manually performed.

| Test | Action | Expected result |
|---|---|---|
| 1 | Run `python main.py` for the first time | Database/table are created |
| 2 | Register a valid lead | Success message and saved record |
| 3 | Reuse an existing ID | Duplicate ID is rejected |
| 4 | Display all leads | Stored records are listed |
| 5 | Search for an existing ID | Matching record appears |
| 6 | Search for unknown ID | No-record message appears |
| 7 | Update an existing lead | Changes are saved |
| 8 | Enter letters for age | Validation requests a whole number |
| 9 | Delete and confirm with `YES` | Record is removed |
| 10 | Restart and display leads | Records remain available |
| 11 | Enter invalid menu option | Error message appears and menu continues |

## 8. Limitations and future improvements
The prototype has no authentication, roles, campaign automation, conversion-rate tracking, or analytics. The local database is not designed for sensitive production data or simultaneous use across multiple computers. Future improvements could include login, follow-up dates, campaign reports, CSV export, and a graphical interface. A real deployment would require appropriate privacy, access-control, backup, and data-protection safeguards.

## 9. Conclusion
The system demonstrates a menu-driven Python application using object-oriented programming, input validation, modular database functions, and SQLite persistence. It can be extended with more advanced school marketing functions.

## 10. References
1. Python Software Foundation, *Python 3 Documentation*: https://docs.python.org/3/
2. Python Software Foundation, *sqlite3 — DB-API 2.0 interface for SQLite databases*: https://docs.python.org/3/library/sqlite3.html
3. SQLite, *SQLite Documentation*: https://www.sqlite.org/docs.html
