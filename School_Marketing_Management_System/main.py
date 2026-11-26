"""School Marketing Management System — PROG211 OOP1 educational project."""
from database import (initialize_database, add_student, get_all_students,
                      get_student, update_student, delete_student)


class StudentLead:
    """Represents a prospective student in a school's marketing records."""
    def __init__(self, student_id, full_name, age, programme, phone, interest):
        self.student_id = str(student_id).strip()
        self.full_name = str(full_name).strip()
        self.age = int(age)
        self.programme = str(programme).strip()
        self.phone = str(phone).strip()
        self.interest = str(interest).strip()

    def summary(self):
        """Instance method: format this object's information."""
        return (f"ID: {self.student_id} | Name: {self.full_name} | Age: {self.age} | "
                f"Programme: {self.programme} | Phone: {self.phone or 'Not provided'} | "
                f"Enquiry source: {self.interest}")

    @classmethod
    def from_database_row(cls, row):
        """Class method: create an object from a SQLite row."""
        return cls(row["student_id"], row["full_name"], row["age"],
                   row["programme"], row["phone"], row["interest"])


def read_required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_age():
    while True:
        try:
            age = int(input("Age: ").strip())
            if 5 <= age <= 120:
                return age
            print("Enter an age between 5 and 120.")
        except ValueError:
            print("Please enter a whole number for age.")


def register_student():
    print("\n--- Register Prospective Student ---")
    student_id = read_required("Student/Lead ID: ")
    full_name = read_required("Full name: ")
    age = read_age()
    programme = read_required("Programme of interest: ")
    phone = input("Phone (optional): ").strip()
    interest = read_required("How did they hear about the school? (e.g. social media, radio): ")
    lead = StudentLead(student_id, full_name, age, programme, phone, interest)
    try:
        if add_student(lead.student_id, lead.full_name, lead.age, lead.programme, lead.phone, lead.interest):
            print("Prospective student registered successfully.")
        else:
            print("That ID already exists. Use a different ID.")
    except ValueError as error:
        print(f"Could not register: {error}")


def display_students():
    print("\n--- Prospective Student List ---")
    rows = get_all_students()
    if not rows:
        print("No student leads have been registered yet.")
        return
    for row in rows:
        print(StudentLead.from_database_row(row).summary())


def search_student():
    student_id = read_required("Enter student/lead ID: ")
    row = get_student(student_id)
    print(StudentLead.from_database_row(row).summary() if row else "No record found for that ID.")


def edit_student():
    student_id = read_required("Enter student/lead ID to update: ")
    row = get_student(student_id)
    if row is None:
        print("No record found.")
        return
    current = StudentLead.from_database_row(row)
    print("Press Enter to keep the current value.")
    name = input(f"Full name [{current.full_name}]: ").strip() or None
    age_text = input(f"Age [{current.age}]: ").strip()
    programme = input(f"Programme [{current.programme}]: ").strip() or None
    phone_text = input(f"Phone [{current.phone}]: ").strip()
    interest = input(f"Enquiry source [{current.interest}]: ").strip() or None
    try:
        age = int(age_text) if age_text else None
        phone = phone_text if phone_text else None
        print("Student lead updated successfully." if update_student(
            student_id, full_name=name, age=age, programme=programme,
            phone=phone, interest=interest) else "No record was updated.")
    except ValueError as error:
        print(f"Could not update: {error}")


def remove_student():
    student_id = read_required("Enter student/lead ID to delete: ")
    row = get_student(student_id)
    if row is None:
        print("No record found.")
        return
    confirm = input(f"Delete {row['full_name']}? Type YES to confirm: ").strip()
    if confirm == "YES":
        print("Record deleted." if delete_student(student_id) else "Record could not be deleted.")
    else:
        print("Deletion cancelled.")


def show_menu():
    print("\n" + "=" * 44)
    print(" SCHOOL MARKETING MANAGEMENT SYSTEM")
    print("=" * 44)
    print("1. Register prospective student")
    print("2. Display all prospective students")
    print("3. Search by student/lead ID")
    print("4. Update prospective student")
    print("5. Delete prospective student")
    print("6. Exit")


def main():
    initialize_database()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            print("Thank you for using the School Marketing Management System.")
            break
        else:
            print("Invalid option. Please choose from 1 to 6.")


if __name__ == "__main__":
    main()
