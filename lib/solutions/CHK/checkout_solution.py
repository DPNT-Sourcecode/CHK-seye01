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
            multibuy2: Optional[Tuple[int, int]] = None,
            multibuy_other: Optional[Tuple[str, int, int]] = None
    ):
        self.sku = sku
        self.cost = cost
        self.count = count
        self.total_cost = total_cost
        self.multibuy = multibuy
        self.multibuy2 = multibuy2
        self.multibuy_other = multibuy_other

    def _handle_multibuy(self, multibuy: Tuple[int, int]) -> None:
        multibuy_count, multibuy_cost = multibuy
        offer_times = self.count // multibuy_count
        self.count = self.count - (offer_times * multibuy_count)
        self.total_cost = self.total_cost + (offer_times * multibuy_cost)

    def _handle_multibuy_once(self, multibuy: Tuple[int, int]) -> None:
        multibuy_count, multibuy_cost = multibuy
        self.count = self.count - multibuy_count
        self.total_cost = self.total_cost + multibuy_cost

    def _calculate_expected_cost(self, multibuy: Tuple[int, int]) -> int:
        multibuy_count, multibuy_cost = multibuy
        offer_times = self.count // multibuy_count
        count = self.count - (offer_times * multibuy_count)
        expected_cost = (offer_times * multibuy_cost) + count * self.cost
        return expected_cost

    def calculate_cost(self) -> None:
        """
        We need to cleverly apply the best multi-buy offer to the sku.
        This means iteratively applying the best multi-buy offer each time.
        """
        if self.multibuy and self.multibuy2:
            while self.count >= self.multibuy[0] and self.count >= self.multibuy2[0]:
                if self._calculate_expected_cost(self.multibuy) > self._calculate_expected_cost(self.multibuy2):
                    self._handle_multibuy_once(self.multibuy2)
                else:
                    self._handle_multibuy_once(self.multibuy)
        if self.multibuy:
            self._handle_multibuy(self.multibuy)
        if self.multibuy2:
            self._handle_multibuy(self.multibuy2)
        self.total_cost = self.total_cost + (self.count * self.cost)


sku_manager = {}


def add_multibuy_offers():
    sku_manager["A"].multibuy = (5, 200)
    sku_manager["A"].multibuy2 = (3, 130)
    sku_manager["B"].multibuy = (2, 45)
    sku_manager["F"].multibuy = (3, 20)
    sku_manager["H"].multibuy = (10, 80)
    sku_manager["H"].multibuy2 = (5, 45)
    sku_manager["K"].multibuy = (2, 120)
    sku_manager["P"].multibuy = (5, 200)
    sku_manager["Q"].multibuy = (3, 80)
    sku_manager["U"].multibuy = (4, 120)
    sku_manager["V"].multibuy = (3, 130)
    sku_manager["V"].multibuy2 = (2, 90)


def add_multibuy_other_offers():
    sku_manager["E"].multibuy_other = ("B", 2, 1)
    sku_manager["N"].multibuy_other = ("M", 3, 1)
    sku_manager["R"].multibuy_other = ("Q", 3, 1)


def read_skus() -> None:
    """
    Helper function to generate sku_manager, again can be extended if required.
    """
    sku_file = open("/Users/kat/PycharmProjects/iwoca/accelerate_runner/lib/solutions/CHK/sku_list", "r")
    for line in sku_file.readlines():
        sku_character = line[2]
        sku_price = int(line[9:11])
        sku_manager[line[2]] = SKU(sku_character, sku_price)
    add_multibuy_offers()
    add_multibuy_other_offers()


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


def remove_free_items() -> None:
    for sku in sku_manager:
        this_sku = sku_manager[sku]
        if this_sku.multibuy_other:
            if this_sku.count >= this_sku.multibuy_other[1]:
                sku_manager[this_sku.multibuy_other[0]].count = max(
                    sku_manager[this_sku.multibuy_other[0]].count - (this_sku.count // this_sku.multibuy_other[1]),
                    0)


def get_sku_counts(skus: str) -> None:
    """
    Get the counts for each sku
    """
    initialise_sku_manager()
    for sku in skus:
        sku_manager[sku].count += 1
    remove_free_items()


def remove_group_item() -> None:
    """
    Attempt to remove the most expensive item
    """
    if sku_manager["Z"].count > 0:
        sku_manager["Z"].count -= 1
    elif sku_manager["S"].count > 0:
        sku_manager["S"].count -= 1
    elif sku_manager["T"].count > 0:
        sku_manager["T"].count -= 1
    elif sku_manager["Y"].count > 0:
        sku_manager["Y"].count -= 1
    elif sku_manager["X"].count > 0:
        sku_manager["X"].count -= 1


def apply_group_item_offer() -> int:
    """
    Apply the offer to the group items as long as possible and return the total costs, removing group items along the
    way. No offers apply to group items so no further complexity is required.
    """
    total_cost = 0
    group_item_count = (sku_manager["Z"].count +
                        sku_manager["S"].count +
                        sku_manager["T"].count +
                        sku_manager["Y"].count +
                        sku_manager["X"].count
                        )
    while group_item_count >= 3:
        total_cost += 45
        for i in range(3):
            remove_group_item()
        group_item_count -= 3
    return total_cost


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
    read_skus()
    try:
        assert_valid_input(skus)
        get_sku_counts(skus)
        group_item_cost = apply_group_item_offer()
        calculate_costs()
        individual_item_cost = 0
        for sku in sku_manager:
            individual_item_cost += sku_manager[sku].total_cost
        return individual_item_cost + group_item_cost
    except ValueError:
        return -1
