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


def test_new_items() -> None:
    assert checkout("F") == 10
    assert checkout("FF") == 20
    assert checkout("FFF") == 20
    assert checkout("FFFF") == 30
    assert checkout("FFFFF") == 40


def test_checkout_invalid() -> None:
    assert checkout(19) == -1
    assert checkout("A19") == -1


def test_basic_data_entry() -> None:
    """
    Test that I entered the right value for each product
    """
    assert checkout("G") == 20
    assert checkout("H") == 10
    assert checkout("I") == 35
    assert checkout("J") == 60
    assert checkout("K") == 80
    assert checkout("L") == 90
    assert checkout("M") == 15
    assert checkout("N") == 40
    assert checkout("O") == 10
    assert checkout("P") == 50
    assert checkout("Q") == 30
    assert checkout("R") == 50
    assert checkout("S") == 30
    assert checkout("T") == 20
    assert checkout("U") == 40
    assert checkout("V") == 50
    assert checkout("W") == 20
    assert checkout("X") == 90
    assert checkout("Y") == 10
    assert checkout("Z") == 50

def test_basic_offers_are_correct() -> None:
    """
    Another Data entry test, but this time for the offers
    """
    assert checkout ("HHHHH") == 45
    assert checkout ("HHHHHHHHHH") == 80
    assert




