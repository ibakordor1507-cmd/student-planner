import streamlit as st

# Custom Header
st.title("🎓 Student Academic Planner & Tracker")
st.caption("A streamlined dashboard for managing internal assessments, attendance, and study tasks.")

# ---------------------------------------------------------
# MODULE 1: ATTENDANCE CALCULATOR (Operators & Conditionals)
# ---------------------------------------------------------
st.header("1. Attendance Eligibility Checker")

col1, col2 = st.columns(2)
with col1:
    classes_held = st.number_input("Total Classes Conducted:", min_value=1, value=40, step=1)
with col2:
    classes_attended = st.number_input("Classes Attended:", min_value=0, value=32, step=1)

# Formula Calculation
if classes_attended > classes_held:
    st.error("Attended classes cannot exceed total classes conducted.")
else:
    attendance_pct = (classes_attended / classes_held) * 100
    st.metric("Current Attendance", f"{attendance_pct:.1f}%")
    
    # Threshold checks
    if attendance_pct >= 75:
        st.success("✅ Eligible for semester/trimester end examinations.")
    elif attendance_pct >= 65:
        st.warning("⚠️ Below 75%. You may require medical condonation or extra remedial classes.")
    else:
        st.error("🚨 Critically Low Attendance. Contact academic administration.")

st.markdown("---")

# ---------------------------------------------------------
# MODULE 2: INTERNAL ASSESSMENT TRACKER (Data Structures & Loops)
# ---------------------------------------------------------
st.header("2. Internal Assessment (IA) Score Log")

# Data structure: List of Tuples -> (Subject, Assessment_Name, Score, Max_Score)
ia_records = [
    ("Law of Contract / Core I", "1st Internal Test", 16, 20),
    ("Law of Contract / Core I", "Mid-Term Essay", 18, 20),
    ("Constitutional Law", "Project Presentation", 14, 20),
    ("Python Programming", "Lab Evaluation 1", 19, 20),
]

# Using SETS to get unique subject list for dropdown filter
subjects = list(set([item[0] for item in ia_records]))
subjects.sort()
subjects.insert(0, "All Subjects")

selected_subject = st.selectbox("Filter Scores by Subject:", subjects)

# Search & Filter Logic
total_obtained = 0
total_max = 0
displayed_count = 0

st.subheader("Logged Assessment Results")
for sub, test_name, marks, max_m in ia_records:
    if selected_subject == "All Subjects" or selected_subject == sub:
        st.info(f"**{sub}** — {test_name}: **{marks} / {max_m}**")
        total_obtained += marks
        total_max += max_m
        displayed_count += 1

# Summary Metrics
if total_max > 0:
    overall_pct = (total_obtained / total_max) * 100
    st.write(f"**Cumulative Internal Average:** `{overall_pct:.2f}%` ({total_obtained}/{total_max} marks)")

st.markdown("---")

# ---------------------------------------------------------
# MODULE 3: TASK & DEADLINE MANAGER (Functions & Exception Handling)
# ---------------------------------------------------------
st.header("3. Assignment & Study Task Planner")

# Function to parse priority styling
def get_priority_badge(priority_level):
    if priority_level == "High":
        return "🔴 High Priority"
    elif priority_level == "Medium":
        return "🟡 Medium Priority"
    else:
        return "🟢 Low Priority"

# Task input form
with st.form("task_form"):
    task_name = st.text_input("Task / Subject Module Title:")
    priority = st.select_slider("Select Priority:", options=["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Task")

# Processing Input safely
try:
    if submitted:
        if task_name.strip() == "":
            st.warning("Please enter a valid task title before submitting.")
        else:
            badge = get_priority_badge(priority)
            st.success(f"Task Added: **{task_name}** | Status: {badge}")
except Exception as e:
    st.error("An unexpected error occurred while processing the task input.")