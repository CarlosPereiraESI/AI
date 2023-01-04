from copy import copy

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["8:00", "9:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00", "17:00"]
subjects = ["Math", "Science", "English", "History", "Physical Education", "Art", "Music"]
classes = ["Class A", "Class B", "Class C", "Class D"]
teachers = ["Mr. Smith", "Ms. Johnson", "Mrs. Williams", "Mr. Brown", "Ms. Davis", 
"Mrs. Rodriguez", "Mr. Patel", "Mrs. Lee", "Ms. Thompson"]
classrooms = ["Room 101", "Room 102", "Room 103", "Room 104", 
"Room 105", "Room 106", "Room 107", "Room 108", "Room 109"]

# Define the start and goal states as dictionaries
start_state = {"day": "Monday", "hour": "8:00", "subject": "Math", "class": "Class A", "classroom": "Room 101", "teacher": "Mr. Smith"}
goal_state = {"day": "Friday", "hour": "16:00", "subject": "English", "class": "Class B", "classroom": "Room 109", "teacher": "Ms. Davis"}

# Define the actions and their costs
# actions = [
#   {"name": "Move forward in time by one hour", "cost": 1},
#   {"name": "Move backward in time by one hour", "cost": 2},
#   {"name": "Move to next day of the week", "cost": 3},
#   {"name": "Move to previous day of the week", "cost": 4},
#   {"name": "Change subject", "cost": 5},
#   {"name": "Change class", "cost": 6},
#   {"name": "Change teacher", "cost": 7},
#   {"name": "Change classroom", "cost": 8},
# ]

actions = [
{"day": "Monday", "hour": "9:00", "subject": "Science", "class": "Class B", "classroom": "Room 102", "teacher": "Ms. Johnson", "cost": 2},
{"day": "Monday", "hour": "10:00", "subject": "English", "class": "Class C", "classroom": "Room 103", "teacher": "Mrs. Williams", "cost": 1},
{"day": "Monday", "hour": "11:00", "subject": "History", "class": "Class D", "classroom": "Room 104", "teacher": "Mr. Brown", "cost": 6},
{"day": "Tuesday", "hour": "8:00", "subject": "Math", "class": "Class A", "classroom": "Room 101", "teacher": "Mr. Smith", "cost": 5},
{"day": "Tuesday", "hour": "9:00", "subject": "Science", "class": "Class B", "classroom": "Room 102", "teacher": "Ms. Johnson", "cost": 3},
{"day": "Tuesday", "hour": "10:00", "subject": "English", "class": "Class C", "classroom": "Room 103", "teacher": "Mrs. Williams", "cost": 4},
{"day": "Tuesday", "hour": "11:00", "subject": "History", "class": "Class D", "classroom": "Room 104", "teacher": "Mr. Brown", "cost": 1},
{"day": "Wednesday", "hour": "8:00", "subject": "Math", "class": "Class A", "classroom": "Room 101", "teacher": "Mr. Smith", "cost": 6},
{"day": "Wednesday", "hour": "9:00", "subject": "Science", "class": "Class B", "classroom": "Room 102", "teacher": "Ms. Johnson", "cost": 7},
{"day": "Wednesday", "hour": "10:00", "subject": "English", "class": "Class C", "classroom": "Room 103", "teacher": "Mrs. Williams", "cost": 2},
{"day": "Wednesday", "hour": "11:00", "subject": "History", "class": "Class D", "classroom": "Room 104", "teacher": "Mr. Brown", "cost": 5},
{"day": "Thursday", "hour": "8:00", "subject": "Math", "class": "Class A", "classroom": "Room 101", "teacher": "Mr. Smith", "cost": 4},
{"day": "Thursday", "hour": "9:00", "subject": "Science", "class": "Class B", "classroom": "Room 102", "teacher": "Ms. Johnson", "cost": 6},
{"day": "Thursday", "hour": "10:00", "subject": "English", "class": "Class C", "classroom": "Room 103", "teacher": "Mrs. Williams", "cost": 8},
{"day": "Thursday", "hour": "11:00", "subject": "History", "class": "Class D", "classroom": "Room 104", "teacher": "Mr. Brown", "cost": 3},
{"day": "Friday", "hour": "8:00", "subject": "Math", "class": "Class A", "classroom": "Room 101", "teacher": "Mr. Smith", "cost": 1},
{"day": "Friday", "hour": "9:00", "subject": "Science", "class": "Class B", "classroom": "Room 102", "teacher": "Ms. Johnson", "cost": 8},
{"day": "Friday", "hour": "10:00", "subject": "English", "class": "Class C", "classroom": "Room 103", "teacher": "Mrs. Williams", "cost": 2},
{"day": "Friday", "hour": "11:00", "subject": "History", "class": "Class D", "classroom": "Room 104", "teacher": "Mr. Brown", "cost": 3},
{"day": "Friday", "hour": "16:00", "subject": "English", "class": "Class B", "classroom": "Room 109", "teacher": "Ms. Davis", "cost": 20}
]

class AStar:
    def __init__(self, start_state, goal_state, actions, heuristic_cost):
        self.start_state = start_state
        self.goal_state = goal_state
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
        path = []
        path.append(current_state)
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
            if current_state == self.goal_state:
                return self.reconstruct_path(came_from, current_state)
        
            # Remove the current state from the open set and add it to the closed set
            open_set.remove(current_state)
            closed_set.append(current_state)

            states.append(current_state)
            # For each action that can be taken from the current state
            for action in self.actions:
                # Find the new state after taking the action
                new_state = self.get_new_state(current_state, action)
                # If the new state is in the closed set, skip it
                if new_state in closed_set:
                    continue
            
                # Calculate the cost to reach the new state
                cost = g_score[tuple(current_state.items())] + action["cost"]                
                # If the new state is not in the open set, or if the cost to reach the new state is lower than the previous cost, update the cost and came_from values
                if new_state not in open_set or cost < g_score[tuple(new_state.items())]:
                    came_from[tuple(new_state.items())] = current_state
                    g_score[tuple(new_state.items())] = cost
                    f_score[tuple(new_state.items())] = cost + self.heuristic_cost(new_state)
          
                # If the new state is not in the open set, add it to the open set
                if new_state not in open_set:
                    open_set.append(new_state)
        return []
# Define the function to calculate the heuristic cost (estimated cost to reach the goal state)
def heuristic_cost(state):
  day_cost = abs(days_of_week.index(state["day"]) - days_of_week.index(goal_state["day"]))
  hour_cost = abs(hours.index(state["hour"]) - hours.index(goal_state["hour"]))
  subject_cost = abs(subjects.index(state["subject"]) - subjects.index(goal_state["subject"]))
  class_cost = abs(classes.index(state["class"]) - classes.index(goal_state["class"]))
  teacher_cost = abs(teachers.index(state["teacher"]) - teachers.index(goal_state["teacher"]))
  classroom_cost = abs(classrooms.index(state["classroom"]) - classrooms.index(goal_state["classroom"]))
  return day_cost + hour_cost + subject_cost + class_cost + teacher_cost + classroom_cost


states = []
states.append(start_state)
modified_actions = []
for action in actions:
    for state in states:
        if (action["day"] != state["day"] or action["hour"] != state["hour"]) and action["teacher"] != state["teacher"]:
            modified_actions.append(action)

# Initialize the A* algorithm
a_star = AStar(start_state, goal_state, modified_actions, heuristic_cost)

# Find the optimal path to the goal state
path = a_star.find_path()

# Print the optimal path
print(path)