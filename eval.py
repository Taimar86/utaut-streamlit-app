import streamlit as st

# Title of the Form
st.title("UTAUT Questionnaire for Context-Sensitive Spell Checking")

# Description
st.write("""
This form evaluates the acceptance and use of context-sensitive spell-checking technology based on the Unified Theory of Acceptance and Use of Technology (UTAUT). Please answer all questions.
""")

# Function to create a question with options
def create_question(question, options):
    return st.radio(question, options)

# Performance Expectancy Questions
st.header("1. Performance Expectancy")
pe1 = create_question(
    "How effective do you believe the context-sensitive spell checker is at improving the accuracy of your writing?",
    ["Very Effective", "Effective", "Somewhat Effective", "Not Effective", "Ineffective"]
)

pe2 = create_question(
    "Does the context-sensitive spell checker help you accomplish your writing tasks faster?",
    ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
)

# Effort Expectancy Questions
st.header("2. Effort Expectancy")
ee1 = create_question(
    "How easy is it to understand and use the context-sensitive spell-checking tool?",
    ["Very Easy", "Easy", "Moderate", "Difficult", "Very Difficult"]
)

ee2 = create_question(
    "Do you find the interface of the spell checker intuitive and straightforward to use?",
    ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
)

# Social Influence Questions
st.header("3. Social Influence")
si1 = create_question(
    "Do your colleagues or peers influence your decision to use the context-sensitive spell checker?",
    ["Strongly Influence", "Somewhat Influence", "No Influence", "Somewhat Discourage", "Strongly Discourage"]
)

si2 = create_question(
    "How important is it to you that people in your workplace or community support the use of this spell checker?",
    ["Very Important", "Important", "Neutral", "Unimportant", "Very Unimportant"]
)

# Facilitating Conditions Questions
st.header("4. Facilitating Conditions")
fc1 = create_question(
    "Do you have the necessary resources (e.g., computer, software) to use the context-sensitive spell-checking tool?",
    ["Always Available", "Mostly Available", "Sometimes Available", "Rarely Available", "Never Available"]
)

fc2 = create_question(
    "Do you feel confident that you have the knowledge to effectively use the context-sensitive spell checker?",
    ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
)

# Behavioral Intention to Use Questions
st.header("5. Behavioral Intention to Use")
bi1 = create_question(
    "How likely are you to continue using the context-sensitive spell checker in the future?",
    ["Very Likely", "Likely", "Neutral", "Unlikely", "Very Unlikely"]
)

bi2 = create_question(
    "Do you intend to use the context-sensitive spell checker regularly for your writing tasks?",
    ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]
)

# Actual Use Behavior Questions
st.header("6. Actual Use Behavior")
aub1 = create_question(
    "How frequently do you use the context-sensitive spell checker in your writing tasks?",
    ["Always", "Often", "Sometimes", "Rarely", "Never"]
)

aub2 = create_question(
    "How integrated is the context-sensitive spell checker into your regular writing routine?",
    ["Fully Integrated", "Mostly Integrated", "Partially Integrated", "Minimally Integrated", "Not Integrated at All"]
)

# Submit button
if st.button("Submit"):
    st.sidebar.write("### Your Responses")
    st.sidebar.write(f"Performance Expectancy 1: {pe1}")
    st.sidebar.write(f"Performance Expectancy 2: {pe2}")
    st.sidebar.write(f"Effort Expectancy 1: {ee1}")
    st.sidebar.write(f"Effort Expectancy 2: {ee2}")
    st.sidebar.write(f"Social Influence 1: {si1}")
    st.sidebar.write(f"Social Influence 2: {si2}")
    st.sidebar.write(f"Facilitating Conditions 1: {fc1}")
    st.sidebar.write(f"Facilitating Conditions 2: {fc2}")
    st.sidebar.write(f"Behavioral Intention 1: {bi1}")
    st.sidebar.write(f"Behavioral Intention 2: {bi2}")
    st.sidebar.write(f"Actual Use Behavior 1: {aub1}")
    st.sidebar.write(f"Actual Use Behavior 2: {aub2}")
