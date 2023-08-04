# noinspection PyUnusedLocal
# skus = unicode string
from typing import Dict, Tuple

A_COST = 50
B_COST = 30
C_COST = 20
D_COST = 15


def assert_valid_input(skus: str) -> None:
    """Assert that the input is a string of valid skus"""
    if not isinstance(skus, str):
        raise ValueError("Input must be a string")
    for sku in skus:
        if sku not in ["A", "B", "C", "D"]:
            raise ValueError("Invalid sku")


def skus_to_dict(skus: str) -> Dict[str, int]:
    """
    Takes a string of skus and returns a dict of skus and their counts
    """
    sku_count = {"A": 0, "B": 0, "C": 0, "D": 0}
    for sku in skus:
        sku_count[sku] += 1
    return sku_count


def handle_multibuy(sku: str, count: int) -> Tuple[int, int]:
    """
    Handle the multi-buy offers.
    Returns a cost after multi-buy offers have been applied and the remaining count
    """
    current_multiby_offers = {
        "A": (3, 130), "B": (2, 45)
    }
    if sku in current_multiby_offers:
        multibuy_count, multibuy_cost = current_multiby_offers[sku]
        multibuy_cost = multibuy_cost * (count // multibuy_count)
        count = count % multibuy_count
        return multibuy_cost, count


def calculate_cost(sku: str, count: int) -> int:
    """Calculate the cost of a sku based on the count"""
    if sku == "A":
        multibuy_cost, new_count = handle_multibuy(sku, count)
        return A_COST * new_count + multibuy_cost
    elif sku == "B":
        multibuy_cost, new_count = handle_multibuy(sku, count)
        return B_COST * new_count + multibuy_cost
    elif sku == "C":
        return C_COST * count
    elif sku == "D":
        return D_COST * count
    else:
        raise ValueError("Invalid sku")


def checklite(skus):
    """
    The main method for the checkout process
    Must take a str of items (skus) and return an int representing the total cost
    """
    try:
        assert_valid_input(skus)
        sku_dict = skus_to_dict(skus)
        total_cost = 0
        for sku in sku_dict:
            total_cost += calculate_cost(sku, sku_dict[sku])
    except ValueError as e:
        print(e)
        return -1
