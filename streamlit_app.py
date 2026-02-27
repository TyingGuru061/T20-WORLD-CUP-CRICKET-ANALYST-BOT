import streamlit as st
from analyst_engine import generate_analysis

st.set_page_config(
    page_title="ICC T20 World Cup Analyst",
    page_icon="🏏",
    layout="centered"
)

st.title("🏏 ICC T20 World Cup – Qualification Analyst Bot")
st.write("Advanced NRR-based qualification and margin predictor")

st.markdown("---")

team = st.text_input("Team Name", placeholder="e.g. Pakistan")

st.subheader("📊 Current Tournament Stats")

runs_scored = st.number_input("Total Runs Scored", min_value=1, value=600)
overs_faced = st.number_input("Total Overs Faced", min_value=1.0, value=80.0)

runs_conceded = st.number_input("Total Runs Conceded", min_value=1, value=580)
overs_bowled = st.number_input("Total Overs Bowled", min_value=1.0, value=80.0)

current_nrr = st.number_input("Current Team NRR", value=0.25)
opponent_nrr = st.number_input("NRR to Beat (Opponent)", value=0.50)

if st.button("🔍 Analyze Qualification Scenario"):
    team_stats = {
        "runs_scored": runs_scored,
        "overs_faced": overs_faced,
        "runs_conceded": runs_conceded,
        "overs_bowled": overs_bowled,
        "nrr": current_nrr
    }

    result = generate_analysis(team, team_stats, opponent_nrr)
    st.success(result)

st.markdown("---")
st.caption("⚠️ Manual simulation – based on ICC T20 NRR rules")
