"""
Student Performance Analytics System
Run: python main.py
"""
from pathlib import Path
from functions import (
    load_student_data, add_performance_columns, get_overall_summary,
    get_subject_summary, get_top_students, get_department_summary
)

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "students.csv"
OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    try:
        students = load_student_data(DATA_FILE)
        analyzed = add_performance_columns(students)
    except (FileNotFoundError, ValueError) as error:
        print(f"Could not start the analysis: {error}")
        return

    summary = get_overall_summary(analyzed)
    subject_summary = get_subject_summary(analyzed)
    top_students = get_top_students(analyzed)
    department_summary = get_department_summary(analyzed)

    print("\\n" + "=" * 65)
    print("          STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 65)
    print(f"Records loaded: {len(students)}")
    print(f"Dataset columns: {', '.join(students.columns)}")

    print("\\n1. STUDENT RESULTS")
    print(analyzed[["Student_ID", "Name", "Department", "Total_Marks",
                    "Average_Marks", "Grade", "Result", "Attendance"]].to_string(index=False))

    print("\\n2. CLASS SUMMARY")
    for label, value in summary.items():
        print(f"{label.replace('_', ' ').title()}: {value}")

    print("\\n3. SUBJECT-WISE SUMMARY")
    print(subject_summary.to_string(index=False))

    print("\\n4. TOP 5 STUDENTS")
    print(top_students[["Student_ID", "Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))

    print("\\n5. DEPARTMENT SUMMARY")
    print(department_summary.to_string(index=False))

    # Save output tables so the results can be inspected or included in documentation.
    analyzed.to_csv(OUTPUT_DIR / "student_results.csv", index=False)
    subject_summary.to_csv(OUTPUT_DIR / "subject_summary.csv", index=False)
    department_summary.to_csv(OUTPUT_DIR / "department_summary.csv", index=False)
    print(f"\\nSaved output CSV files in: {OUTPUT_DIR}")
    print("Analysis completed successfully.")

if __name__ == "__main__":
    main()
