from lib.solutions.CHK.checkout_solution import checkout


def test_checkout() -> None:
    assert checkout("") == 0
    assert checkout("A") == 50
    assert checkout("B") == 30
    assert checkout("C") == 20
    assert checkout("D") == 15
    assert checkout("AAA") == 130
    assert checkout("BB") == 45
    assert checkout("ABCD") == 115
    assert checkout("AAAAAA") == 260
    assert checkout("AAAAA") == 230
    assert checkout("ABCABA") == 195


def test_checkout_invalid() -> None:
    assert checkout("E") == -1
    assert checkout(19) == -1
    assert checkout("A19") == -1

