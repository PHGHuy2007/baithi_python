import pandas as pd
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Pen", "Book", "Mouse", "Keyboard", "Monitor"],
    "price": [20, 50, 150, 200, 500],
    "quantity": [10, 5, 10, 5, 2]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
df = pd.read_csv("students.csv")
print("ALL products:")
print(df)
print("Products with price > 100:")
print(df[df["price"] > 100])