
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="AI Interview Preparation Assistant",
    page_icon="🎯",
    layout="centered"
)

# Store questions and answers across app reruns
if "questions" not in st.session_state:
    st.session_state.questions = []

if "role" not in st.session_state:
    st.session_state.role = ""

if "answers" not in st.session_state:
    st.session_state.answers = {}

# Application title
st.title("🎯 AI Interview Preparation Assistant")

st.write(
    "Prepare for your interviews with AI-generated "
    "questions and sample answers."
)

st.divider()

# Job role input
role = st.text_input("Enter your job role")

# Generate questions button
if st.button("Generate Interview Questions"):

    if role.strip():

        try:
            with st.spinner("Generating questions..."):

                response = requests.get(
                    "http://127.0.0.1:8000/generate-questions",
                    params={"role": role},
                    timeout=60
                )

            if response.status_code == 200:

                data = response.json()

                st.session_state.questions = data["questions"]
                st.session_state.role = role
                st.session_state.answers = {}

                st.success("Interview questions generated successfully!")

            else:
                st.error("Unable to generate questions.")

        except requests.exceptions.RequestException:
            st.error("Unable to connect to the backend.")

    else:
        st.warning("Please enter a job role.")

# Display generated questions
if st.session_state.questions:

    st.divider()

    st.subheader("📝 Interview Questions")

    for i, question in enumerate(st.session_state.questions, start=1):

        with st.expander(f"Question {i}: {question}"):

            if st.button("Generate Sample Answer", key=f"answer_{i}"):

                try:
                    with st.spinner("Generating sample answer..."):

                        response = requests.get(
                            "http://127.0.0.1:8000/generate-answer",
                            params={
                                "role": st.session_state.role,
                                "question": question
                            },
                            timeout=60
                        )

                    if response.status_code == 200:

                        data = response.json()

                        st.session_state.answers[i] = data["sample_answer"]

                    else:
                        st.error("Unable to generate sample answer.")

                except requests.exceptions.RequestException:
                    st.error("Unable to connect to the backend.")

            if i in st.session_state.answers:

                st.markdown("**💡 Sample Answer:**")

                st.write(st.session_state.answers[i])

    # Prepare downloadable content
    download_content = f"AI Interview Preparation Assistant\n"
    download_content += f"Job Role: {st.session_state.role}\n\n"

    for i, question in enumerate(st.session_state.questions, start=1):

        download_content += f"Question {i}: {question}\n\n"

        if i in st.session_state.answers:

            download_content += "Sample Answer:\n"
            download_content += st.session_state.answers[i] + "\n\n"

        else:

            download_content += "Sample Answer: Not generated yet.\n\n"

        download_content += "-" * 60 + "\n\n"

    # Download button
    st.divider()

    st.download_button(
        label="📥 Download Questions and Answers",
        data=download_content,
        file_name="interview_preparation.txt",
        mime="text/plain"
    )
