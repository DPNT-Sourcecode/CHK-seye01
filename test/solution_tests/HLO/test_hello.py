from lib.solutions.HLO.hello_solution import hello


def test_hello() -> None:
    assert isinstance(hello("John"), str)
