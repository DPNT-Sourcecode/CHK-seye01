# noinspection PyUnusedLocal
# skus = unicode string
from typing import Tuple, Optional


# create sku class
class SKU:
    def __init__(
            self,
            sku: str,
            cost: int,
            count: int = 0,
            total_cost: int = 0,
            multibuy: Optional[Tuple[int, int]] = None,
            multibuy2: Optional[Tuple[int, int]] = None
    ):
        self.sku = sku
        self.cost = cost
        self.count = count
        self.total_cost = total_cost
        self.multibuy = multibuy
        self.multibuy2 = multibuy2

    def _handle_multibuy(self, multibuy: Tuple[int, int]) -> None:
        multibuy_count, multibuy_cost = multibuy
        offer_times = self.count // multibuy_count
        self.count = self.count - (offer_times * multibuy_count)
        self.total_cost = self.total_cost + (offer_times * multibuy_cost)

    def calculate_cost(self) -> int:
        if self.multibuy:
            self._handle_multibuy(self.multibuy)
        if self.multibuy2:
            self._handle_multibuy(self.multibuy2)
        self.total_cost = self.total_cost + (self.count * self.cost)


sku_manager = {
    "A": SKU("A", 50, multibuy=(5, 200), multibuy2=(3, 130)),  # The best offer must go first... for now
    "B": SKU("B", 30, multibuy=(2, 45)),
    "C": SKU("C", 20),
    "D": SKU("D", 15),
    "E": SKU("E", 40)
}


def assert_valid_input(skus: str) -> None:
    """Assert that the input is a string of valid skus"""
    if not isinstance(skus, str):
        raise ValueError("Input must be a string")
    for sku in skus:
        if sku not in sku_manager:
            raise ValueError("Invalid sku")


def initialise_sku_manager() -> None:
    """
    Since I am using a global variable, I need to reset the values each time
    """
    for sku in sku_manager:
        sku_manager[sku].count = 0
        sku_manager[sku].total_cost = 0


def get_sku_counts(skus: str) -> None:
    """
    Get the counts for each sku
    """
    initialise_sku_manager()
    for sku in skus:
        sku_manager[sku].count += 1
    if sku_manager["E"].count >= 2:
        sku_manager["B"].count = max(sku_manager["B"].count - (sku_manager["E"].count // 2), 0)
        # Solve the special offer for E, we'll add more functionality later if required


def calculate_costs() -> None:
    """
    Calculate the total cost for each sku
    """
    for sku in sku_manager:
        sku_manager[sku].calculate_cost()


def checkout(skus: str) -> int:
    """
    The main method for the checkout process
    Must take a str of items (skus) and return an int representing the total cost
    """
    try:
        assert_valid_input(skus)
        get_sku_counts(skus)
        calculate_costs()
        total_cost = 0
        for sku in sku_manager:
            total_cost += sku_manager[sku].total_cost
        return total_cost
    except ValueError as e:
        return -1








