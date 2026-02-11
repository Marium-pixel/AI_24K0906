#q4:
class Environment:
  def __init__(self, restaurants):
    self.restaurants = restaurants

  def get_percept(self):
    """Returns restaurant distance and rating."""
    return self.restaurants


class UtilityBasedAgent:
  def utility(self, rating, distance):
    """Compute utility = Rating - Distance"""
    return rating - distance

  def act(self, percept):
    best_restaurant = None
    best_utility = -float('inf')

    for restaurant, values in percept.items():
      rating = values['rating']
      distance = values['distance']
      u = self.utility(rating, distance)

      print(f"Restaurant {restaurant} Utility = {u}")

      if u > best_utility:
        best_utility = u
        best_restaurant = restaurant

    return best_restaurant


def run_agent(agent, environment):
  percept = environment.get_percept()
  selected = agent.act(percept)
  print(f"Selected Restaurant: {selected}")
 
agent = UtilityBasedAgent()

environment = Environment({
  'A': {'distance': 3, 'rating': 7},
  'B': {'distance': 5, 'rating': 9}
})
 
run_agent(agent, environment)
