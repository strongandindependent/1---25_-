import json

def display_products(products):
  for product in products:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
      print("В наличии")
    else:
      print("Нет в наличии!")
    print()

def add_product(products):
  name = input("Введите название продукта: ")
  price = int(input("Введите цену продукта: "))
  weight = int(input("Введите вес продукта: "))
  available = input("В наличии (да/нет)? ")
  available = available.lower() == 'да'
  products.append({
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
  })

with open("products.json", "r") as f:
  data = json.load(f)
  products = data["products"]
  display_products(products)

add_product(products)

with open("products.json", "w") as f:
  json.dump({"products": products}, f)

print("Обновленный список продуктов:")
display_products(products)