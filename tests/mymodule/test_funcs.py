import pytest

from myapp.mymodule.funcs import *


def test_get_team_lions():
    result = get_team("Lions 3")
    assert result["points"] == 0
    assert result["team_name"] == "Lions"
    assert result["score"] == 3


def test_get_team_snakes():
    result = get_team("Snakes 5")
    assert result["points"] == 0
    assert result["team_name"] == "Snakes"
    assert result["score"] == 5


def test_get_team_spaced():
    result = get_team("L i o n s 3999")
    assert result["points"] == 0
    assert result["team_name"] == "L i o n s"
    assert result["score"] == 3999


def test_get_team_number_wrong_place():
    result = get_team("3999 Lions")
    assert not result


def test_get_team_name_weird():
    result = get_team("Club 69 pandas 99")
    assert result["points"] == 0
    assert result["team_name"] == "Club 69 pandas"
    assert result["score"] == 99


def test_get_team_name_weird_extra_space():
    result = get_team("Club 69 pandas 99   ")
    assert result["points"] == 0
    assert result["team_name"] == "Club 69 pandas"
    assert result["score"] == 99


def test_get_get_gameline():
    (team_a, team_b) = get_gameline("Lions 3, Snakes 5")
    assert team_a["points"] == 0
    assert team_a["team_name"] == "Lions"
    assert team_a["score"] == 3
    assert team_b["points"] == 0
    assert team_b["team_name"] == "Snakes"
    assert team_b["score"] == 5


def test_get_gameline_check_rules():
    (team_a, team_b) = get_gameline("Lions   3,  Snakes   5")
    res = rules(team_a, team_b)
    assert res[0]["points"] == 0
    assert res[0]["team_name"] == "Lions"
    assert res[0]["score"] == 3
    assert res[1]["points"] == 3
    assert res[1]["team_name"] == "Snakes"
    assert res[1]["score"] == 5


def test_get_gameline_check_rules_tie():
    (team_a, team_b) = get_gameline("Bandits 1, Cobras 1")
    res = rules(team_a, team_b)
    assert res[0]["points"] == 1
    assert res[1]["points"] == 1


def test_get_gameline_check_rules_cobras_win():
    (team_a, team_b) = get_gameline("Bandits 1, Cobras 2")
    res = rules(team_a, team_b)
    assert res[0]["points"] == 0
    assert res[1]["points"] == 3
