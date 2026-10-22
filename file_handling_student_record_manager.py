import json
from pathlib import Path

FILE_NAME = Path("students.json")


def load_records():
    if not FILE_NAME.exists():
        return []

    try:
        with FILE_NAME.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Error reading student records.")
        return []


def save_record(name, marks):
    records = load_records()

    record = {
        "name": name,
        "marks": marks
    }

    records.append(record)

    try:
        with FILE_NAME.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        print(f"Record saved for {name}.")

    except OSError as error:
        print(f"Error saving record: {error}")


def display_records():
    records = load_records()

    if not records:
        print("No student records found.")
        return

    for index, student in enumerate(records, start=1):
        print(
            f"{index}. {student['name']} "
            f"- Marks: {student['marks']}"
        )


if __name__ == "__main__":
    save_record("Ali", 85)
    save_record("Sara", 92)
    display_records()
