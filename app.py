import streamlit as st

# Title of the app
st.title("Computer Organization & Design Quiz")
st.write("Test your understanding of CPU design, MIPS datapath, and control signals!")

# Initialize session state variables if they don’t exist
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# Questions and answers
quiz = [
     # Introduction to Memory Architecture
    {"question": "What is the fundamental unit of data in computer memory?",
     "options": ["Byte", "Word", "Bit", "Register"],
     "answer": "Bit"},

    {"question": "Why is a single, large memory unit inefficient?",
     "options": ["Increases latency", "Increases power consumption", "Decreases storage capacity", "Reduces processing speed"],
     "answer": "Increases latency"},

    {"question": "What is the key trade-off in memory architecture?",
     "options": ["Size vs. Speed", "Power vs. Durability", "Volatility vs. Cost", "Capacity vs. Cooling"],
     "answer": "Size vs. Speed"},

    # Memory Types
    {"question": "Which of the following is an example of primary memory?",
     "options": ["Hard Disk", "Cache", "USB Drive", "CD-ROM"],
     "answer": "Cache"},

    {"question": "What type of memory is used for permanent data storage?",
     "options": ["RAM", "Cache", "HDD", "Register"],
     "answer": "HDD"},

    {"question": "Which memory type is fastest but most expensive?",
     "options": ["SRAM", "DRAM", "Flash", "HDD"],
     "answer": "SRAM"},

    {"question": "What is the primary advantage of DRAM over SRAM?",
     "options": ["Lower cost", "Faster speed", "Requires no refreshing", "Better energy efficiency"],
     "answer": "Lower cost"},

    # RAM and Cache
    {"question": "What does RAM stand for?",
     "options": ["Random Access Memory", "Read-Only Memory", "Rapid Allocation Memory", "Removable Access Memory"],
     "answer": "Random Access Memory"},

    {"question": "Which type of RAM requires periodic refreshing?",
     "options": ["SRAM", "DRAM", "Flash", "EEPROM"],
     "answer": "DRAM"},

    {"question": "Why do processors use cache memory?",
     "options": ["To store all data permanently", "To reduce access time for frequently used data", "To replace main memory", "To improve disk performance"],
     "answer": "To reduce access time for frequently used data"},

    {"question": "How does cache memory improve CPU efficiency?",
     "options": ["By storing frequently accessed data closer to the processor", "By increasing available RAM", "By reducing power consumption", "By replacing secondary storage"],
     "answer": "By storing frequently accessed data closer to the processor"},

    # Volatility
    {"question": "What type of memory loses data when power is turned off?",
     "options": ["Non-volatile", "Persistent", "Volatile", "Flash"],
     "answer": "Volatile"},

    {"question": "Which memory retains data even when power is lost?",
     "options": ["RAM", "Cache", "HDD", "SRAM"],
     "answer": "HDD"},

    # Hard Disk Access
    {"question": "Why is HDD access slower than RAM?",
     "options": ["Magnetic storage latency", "Smaller size", "Higher data density", "Sequential-only access"],
     "answer": "Magnetic storage latency"},

    {"question": "Which component moves to access different parts of a Hard Disk?",
     "options": ["Register", "Read/Write Head", "ALU", "Controller"],
     "answer": "Read/Write Head"},

    {"question": "Why does HDD access involve sequential movement?",
     "options": ["Due to the spinning platter and mechanical read/write head", "Because data is stored in a queue", "To optimize cache usage", "To minimize CPU workload"],
     "answer": "Due to the spinning platter and mechanical read/write head"},

    # OS and Memory Management
    {"question": "What role does the operating system play in memory management?",
     "options": ["Manages data transfer between memory levels", "Directly executes programs", "Controls CPU frequency", "Formats storage devices"],
     "answer": "Manages data transfer between memory levels"},

    {"question": "Which technique allows OS to use secondary memory as an extension of RAM?",
     "options": ["Cache Mapping", "Disk Scheduling", "Virtual Memory", "Write Buffering"],
     "answer": "Virtual Memory"},

    {"question": "What is paging in memory management?",
     "options": ["Copying files between disks", "Dividing memory into fixed-size blocks", "Increasing CPU clock speed", "Compressing data in cache"],
     "answer": "Dividing memory into fixed-size blocks"},

    {"question": "What is demand paging?",
     "options": ["Loading memory pages only when needed", "Preloading all program data", "Using registers to access cache", "Optimizing RAM speed"],
     "answer": "Loading memory pages only when needed"},

    # Performance Factors
    {"question": "What factor affects memory performance the most?",
     "options": ["Clock speed", "Cache size", "Access latency", "Number of registers"],
     "answer": "Access latency"},

    {"question": "Which of the following improves memory performance?",
     "options": ["Increasing cache size", "Using HDD instead of SSD", "Reducing CPU speed", "Decreasing RAM size"],
     "answer": "Increasing cache size"},

    {"question": "How does increasing CPU speed impact memory performance?",
     "options": ["Requires faster memory access", "Reduces cache efficiency", "Slows down virtual memory", "Decreases RAM capacity"],
     "answer": "Requires faster memory access"}
]

# Display the current question
current_question = quiz[st.session_state.question_index]
st.write(f"**Question {st.session_state.question_index + 1}: {current_question['question']}**")

# Multiple-choice options
selected_option = st.radio("Select your answer:", current_question["options"], key=f"question_{st.session_state.question_index}")

# Submit button to evaluate the selected answer
if st.button("Submit Answer") and not st.session_state.answer_submitted:
    if selected_option == current_question["answer"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. The correct answer is: {current_question['answer']}")
    st.session_state.answer_submitted = True

# Next button (enabled only after an answer is submitted)
if st.session_state.answer_submitted:
    if st.button("Next Question"):
        if st.session_state.question_index < len(quiz) - 1:
            st.session_state.question_index += 1
            st.session_state.answer_submitted = False
            # Force rerun to display the next question immediately
            st.rerun()
        else:
            st.write("### Quiz Completed!")
            st.write(f"Your final score is {st.session_state.score}/{len(quiz)}")
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False

st.write(f"**Current Score:** {st.session_state.score}")
