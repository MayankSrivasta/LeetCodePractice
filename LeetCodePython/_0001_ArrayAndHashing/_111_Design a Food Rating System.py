
from collections import defaultdict
from typing import List
from sortedcontainers import SortedSet

class FoodRatings:

# If there is a tie in the rating, return the lexicographically smallest name.
# SortedSet: Maintains sorted order and ensures uniqueness (important!)
# The sorting will use (-rating, food) tuples to:
# Sort by highest rating first (-rating makes it descending)
# In case of ties, food (string) is sorted lexicographically ascending

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToRating = {} # food -> rating
        self.foodToCuisine = {} # food -> cuisine
        self.cuisineToSortedSet = defaultdict(SortedSet) # cuisine -> SortedSet[(rating, food)]

        for i in range(len(foods)):
            self.foodToRating[foods[i]] = ratings[i]
            self.foodToCuisine[foods[i]] = cuisines[i]
            self.cuisineToSortedSet[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        oldRating = self.foodToRating[food]

        self.cuisineToSortedSet[cuisine].remove((-oldRating, food))
        self.foodToRating[food] = newRating
        self.cuisineToSortedSet[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineToSortedSet[cuisine][0][1]


