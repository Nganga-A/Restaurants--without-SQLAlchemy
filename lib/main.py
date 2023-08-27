from customer import Customer #imports Customer class from customer.py file
from restaurant import Restaurant 
from review import Review

#SAMPLE  DATA
customer1 = Customer("john","Doe")
customer2 = Customer("Abed", "Doe")
restaurant1 = Restaurant("Choma Zone")
restaurant2 = Restaurant("Smocha Zone")

#REVIEWS SAMPLE DATA
customer1.add_review(restaurant1, 50)
customer1.add_review(restaurant2, 43)
customer2.add_review(restaurant1, 75)
customer2.add_review(restaurant2, 71)

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
    print(f"{restaurant.name}: {restaurant.average_star_rating()}")

# Find customers by given name
print() #To add new line
given_name = "Abed"
print(f"Customers with given name '{given_name}':")
matching_customers = Customer.find_all_by_given_name(given_name)
for customer in matching_customers:
    print(customer.full_name)