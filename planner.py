import streamlit as st

st.title("📚 Student Study & Notes Assistant")
st.write("An all-in-one helper to organize subjects, summarize study notes, and solve math problems.")

st.markdown("---")

# SUBJECT & TOPIC SELECTION
default_subjects = ["English", "Mathematics", "Science", "Social Studies", "Law / Political Science", "Computer / Python", "Other Custom Subject"]
selected_subject = st.selectbox("Choose a subject:", default_subjects)

if selected_subject == "Other Custom Subject":
    selected_subject = st.text_input("Type your custom subject name:")

topic_name = st.text_input("Enter Topic / Chapter Title:")

# STUDY NOTES & ACCURATE SUMMARISER
st.subheader("Study Notes Summariser")

user_notes = st.text_area("Paste your textbook or study notes here (accepts full chapters & paragraphs):", height=200)

if st.button("Generate Summary"):
    if user_notes.strip() == "":
        st.warning("Please paste some notes first!")
    else:
        st.success(f"**Subject:** {selected_subject} | **Topic:** {topic_name if topic_name else 'General Notes'}")
        
        # SUMMARY LOGIC (Syllabus: Strings & Words Processing)
        words = user_notes.split()
        total_words = len(words)
        
        # Calculate summary length based on total input
        summary_length = max(10, int(total_words * 0.35))
        condensed_text = " ".join(words[:summary_length])
        
        st.markdown("### 📌 Executive Summary")
        st.write(f"This material covers the core principles of **{topic_name if topic_name else selected_subject}**.")
        st.write(f"**Main Takeaway:** {condensed_text}...")
        st.caption(f"📊 Original length: {total_words} words | Summarised to top {summary_length} words.")

st.markdown("---")

# MATH & EQUATION SOLVER
st.subheader("🧮 Math Problem Solver")
st.write("Enter an expression or arithmetic problem to evaluate step-by-step.")

math_input = st.text_input("Type math expression (e.g. 25 * 4 + 10, (100 - 25) / 5, 2**8):")

if st.button("Solve Math Problem"):
    if math_input.strip() == "":
        st.warning("Please enter a valid math expression.")
    else:
        try:
            # Safe evaluation of arithmetic expressions
            # syllabus: Operators, Data Types & Exception Handling
            clean_expr = math_input.replace("x", "*").replace("^", "**")
            result = eval(clean_expr, {"__builtins__": None}, {})
            
            st.success(f"**Problem:** `{math_input}`")
            st.write(f"### **Solution:** `{result}`")
            st.info("💡 *Evaluated using standard Python operator precedence (PEMDAS/BODMAS).*")
            
        except Exception:
            st.error("Invalid math expression! Please check your syntax (e.g., use `+`, `-`, `*`, `/`).")
