from lib.solutions.CHK.checkout_solution import checkout


def test_checkout() -> None:
    assert checkout("") == 0
    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("C") == 20
    assert checkout("D") == 15
    assert checkout("E") == 40
    assert checkout("AAA") == 130
    assert checkout("BB") == 45
    assert checkout("ABCD") == 115
    assert checkout("AAAAAA") == 250
    assert checkout("AAAAA") == 200
    assert checkout("ABCABA") == 195
    assert checkout("EEB") == 80
    assert checkout("EEEEEE") == 240
    assert checkout("EEEBEEEB") == 240


def test_checkout_invalid() -> None:
    assert checkout("Z") == -1
    assert checkout(19) == -1
    assert checkout("A19") == -1
