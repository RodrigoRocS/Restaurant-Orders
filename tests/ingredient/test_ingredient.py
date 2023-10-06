from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")
    assert ingredient1.__hash__() == ingredient2.__hash__()
    assert ingredient1.__hash__() != ingredient3.__hash__()

    assert ingredient1.__eq__(ingredient2) is True
    assert ingredient1.__eq__(ingredient1) is True
    assert ingredient1.__eq__(ingredient3) is False

    assert ingredient1.__repr__() == "Ingredient('queijo mussarela')"

    assert ingredient1.name == "queijo mussarela"

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient1.restrictions == expected_restrictions
