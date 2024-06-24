from dataclasses import dataclass


# It is handy to use `dataclass` to avoid boilerplate code for `__init__`
@dataclass
class InventoryItem:
    """Entity to observe and manage player's inventory entries."""
    name: str
    unit_price: float
    quantity: int = 0

    def get_total_cost(self) -> float:
        return self.quantity * self.unit_price


if __name__ == '__main__':
    apples = InventoryItem('Apple', 0.45, 4)
    healing_potion = InventoryItem('Healing Potion', 15.75, 2)
    broadsword = InventoryItem('Broadsword', 1_350.00, 1)
    necronomicon = InventoryItem('Necronomicon', 999_999)
