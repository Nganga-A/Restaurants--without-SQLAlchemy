class Restaurant:
    RESTAURANTS = []

    def __init__ (self, name):
        self.name = name
        self.reviews = [] # List to store reviews associated with this restaurant
        Restaurant.all_restaurants.append(self)  # Add the instance to the list of all restaurants

    def name (self):
        return self.name # Return the name of the restaurant
    
    def reviews (self):
        return self.reviews # Return the reviews associated with this restaurant
    
    @classmethod
    def all (cls):
        return cls.RESTAURANTS ## Return all restaurant instances created

    def reviews (self):
        return self.reviews # Return the reviews associated with this 
    
    def customers (self):
        return list({review.customer() for review in self.reviews})
    #Get customers who have reviewed this restaurant

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_rating = sum(review.rating() for review in self.reviews)
        return total_rating / len(self.reviews)
        # Calculate and return the average star rating of the restaurant