import pytest

from myapp.app import process_scoresheet, show_results


@pytest.fixture
def expected_results():
    return {"Lions": 5, "Tarantulas": 6, "Grouches": 0, "FC Awesome": 1, "Snakes": 1}


@pytest.fixture
def expected_text_result():
    return """1. Tarantulas, 6 pts\n2. Lions, 5 pts\n3. FC Awesome, 1 pt\n3. Snakes, 1 pt\n5. Grouches, 0 pts"""


@pytest.fixture
def expected_text_three_result():
    return """1. Tarantulas, 6 pts\n2. Lions, 5 pts\n3. Snakes, 2 pts"""


@pytest.fixture
def expected_bad_result():
    return "No valid game results found"


class TestApp:
    def test_process_scoresheet(self, expected_results):
        res = process_scoresheet(
            """Lions 3, Snakes 3
            Tarantulas 1, FC Awesome 0
            Lions 1, FC Awesome 1
            Tarantulas 3, Snakes 1
            Lions 4, Grouches 0 """
        )
        assert res["Lions"] == expected_results["Lions"]
        assert res["Tarantulas"] == expected_results["Tarantulas"]
        assert res["Grouches"] == expected_results["Grouches"]
        assert res["FC Awesome"] == expected_results["FC Awesome"]
        assert res["Snakes"] == expected_results["Snakes"]

    def test_process_show_results(self, expected_text_result):
        res = process_scoresheet(
            """Lions 3, Snakes 3
            Tarantulas 1, FC Awesome 0
            Lions 1, FC Awesome 1
            Tarantulas 3, Snakes 1
            Lions 4, Grouches 0 """
        )
        result = show_results(res)
        assert result == expected_text_result

    def test_process_three_teams_show_results(self, expected_text_three_result):
        res = process_scoresheet(
            """Lions 3, Snakes 3
            Tarantulas 1, Snakes 0
            Lions 1, Snakes 1
            Tarantulas 3, Snakes 1
            Lions 4, Tarantulas 0 """
        )
        result = show_results(res)
        assert result == expected_text_three_result

    def test_process_bad_input_show_results(self, expected_bad_result):
        res = process_scoresheet(
            """abcd, abs
            abs
            other stuffies """
        )
        result = show_results(res)
        assert result == expected_bad_result
