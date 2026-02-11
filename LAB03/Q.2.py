#q.2:
import random
class Environment:
  def __init__(self, students='No', lights='On'):
    self.students=students
    self.lights=lights
  
  def get_percept(self): 
    return {'students': self.students, 'lights': self.lights}

  def update_students(self):
    self.students = random.choice(['Yes', 'No'])

  def lightsoff(self):
      self.lights= 'Off'
  def lightson(self): 
    self.lights= 'On'

class ModelBasedAgent:
  def __init__(self):
    self.model = {'students' : 'No', 'lights' : 'On'}

  
    
  def act(self,percept):
    """Decides action based on the model(students and lights) and current percept.""" 

    self.model.update(percept)

    if self.model['students'] == 'Yes' and self.model['lights']== 'Off':
      return 'turn on lights'
    elif self.model['students']== 'No' and self.model ['lights'] == 'On':
      return 'turn off lights'
    else :
      return 'no action needed'

def run_agent(agent,environment,steps):
  for step in range(steps):
    environment.update_students()
    percept = environment.get_percept()
    action = agent.act(percept)

    print('step:', step+1, 'percept:' ,percept, 'Action:',action )

    if action == 'turn off lights':
      environment.lightsoff()
    if action =='turn on lights':
      environment.lightson()
    


agent = ModelBasedAgent()
environment = Environment()
run_agent(agent,environment,8)





 
