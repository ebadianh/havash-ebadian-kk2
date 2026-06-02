from app.data_manager import (
    get_team_with_most_wins,
    get_team_with_most_goals,
    get_team_with_most_draws,
)

def handle_question(question):

    if "vinster" in question.lower():
        return get_team_with_most_wins()

    if question == "Vilket lag har gjort flest mål?":
        return get_team_with_most_goals()

    if question == "Vilket lag har flest oavgjorda matcher?":
        return get_team_with_most_draws()

    return {
        "message": "Frågan känns inte igen"
    }