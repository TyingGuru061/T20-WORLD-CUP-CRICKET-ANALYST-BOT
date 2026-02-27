from qualification_engine import required_run_margin, required_chase_overs

def generate_analysis(team, team_stats, opponent_nrr):

    run_margin = required_run_margin(team_stats, opponent_nrr)
    chase_overs = required_chase_overs(team_stats, opponent_nrr)

    analysis = f"""
🏏 **ICC T20 WORLD CUP QUALIFICATION ANALYSIS**

🔹 Team: {team}
🔹 Current NRR: {team_stats['nrr']}
🔹 NRR to Beat: {opponent_nrr}

📌 **If Batting First**
➡ Team must win by **{run_margin} runs** to cross qualification NRR.

📌 **If Chasing**
➡ Team must chase target of 170 within **{chase_overs} overs**.

🧠 **Expert Analyst View**
This is a high-pressure NRR scenario. The team must attack in the powerplay,
keep run rate above 9 RPO, and restrict opposition early. Defensive cricket
will NOT be enough.

📊 Qualification will likely go down to net run rate.
"""

    return analysis
