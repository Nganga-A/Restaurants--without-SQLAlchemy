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
