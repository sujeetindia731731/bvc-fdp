import streamlit as st

st.set_page_config(page_title="Marks to Grade", layout="centered")

st.title("Student Marks — Percentage & Grade Calculator")

st.write("Enter marks for five subjects (0-100).")

with st.form("marks_form"):
    m1 = st.number_input("Subject 1", min_value=0.0, max_value=100.0, step=0.5)
    m2 = st.number_input("Subject 2", min_value=0.0, max_value=100.0, step=0.5)
    m3 = st.number_input("Subject 3", min_value=0.0, max_value=100.0, step=0.5)
    m4 = st.number_input("Subject 4", min_value=0.0, max_value=100.0, step=0.5)
    m5 = st.number_input("Subject 5", min_value=0.0, max_value=100.0, step=0.5)
    submitted = st.form_submit_button("Calculate")

def grade_from_percentage(pct: float) -> str:
    if pct >= 90:
        return "A+"
    if pct >= 80:
        return "A"
    if pct >= 70:
        return "B"
    if pct >= 60:
        return "C"
    if pct >= 50:
        return "D"
    return "F"

if submitted:
    marks = [m1, m2, m3, m4, m5]
    total = sum(marks)
    percentage = total / 5.0
    grade = grade_from_percentage(percentage)

    st.subheader("Result")
    st.write(f"Total Marks: {total:.2f} / 500")
    st.write(f"Percentage: {percentage:.2f}%")
    st.write(f"Grade: {grade}")
    if percentage >= 40 and all(m >= 33 for m in marks):
        st.success("Status: Pass")
    else:
        st.error("Status: Fail")

    st.write("---")
    st.subheader("Marks Breakdown")
    # Prepare per-subject breakdown: subject number, marks, percentage (out of 100), grade
    breakdown = []
    for i, m in enumerate(marks, start=1):
        pct_sub = (m / 100.0) * 100.0
        grade_sub = grade_from_percentage(pct_sub)
        breakdown.append({
            "Subject": f"Subject {i}",
            "Marks": f"{m:.2f}",
            "Percentage": f"{pct_sub:.2f}%",
            "Grade": grade_sub,
        })

    st.table(breakdown)
