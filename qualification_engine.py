def analyze_qualification(df, team_name):

    df = df.sort_values(by=["points", "nrr"], ascending=False)
    top4 = df.head(4)

    if team_name not in df["team"].values:
        return "Team not found in tournament table."

    team_row = df[df["team"] == team_name].iloc[0]

    position = df.index[df["team"] == team_name][0] + 1

    analysis = f"""
📊 Qualification Analysis for {team_name}

Current Position: {position}
Points: {team_row['points']}
NRR: {team_row['nrr']}

Top 4 Teams Currently:
"""

    for _, row in top4.iterrows():
        analysis += f"\n- {row['team']} ({row['points']} pts, NRR {row['nrr']})"

    if position <= 4:
        analysis += "\n\nStatus: Currently in qualification zone."
    else:
        analysis += "\n\nStatus: Outside top 4. Must win remaining matches."

    return analysis
