import sqlite3
import random
import pandas as pd

conn = sqlite3.connect("food.db")
cursor = conn.cursor()

cities = [
    "Mumbai",
    "Pune",
    "Nagpur",
    "Nashik",
    "Thane",
    "Aurangabad"
]

providers = [
    "Restaurant",
    "Supermarket",
    "Catering Service",
    "Grocery Store"
]

meals = [
    "Breakfast",
    "Lunch",
    "Dinner",
    "Snacks"
]

diets = [
    "Vegetarian",
    "Non-Vegetarian",
    "Vegan"
]

rows = []

for i in range(300):

    rows.append([
        random.choice(cities),
        random.choice(providers),
        random.choice(meals),
        random.choice(diets),
        random.randint(10,150)
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "city",
        "provider_type",
        "meal_type",
        "diet_type",
        "quantity"
    ]
)

df.to_sql(
    "food",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Sample Data Generated")