class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        name_type = f"Ресторан:{self.restaurant_name}, Кухня:{self.cuisine_type}"
        return name_type.title()

    def open_restaurant(self):
        '''' метод выводит  информацию, что ресторан открыт'''
        return "Ресторан открыт"

restaurant = Restaurant('Уральские пельмени', 'пельмени и варенники' )

print(restaurant.describe_restaurant_name()) # печатаю название ресторана
print(restaurant.describe_restaurant_cuisine()) # печатаю тип кухни в ресторане
print('Название ресторана и кухня: ',restaurant.describe_restaurant()) # # печатаю название и тип кухни в ресторане
print(restaurant.open_restaurant()) # сообщение, что ресторан открыт

print(restaurant.describe_restaurant(), restaurant.open_restaurant()) # Имя и кухня ресторана + сообщение, что ресторан открыт