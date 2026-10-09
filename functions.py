"""
Reusable functions for the Student Performance Analytics System.
"""
import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Science", "English", "Computer"]

def load_student_data(file_path):
    """Load the CSV file into a Pandas DataFrame and validate required columns."""
    df = pd.read_csv(file_path)
    required = ["Student_ID", "Name", "Gender", "Department", *SUBJECTS, "Attendance"]
    missing = [column for column in required if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df.empty:
        raise ValueError("The student dataset is empty.")
    return df

def add_performance_columns(df):
    """Calculate total, average, grade, and pass/fail status for every student."""
    result = df.copy()
    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = result[SUBJECTS].mean(axis=1).round(2)

    grades = []
    statuses = []
    # Loop through each student's subject marks.
    for _, student in result.iterrows():
        average = student["Average_Marks"]
        all_subjects_pass = all(student[subject] >= 35 for subject in SUBJECTS)

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        # Passing requires at least 35 in every subject.
        status = "Pass" if all_subjects_pass else "Fail"
        grades.append(grade)
        statuses.append(status)

    result["Grade"] = grades
    result["Result"] = statuses
    return result

def get_overall_summary(df):
    """Return key class-level statistics using Pandas and NumPy."""
    averages = df["Average_Marks"].to_numpy()
    return {
        "student_count": int(len(df)),
        "class_average": round(float(np.mean(averages)), 2),
        "highest_average": round(float(np.max(averages)), 2),
        "lowest_average": round(float(np.min(averages)), 2),
        "pass_count": int((df["Result"] == "Pass").sum()),
        "fail_count": int((df["Result"] == "Fail").sum()),
        "pass_percentage": round(float((df["Result"] == "Pass").mean() * 100), 2),
        "average_attendance": round(float(np.mean(df["Attendance"].to_numpy())), 2),
    }

def get_subject_summary(df):
    """Calculate the average, highest, and lowest mark for each subject."""
    rows = []
    for subject in SUBJECTS:
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(df[subject].to_numpy())), 2),
            "Highest": int(df[subject].max()),
            "Lowest": int(df[subject].min()),
        })
    return pd.DataFrame(rows)

def get_top_students(df, number=5):
    """Return the top students ranked by average marks."""
    return df.sort_values(
        by=["Average_Marks", "Name"], ascending=[False, True]
    ).head(number)

def get_department_summary(df):
    """Compare average marks and student counts by department."""
    return (
        df.groupby("Department", as_index=False)
          .agg(Student_Count=("Student_ID", "count"),
               Average_Marks=("Average_Marks", "mean"))
          .assign(Average_Marks=lambda data: data["Average_Marks"].round(2))
          .sort_values("Average_Marks", ascending=False)
    )
