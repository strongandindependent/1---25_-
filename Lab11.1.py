class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Ресторан " + self.name.title() + " предложит вам " + self.cuisine_type + " кухню!")

    def open_restaurant(self):
        print("Ресторан " + self.name.title() + " открыт сейчас!")



kebab_resto = Restaurant('Skuratov', 'европейская')
tokyo_resto = Restaurant('Tokio', 'japan')
tokyo_resto = Restaurant('Tokio', 'japan')


print(kebab_resto.describe_restaurant())
print(kebab_resto.open_restaurant())