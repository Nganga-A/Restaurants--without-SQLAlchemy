# Restaurants--without-SQLAlchemy  ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
A simple review system for restaurants, customers and their reviews

## Overview

This project implements a basic review system where customers can review restaurants and calculate the average star rating for each restaurant. It includes three main classes: `Customer`, `Restaurant`, and `Review`.


# Getting Started

## Project Setup

1. Clone the repository
```
git clone git@github.com:Nganga-A/Restaurants--without-SQLAlchemy.git
```

2. Install required dependencies
```
cd into the project directory
```

3. Run the main script 


## Project Composition

This repository contains four Python files

    1. customer.py - Contains the `Customer` class implementation.

    2. review.py - Contains the `Review` class implementation.

    3. restaurant.py - Contains the `Restaurant` class implementation.

    4. main.py - The main script to run the project.

    project_folder/
    │
    ├── customer.py
    ├── restaurant.py
    ├── review.py
    └── main.py


## Usage

The system allows you to:

- Create customers, restaurants, and reviews.
- Associate customers with their reviews and restaurants with their reviews.
- Calculate average star ratings for restaurants.
- Find customers by given name.

## Example Usage

```python
from customer import Customer #imports Customer class from customer.py file
from restaurant import Restaurant 
from review import Review

#SAMPLE  DATA
customer1 = Customer("john","Doe")
customer2 = Customer("Abed", "Doe")
restaurant1 = Restaurant("Choma Zone")
restaurant2 = Restaurant("Smocha Zone")

#REVIEWS SAMPLE DATA
# Creating Review instances
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 14)
review3 = Review(customer1, restaurant2, 8)
review4 = Review(customer2, restaurant2, 7)


# Print all customers
print("All Customers: ")
for customer in Customer.all():
    print(customer.full_name)

# Print all restaurants
print() #To add new line
print("All Restaurants: ")
for restaurant in Restaurant.all():
    print(restaurant.name)

# Print average star rating for each restaurant
print() #To add new line
print("Average Star Ratings: ")
for restaurant in Restaurant.all():
    avg_rating = restaurant.average_star_rating()
    print(f"{restaurant.name}: {avg_rating}")

# Find customers by given name
print() #To add new line
given_name = "Abed"
print(f"Customers with given name '{given_name}':")
matching_customers = Customer.find_all_by_given_name(given_name)
for customer in matching_customers:
    print(customer.full_name)

#Print number of Reviews for Each customer 
print() #To add new line
print("Number of Reviews for Each customer")
for customer in customer.all():
    num_reviews = customer.num_review()
    print(f"{customer.full_name}'s Reviews: {num_reviews}")


# Print list of reviews for each customer
print()
print("List of Reviews for Each Customer:")
for customer in Customer.all():
    print(f"{customer.full_name}'s Reviews:")
    for review in customer.reviews:
        print(f"  - Restaurant: {review.restaurant().name}")
        print(f"    Rating: {review.get_rating()}")


```
## Results from Example Usage

```python

All Customers: 
john Doe
Abed Doe

All Restaurants: 
Choma Zone
Smocha Zone

Average Star Ratings: 
Choma Zone: 9.0
Smocha Zone: 7.5

Customers with given name 'Abed':
Abed Doe

Number of Reviews for Each customer
john Doe's Reviews: 2
Abed Doe's Reviews: 2

List of Reviews for Each Customer:
john Doe's Reviews:
  - Restaurant: Choma Zone
    Rating: 4
  - Restaurant: Smocha Zone
    Rating: 8
Abed Doe's Reviews:
  - Restaurant: Choma Zone
    Rating: 14
  - Restaurant: Smocha Zone
    Rating: 7

```

## Contribution

Contributions are welcome! Please open an issue or pull request for any improvements or bug fixes.


## License

This project is licensed under the [MIT License](LICENSE).

## Author

Created by [Abed Nganga Njuguna ](https://github.com/Nganga-A)