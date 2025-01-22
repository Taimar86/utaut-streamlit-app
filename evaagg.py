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

# Streamlit app layout
st.title("UTAUT Questionnaire: Context-Sensitive Spell Checking")
st.write("Please respond to the questions below. Responses will be aggregated by construct.")

# Collect responses
responses = {}
for construct, questions in utaut_data.items():
    st.header(construct)
    responses[construct] = []
    for question in questions:
        response = st.selectbox(
            question,
            options=likert_options,
            key=f"{construct}_{question}",
        )
        responses[construct].append(likert_mapping[response])

# Calculate aggregates
aggregates = {
    "Construct": [],
    "Average Score (1-5)": [],
    "Percentage Agreement (>=4)": [],
}

for construct, scores in responses.items():
    avg_score = sum(scores) / len(scores)
    percentage_agreement = (len([s for s in scores if s >= 4]) / len(scores)) * 100

    aggregates["Construct"].append(construct)
    aggregates["Average Score (1-5)"].append(round(avg_score, 2))
    aggregates["Percentage Agreement (>=4)"].append(round(percentage_agreement, 2))

# Display results
st.write("### Aggregated Results")
aggregates_df = pd.DataFrame(aggregates)
st.table(aggregates_df)

# Visualize results
st.bar_chart(aggregates_df.set_index("Construct")["Average Score (1-5)"])