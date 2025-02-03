import streamlit as st
import pandas as pd

# Set page title
st.title("UTAUT Questionnaire for Context-Sensitive Spell Checking")

# Define UTAUT constructs and their corresponding questions
questions = {
    "Performance Expectancy": "I find the context-sensitive spell checker useful in my tasks.",
    "Effort Expectancy": "The spell checker is easy to use.",
    "Social Influence": "People whose opinions I value prefer this spell checker.",
    "Facilitating Conditions": "I have the necessary resources to use this spell checker.",
    "Behavioral Intention": "I intend to use this spell checker regularly.",
    "Actual Use Behavior": "I frequently use the context-sensitive spell checker."
}

# Define Likert scale options
likert_options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

# Initialize session state to store responses
if "responses" not in st.session_state:
    st.session_state.responses = []

# Display questions with radio buttons
st.subheader("Please select your response for each statement:")
user_responses = {}

for construct, question in questions.items():
    st.write(f"**{question}**")  # Display the question
    user_responses[construct] = st.radio(
        label="",  # No label for the radio buttons
        options=likert_options,  # Only the Likert scale options
        index=None,  # No default selection
        key=construct
    )

# Submit button with validation check
if st.button("Submit Responses"):
    if None in user_responses.values():  # Ensure all questions are answered
        st.error("Please select an option for all questions before submitting.")
    else:
        st.session_state.responses.append(user_responses)
        st.success("Your responses have been recorded!")

# Display responses table and bar chart if data exists
if st.session_state.responses:
    df = pd.DataFrame(st.session_state.responses)

    # Show responses table
    st.subheader("Responses Table")
    st.table(df)

    # Convert Likert responses to numerical values for visualization
    likert_mapping = {
        "Strongly Disagree": 1,
        "Disagree": 2,
        "Neutral": 3,
        "Agree": 4,
        "Strongly Agree": 5
    }
    df_numeric = df.replace(likert_mapping)

    # Show bar chart
    st.subheader("Survey Results (Bar Chart)")
    st.bar_chart(df_numeric.mean())
