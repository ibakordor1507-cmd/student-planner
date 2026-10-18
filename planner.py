import streamlit as st

# Custom App Title
st.title("📚 Student Study & Notes Planner")
st.write("A simple academic helper for students of all classes.")

st.markdown("---")

# ---------------------------------------------------------
# STEP 1: SUBJECT & TOPIC SELECTION
# ---------------------------------------------------------
st.header("1. Select Your Course / Subject")

# Pre-defined list of common subjects
default_subjects = ["English", "Mathematics", "Science", "Social Studies", "Law / Political Science", "Computer / Python", "Other Custom Subject"]
selected_subject = st.selectbox("Choose a subject:", default_subjects)

# If user chooses "Other Custom Subject", allow custom input
if selected_subject == "Other Custom Subject":
    selected_subject = st.text_input("Type your custom subject name:")

topic_name = st.text_input("Enter Topic Title (e.g., Chapter 1, Contract Act, Photosynthesis):")

st.markdown("---")

# ---------------------------------------------------------
# STEP 2: USER NOTES & EASY SUMMARISER
# ---------------------------------------------------------
st.header("2. Paste Your Study Notes")

# Multi-line text area for students to paste raw notes
user_notes = st.text_area("Paste your textbook or class notes here:", height=150)

# Summarise Action Button
if st.button("✨ Summarise Notes"):
    if user_notes.strip() == "":
        st.warning("Please paste some notes first before summarising!")
    else:
        st.subheader("📌 Key Summary & Key Points")
        
        # BASIC PYTHON SUMMARISER LOGIC (Syllabus: Strings & Loops)
        # 1. Split text into individual sentences based on periods
        sentences = user_notes.split(".")
        
        # 2. Extract key non-empty sentences
        summary_points = []
        for sentence in sentences:
            clean_sentence = sentence.strip()
            # Collect meaningful sentences that aren't too short
            if len(clean_sentence) > 15:
                summary_points.append(clean_sentence)
        
        # 3. Display summary points clearly
        st.success(f"**Subject:** {selected_subject} | **Topic:** {topic_name if topic_name else 'General Notes'}")
        
        if summary_points:
            st.write("Here are the core takeaways from your notes:")
            for point in summary_points[:4]:  # Takes top 4 key sentences
                st.write(f"• {point}.")
        else:
            st.info("Your notes were very short! Here is your saved note:")
            st.write(f"• {user_notes}")

st.markdown("---")
st.caption("💡 *Phase 1 Version: Keeps things simple, lightweight, and easy to explain during your presentation.*")