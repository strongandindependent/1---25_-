
# Добавление атрибута рейтинга и метода для его обновления
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type, "кухня")
        print(self.rating, "звезд")

    def open_restaurant(self):
        print("Ресторан открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating

newRestaurant = Restaurant("Скуратов", "Кофе")

newRestaurant.update_rating(5)

newRestaurant.describe_restaurant()