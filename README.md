# Restaurants--without-SQLAlchemy 
![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
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
from customer import Customer
from restaurant import Restaurant
from review import Review

# Create instances
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Choma Zone")
review1 = Review(customer1, restaurant1, 4)

# Calculate average star rating
avg_rating = restaurant1.average_star_rating()
print(f"Average Rating for {restaurant1.name}: {avg_rating}")
```

## Contribution

Contributions are welcome! Please open an issue or pull request for any improvements or bug fixes.


## License

This project is licensed under the [MIT License](LICENSE).

## Author

Created by [Abed Nganga Njuguna ](https://github.com/Nganga-A)