import streamlit as st

# Set page layout and title
st.set_page_config(page_title="Python Syllabus Helper", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Quiz Hub")
st.write("Welcome! This simple tool helps you review concepts and test your knowledge based on your syllabus.")

# Sidebar navigation using simple conditional structures (Unit II)
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Intro & Operators",
        "Unit II: Control & Logic",
        "Unit III: Functions & Data Structures",
        "Interactive Syllabus Quiz"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Tip: Select a topic above to practice syllabus concepts.")

# ---------------------------------------------------------
# UNIT I: Introduction to Python
# Concepts: Input/Output, Variables, Data Types, Operators
# ---------------------------------------------------------
if choice == "Unit I: Intro & Operators":
    st.header("Unit I: Introduction & Basic Operators")
    st.write("Learn how variables, data types, and arithmetic operators work in Python.")

    st.subheader("1. Variable Inspector & Basic Calculations")
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter First Number (Float/Int):", value=10.0, step=1.0)
        num2 = st.number_input("Enter Second Number (Float/Int):", value=5.0, step=1.0)

    with col2:
        st.write("**Data Types:**")
        st.code(f"type({num1}) -> {type(num1).__name__}\ntype({num2}) -> {type(num2).__name__}")

    st.subheader("2. Basic Operators Demo")
    if num2 != 0:
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2
        modulo = num1 % num2

        st.write(f"- **Addition (`+`):** `{num1} + {num2} = {addition}`")
        st.write(f"- **Subtraction (`-`):** `{num1} - {num2} = {subtraction}`")
        st.write(f"- **Multiplication (`*`):** `{num1} * {num2} = {multiplication}`")
        st.write(f"- **Division (`/`):** `{num1} / {num2} = {division:.2f}`")
        st.write(f"- **Modulo (`%`):** `{num1} % {num2} = {modulo}`")
    else:
        st.warning("Division and modulo require the second number to be non-zero.")

# ---------------------------------------------------------
# UNIT II: Control Structures & Exception Handling
# Concepts: Conditionals, Loops, Pattern Programs, Exceptions
# ---------------------------------------------------------
elif choice == "Unit II: Control & Logic":
    st.header("Unit II: Control Structures & Logic")

    st.subheader("1. Grade Evaluator (Conditional Statements)")
    score = st.slider("Select Student Marks (0 to 100):", min_value=0, max_value=100, value=75)

    if score >= 90:
        grade = "A+ (Outstanding)"
    elif score >= 75:
        grade = "A (Very Good)"
    elif score >= 60:
        grade = "B (Good)"
    elif score >= 40:
        grade = "C (Pass)"
    else:
        grade = "F (Fail)"

    st.success(f"Score: **{score}** | Result: **{grade}**")

    st.markdown("---")
    st.subheader("2. Pattern Generator (Loops & Nested Loops)")
    rows = st.number_input("Enter Number of Rows for Pattern:", min_value=1, max_value=10, value=5)

    pattern_type = st.selectbox("Select Pattern Style:", ["Star Triangle", "Number Pyramid"])

    pattern_output = ""
    if pattern_type == "Star Triangle":
        for i in range(1, rows + 1):
            pattern_output += "*" * i + "\n"
    elif pattern_type == "Number Pyramid":
        for i in range(1, rows + 1):
            pattern_output += (str(i) + " ") * i + "\n"

    st.code(pattern_output, language="text")

    st.markdown("---")
    st.subheader("3. Safe Division (Exception Handling)")
    val_a = st.text_input("Numerator:", value="10")
    val_b = st.text_input("Denominator:", value="0")

    if st.button("Execute Safe Division"):
        try:
            res = float(val_a) / float(val_b)
            st.success(f"Result: {res}")
        except ZeroDivisionError:
            st.error("Exception Caught: `ZeroDivisionError` — Cannot divide by zero!")
        except ValueError:
            st.error("Exception Caught: `ValueError` — Please enter valid numerical inputs.")

# ---------------------------------------------------------
# UNIT III: Functions & Data Structures
# Concepts: Functions, Strings, Lists, Tuples, Dicts, Sets
# ---------------------------------------------------------
elif choice == "Unit III: Functions & Data Structures":
    st.header("Unit III: Functions & Data Structures")

    # Helper function demonstration
    def analyze_text(text):
        char_count = len(text)
        word_count = len(text.split())
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in text if char in vowels)
        return char_count, word_count, vowel_count

    st.subheader("1. String Analysis (Using Functions)")
    user_string = st.text_area("Enter any text snippet:", "Python programming is fun and structured.")

    if user_string:
        c_count, w_count, v_count = analyze_text(user_string)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Characters", c_count)
        col2.metric("Total Words", w_count)
        col3.metric("Vowel Count", v_count)

    st.markdown("---")
    st.subheader("2. Data Structure Operations")

    ds_type = st.radio("Select Data Structure:", ["List", "Tuple", "Dictionary", "Set"])

    if ds_type == "List":
        sample_list = ["Python", "Variables", "Loops", "Functions"]
        st.write("**Sample List:**", sample_list)
        new_item = st.text_input("Add new item to list:", "Data Structures")
        if st.button("Append Item"):
            sample_list.append(new_item)
            st.write("**Updated List:**", sample_list)

    elif ds_type == "Tuple":
        sample_tuple = ("Unit I", "Unit II", "Unit III")
        st.write("**Sample Tuple (Immutable):**", sample_tuple)
        st.info(f"First element: `{sample_tuple[0]}` | Length: `{len(sample_tuple)}`")

    elif ds_type == "Dictionary":
        syllabus_dict = {
            "Unit I": "Introduction & Operators",
            "Unit II": "Control Structures",
            "Unit III": "Functions & Data Structures"
        }
        st.write("**Syllabus Map (Keys & Values):**", syllabus_dict)

    elif ds_type == "Set":
        sample_set = {"Loops", "Functions", "Variables", "Loops"} # Duplicate automatically removed
        st.write("**Sample Set (Unique Elements Only):**", sample_set)

# ---------------------------------------------------------
# INTERACTIVE QUIZ MODULE
# ---------------------------------------------------------
elif choice == "Interactive Syllabus Quiz":
    st.header("📝 Python Syllabus Knowledge Check")

    quiz_score = 0

    q1 = st.radio(
        "1. Which of the following data structures is immutable?",
        ["List", "Dictionary", "Tuple", "Set"]
    )
    if q1 == "Tuple":
        quiz_score += 1

    q2 = st.radio(
        "2. Which keyword is used in Python to handle exceptions?",
        ["try / except", "do / catch", "if / else", "error / handle"]
    )
    if q2 == "try / except":
        quiz_score += 1

    q3 = st.radio(
        "3. What operator is used for calculating remainder in Python?",
        ["/", "//", "%", "**"]
    )
    if q3 == "%":
        quiz_score += 1

    if st.button("Submit Answers"):
        st.subheader(f"Your Final Score: {quiz_score} / 3")
        if quiz_score == 3:
            st.balloons()
            st.success("Excellent! Perfect score on syllabus fundamentals.")
        else:
            st.info("Good attempt! Review Units I-III and try again.")