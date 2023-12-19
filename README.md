# IP02-Compulsory-Phase-3-Code-Challenge-pt2
# Restaurant Reviews Database
This Python script sets up a simple SQLite database for storing restaurant reviews. It defines three tables: customers, restaurants, and reviews. The Customer, Restaurant, and Review classes allow users to interact with the database by adding customers, restaurants, and reviews.

## Instructions
1. Git Clone git@github.com:dmbeastz/IP02-Compulsory-Phase-3-Code-Challenge-pt2.git

2. cd IP02-Compulsory-Phase-3-Code-Challenge-pt2

3. Run the main.py 

## Purpose
The purpose of this code is to provide a basic framework for managing restaurant reviews. It creates a SQLite database with three tables to store information about customers, restaurants, and reviews. Users can add new entries and retrieve information about existing customers, restaurants, and reviews.

## Usage
Database Initialization: The script automatically creates the necessary tables (customers, restaurants, and reviews) if they do not already exist.

Adding Customers and Restaurants:

Create instances of the Customer and Restaurant classes, specifying given names, family names, and restaurant names.
Save instances to the database using the save() method.
Adding Reviews:

Create instances of the Review class, specifying customer IDs, restaurant IDs, and ratings.
Save instances to the database using the save() method.
Retrieving Information:

Use the all() class method of Customer, Restaurant, and Review classes to retrieve all entries from the respective tables.
