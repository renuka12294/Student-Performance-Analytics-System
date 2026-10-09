# Student Performance Analytics System

## 1. Project Overview

The Student Performance Analytics System is a Python-based application designed to analyze student academic performance. It uses Pandas and NumPy to process student marks, calculate averages, assign grades, and generate performance reports. A Streamlit web interface allows users to view student information and analysis.

## 2. Objectives

* Analyze student marks and attendance.
* Calculate total marks and average scores.
* Assign grades based on student averages.
* Identify pass and fail students.
* Display subject-wise performance.
* Identify top-performing students.
* Generate reports for further analysis.

## 3. Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* CSV dataset

## 4. Dataset

The project uses a CSV file named `students.csv` containing student information and academic scores.

Dataset fields include:

* Student ID
* Name
* Gender
* Department
* Mathematics marks
* Science marks
* English marks
* Computer marks
* Attendance

## 5. Key Features

* Student performance analysis
* Total and average marks calculation
* Grade assignment
* Pass/fail classification
* Class performance summary
* Subject-wise average analysis
* Top student identification
* Interactive dashboard
* Student records display
* Downloadable reports, if enabled in the application

## 6. Project Structure

```text
student_performance_analytics_system/
│
├── main.py
├── functions.py
├── app.py
├── students.csv
├── README.md
├── Project_Documentation.docx
├── screenshots/
└── output/
```

## 7. Installation

Install Python first. Open a terminal in the project folder and run:

```bash
python -m pip install pandas numpy streamlit
```

## 8. How to Run

### Run the Python analysis

```bash
python main.py
```

### Run the Streamlit web application

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal, usually:

`http://localhost:8501`

## 9. Sample Results

Based on the original sample dataset:

* Total students: 20
* Class average: 68.72
* Highest student average: 94
* Lowest student average: 36
* Students passed: 18
* Students failed: 2
* Pass percentage: 90%

Results may change when the dataset is updated.

## 10. Future Enhancements

* Add new student records through the web interface.
* Add student search and filtering.
* Improve dashboard visualizations.
* Generate downloadable performance reports.
* Add more detailed attendance analysis.

## 11. Conclusion

The Student Performance Analytics System demonstrates how Python, Pandas, NumPy, and Streamlit can be used to analyze student academic data and present useful performance information through reports and a web dashboard.
