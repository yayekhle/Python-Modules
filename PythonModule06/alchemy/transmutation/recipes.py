from alchemy.elements import create_air
from alchemy.potions import strength_potion
import elements as _root_elements


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}'"
        f" mixed with '{_root_elements.create_fire()}'"
    )
