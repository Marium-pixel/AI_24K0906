#q.1:

class Environment:
  def __init__(self,state = 'Heavy Traffic') :
    self.state = state

  def percept(self):
    return self.state

class ReflexAgent:
  def __init__(self):
    pass
  def takeaction(self,percept):
    if percept == 'Heavy Traffic':
      return 'Extend green'
    else :
      return 'Normal green'

def run_agent(agent,environment):
  percept = environment.percept()
  action = agent.takeaction(percept)
  print(f"Percent: {percept} , Action taken: {action}")

agent = ReflexAgent()
environment = Environment()

run_agent(agent,environment)
