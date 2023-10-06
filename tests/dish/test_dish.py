import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish1 = Dish('Coxinha', 2.99)
    dish2 = Dish('Coxinha', 2.99)
    dish3 = Dish('Buxada', 15.99)
    ingredient1 = Ingredient('frango')
    dish1.add_ingredient_dependency(ingredient1, 2)
    expected_restrictions = {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT
    }

    assert dish1.name == 'Coxinha'

    assert dish1.__hash__() == dish2.__hash__()
    assert dish1.__hash__() != dish3.__hash__()

    assert dish1.__eq__(dish2) is True
    assert dish1.__eq__(dish1) is True
    assert dish1.__eq__(dish3) is False

    assert dish1.__repr__() == "Dish('Coxinha', R$2.99)"

    with pytest.raises(TypeError):
        Dish("Coxinha", "abc")

    with pytest.raises(ValueError):
        Dish("Coxinha", -2.99)

    assert dish1.recipe.get(ingredient1) == 2

    assert dish1.get_restrictions() == expected_restrictions
    assert dish1.get_ingredients() == {ingredient1}
