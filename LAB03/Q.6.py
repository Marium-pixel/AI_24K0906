#Q.6
class Environment:
  def __init__(self):
    # A B C
    # D E F
    # G H J
    self.grid = [
      'Safe', 'Safe', 'Fire',
      'Safe', 'Fire', 'Safe',
      'Safe', 'Safe', 'Fire'
    ]

  def get_percept(self, position):
    return self.grid[position]

  def extinguish_fire(self, position):
    self.grid[position] = 'Safe'

  def display_grid(self, agent_position):
    print("\nCurrent Environment State:")
    grid_view = []
    for i, room in enumerate(self.grid):
      if i == agent_position:
        grid_view.append('R')  
      elif room == 'Fire':
        grid_view.append(' ~!~')  # FIRE SYMBOLS
      else:
        grid_view.append(' ')   #  SAFE ROOM SYMBOLS

    for i in range(0, 9, 3):
      print(" | ".join(grid_view[i:i+3]))
    print()


class FireFightingRobot:
  def __init__(self):
  #Predefined path AS: a b c d e f g h j
    self.path = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    self.step = 0
    self.position = self.path[self.step]

  def act(self, percept):
    if percept == 'Fire':
      return 'Extinguish Fire'
    else:
      return 'Move On'

  def move(self):
    if self.step < len(self.path) - 1:
      self.step += 1
      self.position = self.path[self.step]


def run_agent(agent, environment):
  for step in range(len(agent.path)):
    percept = environment.get_percept(agent.position)
    action = agent.act(percept)

    print(f"Step {step + 1}: Room {agent.position} -> Percept: {percept}, Action: {action}")

    if percept == 'Fire':
      environment.extinguish_fire(agent.position)

    environment.display_grid(agent.position)
    agent.move()

  print("Final Status: All fires  PUT OUT")

 
environment = Environment()
agent = FireFightingRobot()
 
run_agent(agent, environment)
