# Req 3
import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set()
        self.load_menu_data()

    def load_menu_data(self) -> None:
        with open(self.source_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                dish_name = row[0]
                price = float(row[1])
                ingredient_str = row[2]
                amount = int(row[3])
                ingredient = Ingredient(ingredient_str)
                dish = self._get_or_create_dish(dish_name, price)
                dish.add_ingredient_dependency(ingredient, amount)

    def _get_or_create_dish(self, name: str, price: float) -> Dish:
        for existing_dish in self.dishes:
            if existing_dish.name == name and existing_dish.price == price:
                return existing_dish
        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish
