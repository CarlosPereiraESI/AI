from copy import copy
from data import *

class AStar:
    def __init__(self, start_state, goal_states, actions, heuristic_cost):
        self.start_state = start_state
        self.goal_states = goal_states
        self.actions = actions
        self.heuristic_cost = heuristic_cost

    def get_new_state(self, current_state, action):
        # Update the current state based on the action
        new_state = copy(current_state)
        for key in action:
            # If the key is in the state, update the value in the new state
            if key in new_state:
                new_state[key] = action[key]
        return new_state
    
    def reconstruct_path(self, came_from, current_state):
        path = [dict(current_state)]
        while tuple(current_state.items()) in came_from:
            # Set the current state to its predecessor
            print(current_state, came_from)
            current_state = came_from[tuple(current_state.items())]
            path.append(current_state)
        return path[::-1]

    def find_path(self):
        # Initialize the open and closed sets
        open_set = []
        closed_set = []
        
        # Add the start state to the open set
        open_set.append(self.start_state)
        
        # Initialize the came_from dictionary
        came_from = {}
        
        # Initialize the g_score (cost to reach each state) and f_score (estimated total cost to reach the goal state) dictionaries
        g_score = {tuple(self.start_state.items()): 0}
        f_score = {tuple(self.start_state.items()): self.heuristic_cost(self.start_state)}
        
        # While the open set is not empty
        while open_set:
        # Find the state in the open set with the lowest f_score
            current_state = min(open_set, key=lambda s: f_score[tuple(s.items())])
            # If the current state is the goal state, return the path
            if dict(current_state) in self.goal_states:
                return self.reconstruct_path(came_from, current_state)
            # Remove the current state from the open set and add it to the closed set
            open_set.remove(current_state)
            closed_set.append(current_state)

            states.append(current_state)
            # For each action that can be taken from the current state
            for action in self.actions:
                # Find the new state after taking the action
                new_state = self.get_new_state(dict(current_state), action)
                # If the new state is in the closed set, skip it
                if tuple(new_state.items()) in closed_set:
                    continue

                # Calculate the cost to reach the new state
                cost = g_score[tuple(current_state.items())] + action["cost"]                
                # If the new state is not in the open set, or if the cost to reach the new state is lower than the previous cost, update the cost and came_from values
                if new_state not in open_set or cost < g_score[tuple(new_state.items())]:
                    came_from[tuple(new_state.items())] = current_state
                    g_score[tuple(new_state.items())] = cost
                    f_score[tuple(new_state.items())] = cost + self.heuristic_cost(new_state)
          
                # If the new state is not in the open set, add it to the open set
                if tuple(new_state.items()) not in open_set:
                    open_set.append(new_state)
        return []
# Define the function to calculate the heuristic cost (estimated cost to reach the goal state)
def heuristic_cost(state):
    min_cost = float("inf")
    for goal_state in goal_states:
        day_cost = abs(days_of_week.index(state["day"]) - days_of_week.index(goal_state["day"]))
        hour_cost = abs(hours.index(state["hour"]) - hours.index(goal_state["hour"]))
        subject_cost = abs(subjects.index(state["subject"]) - subjects.index(goal_state["subject"]))
        class_cost = abs(classes.index(state["class"]) - classes.index(goal_state["class"]))
        teacher_cost = abs(teachers.index(state["teacher"]) - teachers.index(goal_state["teacher"]))
        classroom_cost = abs(classrooms.index(state["classroom"]) - classrooms.index(goal_state["classroom"]))
    total = day_cost + hour_cost + subject_cost + class_cost + teacher_cost + classroom_cost
    min_cost = min(min_cost, total)
    return min_cost


states = []
states.append(start_state)
modified_actions = []
for action in actions:
    for state in states:
        if (action["day"] != state["day"] or action["hour"] != state["hour"]
            and action["teacher"] != state["teacher"] and action["classroom"] != state["classroom"]):
            modified_actions.append(action)

# Initialize the A* algorithm
a_star = AStar(start_state, goal_states, modified_actions, heuristic_cost)

# Find the optimal path to the goal state
path = a_star.find_path()

# Print the optimal path
print(path)