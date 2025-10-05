class InvalidGradeError(Exception):
    def __init__(self, message):
        super().__init__(message)

def read_student_records(filename):
    try:
        with open(filename, "r") as file:
            students = []
            for line in file:
                name, grade_str = line.strip().split(",")
                name = name.strip()
                grade_str = grade_str.strip()

                try:
                    grade = float(grade_str)
                    students.append((name, grade))
                except ValueError:
                    # Raise custom exception for invalid grade
                    raise InvalidGradeError(f"Invalid grade for student '{name}': {grade_str}")

            return students

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except InvalidGradeError as e:
        print("Error:", e)
        return []

def calculate_average(students):
    if not students:
        return 0
    total = sum(grade for _, grade in students)
    return total / len(students)

def main():
    filename = "student_records.txt"
    students = read_student_records(filename)

    if students:
        average = calculate_average(students)
        print("Student Records:")
        for name, grade in students:
            print(f"{name}: {grade}")
        print(f"\nAverage Grade: {average:.2f}")

if __name__ == "__main__":
    main()
