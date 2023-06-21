class Coffee:
    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def recipe(self):
        if self.ingredient:
            print(f'Кофе и {self.ingredient}')
        else:
            print('Обычный растворимый кофе')
