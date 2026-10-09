import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide"
)

st.sidebar.title("🎓 Student Analytics")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Dashboard", "Student Records", "Reports"]
)

st.title("Student Performance Analytics System")
st.write("Analyze student marks, attendance, grades, and academic performance.")

file_path = Path(__file__).parent / "students.csv"

if not file_path.exists():
    st.error("students.csv was not found.")
    st.stop()

df = pd.read_csv(file_path)
subjects = ["Maths", "Science", "English", "Computer"]

missing = [col for col in subjects if col not in df.columns]
if missing:
    st.error(f"Missing columns: {missing}")
    st.write("Available columns:", list(df.columns))
    st.stop()

df[subjects] = df[subjects].apply(pd.to_numeric, errors="coerce")
df["Average"] = df[subjects].mean(axis=1).round(2)

if page == "Home":
    st.header("Welcome to the Home Page")
    st.write("A student analytics project using Python and Pandas.")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Students", len(df))
    c2.metric("Class Average", round(df["Average"].mean(), 2))
    c3.metric("Highest Average", round(df["Average"].max(), 2))

    st.subheader("Student Data Preview")
    st.dataframe(df.head(10), use_container_width=True)

elif page == "Dashboard":
    st.header("Performance Dashboard")
    c1, c2 = st.columns(2)
    c1.metric("Highest Average", round(df["Average"].max(), 2))
    c2.metric("Lowest Average", round(df["Average"].min(), 2))

    st.subheader("Student-wise Average")
    st.bar_chart(df.set_index("Name")["Average"])

    st.subheader("Subject-wise Average")
    st.bar_chart(df[subjects].mean())

elif page == "Student Records":
    st.header("Student Records")
    search = st.text_input("Search student by name")
    filtered = df[
        df["Name"].astype(str).str.contains(search, case=False, na=False)
    ]
    st.dataframe(filtered, use_container_width=True)

elif page == "Reports":
    st.header("Download Reports")
    st.download_button(
        "Download Student Report",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="student_performance_report.csv",
        mime="text/csv"
    )
