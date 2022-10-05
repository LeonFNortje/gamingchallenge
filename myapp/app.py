import collections

from myapp.mymodule.funcs import rules, get_gameline, get_team


def process_scoresheet(scoresheet):
    team_list = []
    team_points = {}

    for scoreline in [score for score in scoresheet.split("\n") if score]:
        teams = get_gameline(scoreline)
        if teams[0]:
            team_list.extend(rules(teams[0], teams[1]))

    for team in team_list:
        if team_points.get(team["team_name"]):
            team["points"] += team_points[team["team_name"]]
        team_points[team["team_name"]] = team["points"]
    return team_points


def show_results(res):
    result = []
    prev_score = -1
    rank = 0
    ind = 0
    odered_items = collections.OrderedDict(sorted(res.items()))
    for w in sorted(odered_items, key=odered_items.get, reverse=True):
        ind += 1
        if res[w] != prev_score:
            prev_score = res[w]
            rank = ind
        result.append(f"{rank}. {w}, {res[w]} {'pt' if res[w]==1 else 'pts'}")
    if len(result) == 0:
        return "No valid game results found"
    return "\n".join(result)
