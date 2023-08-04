# noinspection PyUnusedLocal
# skus = unicode string


def skus_to_dict(skus):
    """
    Takes a string of skus and returns a dict of skus and their counts
    """
    sku_count = {"A": 0, "B": 0, "C": 0, "D": 0}
    for sku in skus:
        sku_count[sku] += 1
    return sku_count


def checklite(skus):
    """
    The main method for the checkout process
    Must take a str of items (skus) and return an int representing the total cost
    """
    raise NotImplementedError()


