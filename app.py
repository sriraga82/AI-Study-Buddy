
import streamlit as st

st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🎓"
)

st.title("🎓 AI Study Buddy")
st.write("Your Smart Learning Assistant")

st.sidebar.title("Study Assistant")
choice = st.sidebar.selectbox(
    "Choose a feature",
    ["Ask a Question", "Study Tips"]
)

def answer_question(question):
    q = question.lower()

    topics = {
        "python": "Python is a simple, high-level programming language used for web development, automation, data science and AI.",
        "oops": "OOP stands for Object-Oriented Programming. It is a programming approach based on classes and objects. Its four main concepts are Encapsulation, Inheritance, Polymorphism and Abstraction.",
        "dbms": "DBMS stands for Database Management System. It is software used to store, manage, retrieve and organize data. Examples include MySQL and Oracle.",
        "operating system": "An Operating System manages computer hardware and software resources. Examples include Windows, Linux and macOS.",
        "sql": "SQL stands for Structured Query Language. It is used to create, retrieve, update and delete data in relational databases.",
        "artificial intelligence": "Artificial Intelligence is the ability of computer systems to perform tasks that normally require human intelligence, such as learning and problem-solving.",
        "machine learning": "Machine Learning is a branch of AI that enables computers to learn patterns from data and make predictions.",
        "computer network": "A computer network connects computers and devices to share information and resources.",
        "data structure": "A data structure is a way of organizing and storing data efficiently. Examples include arrays, linked lists, stacks and queues."
    }

    for topic, explanation in topics.items():
        if topic in q:
            return explanation

    return (
        "Here is a simple way to study this question:\n\n"
        "1. Understand the definition of the topic.\n"
        "2. Learn its important concepts.\n"
        "3. Study one practical example.\n"
        "4. Revise the main points.\n\n"
        "Try entering a topic such as Python, DBMS, SQL or Operating System "
        "for a prepared explanation."
    )

if choice == "Ask a Question":
    st.header("💬 Ask Your Question")
    question = st.text_area("Enter your academic question")

    if st.button("Get Answer"):
        if question.strip():
            st.subheader("📖 Answer")
            st.success(answer_question(question))
        else:
            st.warning("Please enter a question.")

else:
    st.header("📚 Get Study Tips")
    subject = st.text_input("Enter your subject or topic")

    if st.button("Get Study Tips"):
        if subject.strip():
            st.subheader("✨ Your Study Tips")
            st.info(f"Study suggestions for: {subject}")

            st.write("1. Understand the basic concepts first.")
            st.write("2. Prepare short notes for revision.")
            st.write("3. Study for 30–40 minutes at a time.")
            st.write("4. Practice important questions.")
            st.write("5. Take short breaks between sessions.")
            st.write("6. Revise the topic before sleeping.")
        else:
            st.warning("Please enter a subject.")

st.divider()
st.caption("AI Study Buddy | Learn Smart, Study Better!")
