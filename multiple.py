
import streamlit as st
import pandas as pd
import os
import json
from collections import Counter

# Set page title
st.title("UTAUT Questionnaire for Context-Sensitive Spell Checking")

# Define UTAUT constructs and questions
questions = {
    "Performance Expectancy": "I find the context-sensitive spell checker useful in my tasks.",
    "Effort Expectancy": "The spell checker is easy to use.",
    "Social Influence": "People whose opinions I value prefer this spell checker.",
    "Facilitating Conditions": "I have the necessary resources to use this spell checker.",
    "Behavioral Intention": "I intend to use this spell checker regularly.",
    "Actual Use Behavior": "I frequently use the context-sensitive spell checker."
}

likert_options = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
response_file = "survey_responses.json"

# Load previous responses
if os.path.exists(response_file):
    with open(response_file, "r", encoding="utf-8") as f:
        all_responses = json.load(f)
else:
    all_responses = []

# Display form
st.subheader("Please select your response for each statement:")
user_responses = {}

for construct, question in questions.items():
    st.write(f"**{question}**")
    user_responses[construct] = st.radio(
        label="", options=likert_options, index=None, key=construct
    )

# Submit button
if st.button("Submit Responses"):
    if None in user_responses.values():
        st.error("Please select an option for all questions before submitting.")
    else:
        all_responses.append(user_responses)
        with open(response_file, "w", encoding="utf-8") as f:
            json.dump(all_responses, f, indent=4, ensure_ascii=False)
        st.success("Your responses have been recorded!")

# Display summary if there are any responses
if all_responses:
    df = pd.DataFrame(all_responses)

    st.subheader("Percentage Breakdown of Responses")

    # Compute percentage breakdown
    percentages = {}
    for column in df.columns:
        counts = df[column].value_counts(normalize=True) * 100
        counts = counts.reindex(likert_options, fill_value=0)
        percentages[column] = counts

    percent_df = pd.DataFrame(percentages).T.round(2)
    st.table(percent_df)

    # Optional: Show bar chart for average numeric scores
    likert_mapping = {
        "Strongly Disagree": 1,
        "Disagree": 2,
        "Neutral": 3,
        "Agree": 4,
        "Strongly Agree": 5
    }
    df_numeric = df.replace(likert_mapping)
    st.subheader("Average Score per Question")
    st.bar_chart(df_numeric.mean())
