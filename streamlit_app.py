import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/students/"

st.set_page_config(page_title="Student Management", layout="centered")
st.title("🎓 Student Management Dashboard")

menu = ["Create", "Read All", "Read One", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

# --- Create ---
if choice == "Create":
    st.subheader("Add New Student")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0)
    enrolled_date = st.date_input("Enrolled Date")

    if st.button("Add"):
        data = {
            "name": name,
            "email": email,
            "age": age,
            "enrolled_date": str(enrolled_date)
        }
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            st.success("Student added successfully!")
        else:
            st.error(f"Failed to add student: {response.text}")

# --- Read All ---
elif choice == "Read All":
    st.subheader("All Students")
    response = requests.get(API_URL)
    if response.status_code == 200:
        students = response.json()
        st.table(students)
    else:
        st.error(f"Failed to fetch students. Status Code: {response.status_code}")

# --- Read One ---
elif choice == "Read One":
    st.subheader("Get Student by ID")
    student_id = st.number_input("Student ID", min_value=1, step=1)
    if st.button("Fetch"):
        response = requests.get(f"{API_URL}{student_id}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error(f"Failed to fetch student with ID {student_id}: {response.text}")

# --- Update ---
elif choice == "Update":
    st.subheader("Update Student Info")
    student_id = st.number_input("Student ID to Update", min_value=1, step=1)
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    age = st.number_input("New Age", min_value=0)
    enrolled_date = st.date_input("New Enrolled Date")

    if st.button("Update"):
        data = {
            "name": name,
            "email": email,
            "age": age,
            "enrolled_date": str(enrolled_date)
        }
        response = requests.put(f"{API_URL}{student_id}", json=data)
        if response.status_code == 200:
            st.success("Student updated successfully!")
        else:
            st.error(f"Failed to update student: {response.text}")

# --- Delete ---
elif choice == "Delete":
    st.subheader("Delete Student")
    student_id = st.number_input("Student ID to Delete", min_value=1, step=1)
    if st.button("Delete"):
        response = requests.delete(f"{API_URL}{student_id}")
        if response.status_code == 200:
            st.success("Student deleted successfully!")
        else:
            st.error(f"Failed to delete student with ID {student_id}: {response.text}")
