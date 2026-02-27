def parse_prompt(user_input):
    user_input = user_input.lower()

    teams = [
        "pakistan", "india", "england", "australia",
        "new zealand", "south africa", "sri lanka"
    ]

    for team in teams:
        if team in user_input:
            return team.title()

    return None
