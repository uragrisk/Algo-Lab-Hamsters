class Hamster:
    def __init__(self, daily_food, greed_food):
        self.daily_food = daily_food
        self.greed_food = greed_food

    def get_hamster_total_consumption(self, number_of_hamsters):
        return self.daily_food + self.greed_food * (number_of_hamsters - 1)
