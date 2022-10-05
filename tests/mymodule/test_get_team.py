import pytest

from myapp.mymodule.funcs import get_team


@pytest.mark.parametrize(
    "a, b, c",
    [
        ("Lions 3", "Lions", 3),
        ("Tarantulas 1", "Tarantulas", 1),
        ("Awesome Four Beasts 5", "Awesome Four Beasts", 5),
        ("Awesome 123 Beasts 10", "Awesome 123 Beasts", 10),
    ],
)
def test_get_teams(a, b, c):
    res = get_team(a)

    assert res["team_name"] == b
    assert res["score"] == c
