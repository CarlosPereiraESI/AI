import heapq

class Class:
  def __init__(self, teacher, subject, classroom):
    self.teacher = teacher
    self.subject = subject
    self.classroom = classroom

class Schedule:
  def __init__(self):
    self.classes = []
  
  def add_class(self, classs):
    self.classes.append(classs)

def find_class(schedule, subject):
  start = (0, subject)
  frontier = []
  heapq.heappush(frontier, start)
  came_from = {}
  cost_so_far = {}
  came_from[start] = None
  cost_so_far[start] = 0
  
  while len(frontier) > 0:
    current = heapq.heappop(frontier)
    
    if current[1] == subject:
      path = []
      while current != start:
        path.append(current)
        current = came_from[current]
      path.append(start)
      path.reverse()
      return path
    
    for next in schedule.classes:
      new_cost = cost_so_far[current] + 1
      if next not in cost_so_far or new_cost < cost_so_far[next]:
        cost_so_far[next] = new_cost
        priority = new_cost + heuristic(next, subject)
        heapq.heappush(frontier, (priority, next))
        came_from[next] = current
  
  return None

def heuristic(classs, goal):
  return abs(classs.subject - goal.subject)

schedule = Schedule()
schedule.add_class(Class("Ms. Smith", "Math", "Room 101"))
schedule.add_class(Class("Mr. Johnson", "Science", "Room 102"))
schedule.add_class(Class("Mrs. Williams", "English", "Room 103"))

math_class = find_class(schedule, "Math")
print(math_class)
   