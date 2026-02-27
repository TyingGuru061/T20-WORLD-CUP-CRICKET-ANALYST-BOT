import streamlit as st
from data_fetcher import fetch_points_table
from qualification_engine import analyze_qualification
from prompt_engine import parse_prompt

st.set_page_config(
    page_title="ICC T20 Qualification Analyst",
    page_icon="🏏",
    layout="centered"
)

st.title("🏏 ICC T20 World Cup Qualification Analyst")

st.markdown("Ask questions like:")
st.markdown("- Can Pakistan qualify?")
st.markdown("- Is India safe?")
st.markdown("- Who is top 4?")

user_input = st.text_input("Enter your question:")

if st.button("Analyze"):

    team = parse_prompt(user_input)

    if not team:
        st.error("Please mention a valid team name.")
    else:
        df = fetch_points_table()
        result = analyze_qualification(df, team)
        st.success(result)
