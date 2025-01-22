import streamlit as st
import pandas as pd

# Define UTAUT constructs and corresponding questions
utaut_data = {
    "Performance Expectancy": [
        "I find context-sensitive spell checking improves my productivity.",
        "Using context-sensitive spell checking increases my work quality.",
        "The system enables me to accomplish tasks more quickly.",
    ],
    "Effort Expectancy": [
        "The spell-checking system is easy to use.",
        "It is easy for me to become skillful at using this system.",
        "Learning to operate the system is straightforward.",
    ],
    "Social Influence": [
        "People important to me think I should use this system.",
        "My colleagues use the system and recommend it to me.",
    ],
    "Facilitating Conditions": [
        "I have the resources necessary to use the system.",
        "I have the knowledge necessary to use the system.",
        "The system is compatible with other tools I use.",
    ],
}

# Likert scale options
likert_options = [
    "Strongly Disagree",
    "Disagree",
    "Neutral",
    "Agree",
    "Strongly Agree",
]

# Convert Likert scale to numerical values for calculations
likert_mapping = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5,
}

# Initialize a placeholder to store responses
if "all_responses" not in st.session_state:
    st.session_state["all_responses"] = []

# Streamlit app layout
st.title("UTAUT Questionnaire: Context-Sensitive Spell Checking")
st.write("Please respond to the questions below. Responses will be aggregated by construct.")

# Collect user responses
current_response = {}
for construct, questions in utaut_data.items():
    st.header(construct)
    current_response[construct] = []
    for question in questions:
        response = st.selectbox(
            question,
            options=likert_options,
            key=f"{construct}_{question}_{len(st.session_state['all_responses'])}",
        )
        current_response[construct].append(likert_mapping[response])

# Add a submit button
if st.button("Submit Response"):
    # Append the current response to the session state
    st.session_state["all_responses"].append(current_response)
    st.success("Your response has been recorded!")
    st.experimental_rerun()  # Refresh the app to clear input fields

# Check if there are any responses
if st.session_state["all_responses"]:
    # Aggregate all responses
    st.write("### Aggregated Results Across All Responses")

    # Prepare data for aggregation
    aggregated_data = {construct: [] for construct in utaut_data.keys()}
    for user_response in st.session_state["all_responses"]:
        for construct, scores in user_response.items():
            aggregated_data[construct].extend(scores)

    # Calculate aggregates
    aggregates = {
        "Construct": [],
        "Average Score (1-5)": [],
        "Percentage Agreement (>=4)": [],
    }
    for construct, scores in aggregated_data.items():
        avg_score = sum(scores) / len(scores)
        percentage_agreement = (len([s for s in scores if s >= 4]) / len(scores)) * 100

        aggregates["Construct"].append(construct)
        aggregates["Average Score (1-5)"].append(round(avg_score, 2))
        aggregates["Percentage Agreement (>=4)"].append(round(percentage_agreement, 2))

    # Display aggregated results
    aggregates_df = pd.DataFrame(aggregates)
    st.table(aggregates_df)

    # Visualize results
    st.bar_chart(aggregates_df.set_index("Construct")["Average Score (1-5)"])

    # Option to download data as CSV
    if st.button("Download Results as CSV"):
        all_responses_df = pd.DataFrame(st.session_state["all_responses"])
        all_responses_df.to_csv("utaut_responses.csv", index=False)
        st.success("Results saved as `utaut_responses.csv`")
else:
    st.write("No responses have been submitted yet.")
