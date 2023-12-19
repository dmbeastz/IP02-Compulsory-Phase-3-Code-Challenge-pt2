import sqlite3

conn = sqlite3.connect('restaurant_reviews.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        given_name TEXT,
        family_name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        restaurant_id INTEGER,
        rating INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers (id),
        FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
    )
''')

conn.commit()


class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.id = None

    def save(self):
        cursor.execute('''
            INSERT INTO customers (given_name, family_name)
            VALUES (?, ?)
        ''', (self.given_name, self.family_name))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def all(cls):
        cursor.execute('SELECT * FROM customers')
        return [cls(*row[1:]) for row in cursor.fetchall()]  


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.id = None

    def save(self):
        cursor.execute('''
            INSERT INTO restaurants (name)
            VALUES (?)
        ''', (self.name,))
        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def all(cls):
        cursor.execute('SELECT * FROM restaurants')
        return [cls(*row[1:]) for row in cursor.fetchall()]  # Extract name


class Review:
    def __init__(self, customer_id, restaurant_id, rating):
        self.rating = rating
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.id = None

    def save(self):
        cursor.execute('''
            INSERT INTO reviews (customer_id, restaurant_id, rating)
            VALUES (?, ?, ?)
        ''', (self.customer_id, self.restaurant_id, self.rating))

        conn.commit()
        self.id = cursor.lastrowid

    @classmethod
    def all(cls):
        cursor.execute('SELECT * FROM reviews')
        return [cls(row[1], row[2], row[3]) for row in cursor.fetchall()]


customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
restaurant1 = Restaurant("Pizza Palace")
restaurant2 = Restaurant("Burger Kingdom")

customer1.save()
customer2.save()
restaurant1.save()
restaurant2.save()

review1 = Review(customer1.id, restaurant1.id, 4)
review2 = Review(customer2.id, restaurant1.id, 5)
review3 = Review(customer1.id, restaurant2.id, 3)

# Save reviews to the database
review1.save()
review2.save()
review3.save()

# Print some information for verification
print("Reviews added to the database.")

# Retrieving data
all_customers = Customer.all()
all_restaurants = Restaurant.all()
all_reviews = Review.all()

# Print the retrieved data
print("\nAll Customers:")
for customer in all_customers:
    print(f"ID: {customer.id}, Given Name: {customer.given_name}, Family Name: {customer.family_name}")

print("\nAll Restaurants:")
for restaurant in all_restaurants:
    print(f"ID: {restaurant.id}, Name: {restaurant.name}")

print("\nAll Reviews:")
for review in all_reviews:
    print(f"ID: {review.id}, Customer ID: {review.customer_id}, Restaurant ID: {review.restaurant_id}, Rating: {review.rating}")

# Close the connection
conn.close()
