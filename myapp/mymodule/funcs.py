import re

"""
funcs.py contains rules and some math functions.
"""

TIE_SCORE = 1
WIN_SCORE = 3
PNTS = "points"

"""
    In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points.
"""


def rules(team_a, team_b):
    if team_a["score"] == team_b["score"]:
        team_a[PNTS] += TIE_SCORE
        team_b[PNTS] += TIE_SCORE
    elif team_a["score"] > team_b["score"]:
        team_a[PNTS] += WIN_SCORE
    else:
        team_b[PNTS] += WIN_SCORE
    return [team_a, team_b]


def get_team(team_str):
    scores = re.findall(r" \d+$", team_str.strip())
    if not scores:
        return None
    team_name = team_str.replace(scores[0], "").strip()
    return {"score": int(scores[0]), "team_name": team_name, PNTS: 0}


def get_gameline(game_str):
    return [get_team(player.strip()) for player in game_str.split(",") if player]
