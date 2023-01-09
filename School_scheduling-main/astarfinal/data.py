days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["9-11", "11-13", "14-16", "16-18", "18-20"]
subjects = ["Artificial Inteligence", "Applied Project", "Mobile Programming", "Systems Integration", 
"Embedded Systems", "Calculus", "Discrete Maths", "Informatics Labs", "Imperative Programming", 
"Computers Architecture", "Object-Oriented Programming", "Statistics", "Physics", "Data Storage", "Software Engineering"]
classes = ["LESI1", "LESI2", "LESI3", "LESI-PL1", "LESI-PL2", "LESI-PL3"]
teachers = ["Joaquim Gonçalves", "Patrícia Leite", "Nuno Mendes", "Luís Ferreira", "Paulo Macedo", 
"Natália Rego", "Teresa Abreu", "Óscar Ribeiro", "Nuno Rodrigues", "Sandro Carvalho", "Andreia Monteiro",
"Daniel Miranda", "Paulo Teixeira", "Joaquim Silva"]
classrooms = ["Room T", "Room E", "Room C", "Room N", "Room IOT", 
"Room Networking", "Room Auditorium", "Room Automation", "Room Electronics"]

# Define the start and goal states as dictionaries
start_state = {"day": "Monday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room T", "teacher": "Joaquim Gonçalves"}

actions = [
{"day": "Monday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 2},
{"day": "Monday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 1},
{"day": "Monday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 6},
{"day": "Tuesday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI-PL2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 5},
{"day": "Tuesday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 3},
{"day": "Tuesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 4},
{"day": "Tuesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 1},
{"day": "Wednesday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI-PL2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 6},
{"day": "Wednesday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 7},
{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 2},
{"day": "Wednesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 5},
{"day": "Thursday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI-PL2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 4},
{"day": "Thursday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 6},
{"day": "Thursday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 8},
{"day": "Thursday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 3},
{"day": "Friday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI-PL2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 1},
{"day": "Friday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 8},
{"day": "Friday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 2},
{"day": "Friday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 3},
{"day": "Friday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI-PL1", "classroom": "Room E", "teacher": "Teresa Abreu", "cost": 20}
]

goal_states = [
    {"day": "Friday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite"},
    {"day": "Friday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
    {"day": "Friday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI-PL1", "classroom": "Room E", "teacher": "Teresa Abreu"}
    ]
