def calculate_nrr(runs_scored, overs_faced, runs_conceded, overs_bowled):
    return (runs_scored / overs_faced) - (runs_conceded / overs_bowled)


def updated_nrr(stats, add_runs_scored, add_overs_faced,
                add_runs_conceded, add_overs_bowled):

    rs = stats["runs_scored"] + add_runs_scored
    of = stats["overs_faced"] + add_overs_faced
    rc = stats["runs_conceded"] + add_runs_conceded
    ob = stats["overs_bowled"] + add_overs_bowled

    return calculate_nrr(rs, of, rc, ob)


def required_run_margin(team_stats, target_nrr, assumed_score=170, overs=20):
    for margin in range(1, 201):
        new_nrr = updated_nrr(
            team_stats,
            assumed_score,
            overs,
            assumed_score - margin,
            overs
        )
        if new_nrr > target_nrr:
            return margin
    return "Extremely difficult"


def required_chase_overs(team_stats, target_nrr, opponent_score=170, overs=20):
    o = 1.0
    while o <= overs:
        new_nrr = updated_nrr(
            team_stats,
            opponent_score,
            o,
            opponent_score,
            overs
        )
        if new_nrr > target_nrr:
            return round(o, 1)
        o += 0.5
    return "Must win very early"
