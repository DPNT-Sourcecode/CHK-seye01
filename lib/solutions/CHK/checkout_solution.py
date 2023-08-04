# noinspection PyUnusedLocal
# skus = unicode string
from typing import Dict, Tuple, Optional

A_COST = 50
B_COST = 30
C_COST = 20
D_COST = 15


# create sku class
class SKU:
    def __init__(self, sku: str, cost: int, multibuy: Optional[Tuple[int, int]]=None, multibuy2: Optional[Tuple[int, int]]=None):
        self.sku = sku
        self.cost = cost
        self.multibuy = multibuy
        self.multibuy2 = multibuy2


current_skus = {
    "A": SKU("A", 50, (5, 200)),
    "B": SKU("B", 30, (2, 45)),
    "C": SKU("C", 20, None),
    "D": SKU("D", 15, None),
    "E": SKU("E", 40, None)
}



def assert_valid_input(skus: str) -> None:
    """Assert that the input is a string of valid skus"""
    if not isinstance(skus, str):
        raise ValueError("Input must be a string")
    for sku in skus:
        if sku not in ["A", "B", "C", "D", "E"]:
            raise ValueError("Invalid sku")


def skus_to_dict(skus: str) -> Dict[str, int]:
    """
    Takes a string of skus and returns a dict of skus and their counts
    """
    sku_count = {"A": 0, "B": 0, "C": 0, "D": 0}
    for sku in skus:
        sku_count[sku] += 1
    return sku_count


def reduce_cost_with_multibuy(sku: str, count: int, multibuy_offers: Dict[str, Tuple[int, int]]) -> Tuple[int, int]:
    if sku in multibuy_offers:
        multibuy_count, multibuy_cost = multibuy_offers[sku]
        multibuy_cost = multibuy_cost * (count // multibuy_count)
        count = count % multibuy_count
        return multibuy_cost, count


def handle_multibuy(sku: str, count: int) -> Tuple[int, int]:
    """
    Handle the multi-buy offers.
    Returns a cost after multi-buy offers have been applied and the remaining count
    """
    first_multibuy_offers = {
        "A": (5, 200)
    }
    current_multibuy_offers = {
        "A": (3, 130), "B": (2, 45)
    }
     = reduce_cost_with_multibuy(sku, count, first_multibuy_offers)



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


def checkout(skus: str) -> int:
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
        return total_cost
    except ValueError as e:
        return -1



