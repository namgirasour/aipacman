from game import Agent
from game import Directions
import random

class BasicAgent(Agent):
  """This agents just heads North until it cannot move"""
  def getAction(self, state):
      if Directions.NORTH in state.getLegalPacmanActions():
          return Directions.NORTH
      else: 
          return Directions.STOP
      

class RandomAgent(Agent):

    
    def getAction(self, state):
        legal = state.getLegalPacmanActions()
        
        # If STOP is the only legal action, return it
        if len(legal) == 1 and Directions.STOP in legal:
            return Directions.STOP
        
        # Remove the STOP action from the list of legal actions if available
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        
        # Choose randomly from the legal actions and return t action.
        return random.choice(legal)
    
class ReflexAgent(Agent):
    def getAction(self, state):
        legal = state.getLegalPacmanActions()
        
        # If STOP is the only legal action, return it
        if len(legal) == 1 and Directions.STOP in legal:
            return Directions.STOP
        
        # Else, remove the STOP action from the list of legal actions if available
        if Directions.STOP in legal:
            legal.remove(Directions.STOP)
        
        # Locations of the dot
        food = state.getFood()
        
        # Check for each legal action if it leads to a position with a dot
        food_actions = []
        for action in legal:
            # Get the next state based on the current action
            next_state = state.generateSuccessor(0, action)
            # Find the position of Pacman in the next state
            next_position = next_state.getPacmanPosition()
            if food[next_position[0]][next_position[1]]:
                food_actions.append(action)
        
        # If there are actions that lead to food, choose randomly
        if food_actions:
            return random.choice(food_actions)
        
        # If no food is found, choose randomly legal actions
        return random.choice(legal)
    
    
    
        
    
            
          
        
