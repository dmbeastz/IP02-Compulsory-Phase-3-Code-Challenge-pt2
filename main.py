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
        return [cls(*row[1:]) for row in cursor.fetchall()]

class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.id = None  

    def save(self):
        if not self.customer.id:
            self.customer.save()
        if not self.restaurant.id:
            self.restaurant.save()

        cursor.execute('''
            INSERT INTO reviews (customer_id, restaurant_id, rating)
            VALUES (?, ?, ?)
        ''', (self.customer.id, self.restaurant.id, self.rating))
        conn.commit()
        self.id = cursor.lastrowid 

    @classmethod
    def all(cls):
        cursor.execute('SELECT * FROM reviews')
        return [cls(*row[1:]) for row in cursor.fetchall()]

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
restaurant1 = Restaurant("Pizza Palace")
restaurant2 = Restaurant("Burger Kingdom")

review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer1, restaurant2, 3)

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
    print(f"ID: {review.id}, Customer ID: {review.customer.id}, Restaurant ID: {review.restaurant.id}, Rating: {review.rating}")

# Close the connection
conn.close()
