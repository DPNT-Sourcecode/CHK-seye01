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
    assert checkout("K") == 70
    assert checkout("L") == 90
    assert checkout("M") == 15
    assert checkout("N") == 40
    assert checkout("O") == 10
    assert checkout("P") == 50
    assert checkout("Q") == 30
    assert checkout("R") == 50
    assert checkout("S") == 20
    assert checkout("T") == 20
    assert checkout("U") == 40
    assert checkout("V") == 50
    assert checkout("W") == 20
    assert checkout("X") == 17
    assert checkout("Y") == 20
    assert checkout("Z") == 21


def test_basic_offers_are_correct() -> None:
    """
    Another Data entry test, but this time for the offers
    """
    assert checkout("HHHHH") == 45
    assert checkout("HHHHHHHHHH") == 80
    assert checkout("KK") == 120
    assert checkout("NNNM") == 120
    assert checkout("PPPPP") == 200
    assert checkout("QQQ") == 80
    assert checkout("RRRQ") == 150
    assert checkout("UUUU") == 120
    assert checkout("VV") == 90
    assert checkout("VVV") == 130
    assert checkout("VVVVV") == 220
    assert checkout("VVVVVV") == 260
    assert checkout("AAAAAAAAA") == 380


def test_new_special_offers_are_correct() -> None:
    assert checkout("STX") == 45
    assert checkout("STXSTXXYZ") == 135
    assert checkout("ZZZX") == 62
