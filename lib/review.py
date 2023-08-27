class Review:
    REVIEWS = [] # list of reviews

    def __init__(self,customer,restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.REVIEWS.append(self) # Add the review instance to the list of all reviews
        customer.add_review(restaurant, rating) # Associate the review with customer and restaurant
        restaurant.reviews.append(self)  # Add the review to the restaurant's list of reviews
    
    def rating(self):
        return self.rating  # Return the rating of the review
    
    @classmethod
    def all(cls):
        return cls.REVIEWS  # Return all review instances created
    
    def customer(self):
        return self.customer  # Return the associated customer instance
    
    def restaurant(self):
        return self.restaurant  # Return the associated restaurant instance