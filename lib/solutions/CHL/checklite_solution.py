# noinspection PyUnusedLocal
# skus = unicode string
from typing import Dict, Tuple

A_COST = 50
B_COST = 30
C_COST = 20
D_COST = 15


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
        new_count = handle_multibuy(sku, count)
        return A_COST * new_count
    elif sku == "B":
        new_count = handle_multibuy(sku, count)
        return B_COST * new_count
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
    sku_dict = skus_to_dict(skus)
    raise NotImplementedError()



