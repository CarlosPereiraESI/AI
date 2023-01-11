days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours = ["9-11", "11-13", "14-16", "16-18", "18-20"]
subjects = ["Artificial Inteligence", "Applied Project", "Mobile Programming", "Systems Integration", 
"Embedded Systems", "Calculus", "Discrete Maths", "Informatics Labs", "Imperative Programming", 
"Computers Architecture", "Object-Oriented Programming", "Statistics", "Physics", "Data Storage", "Software Engineering"]
classes = ["LESI1", "LESI2", "LESI3"]
teachers = ["Joaquim Gonçalves", "Patrícia Leite", "Nuno Mendes", "Luís Ferreira", "Paulo Macedo", 
"Natália Rego", "Teresa Abreu", "Óscar Ribeiro", "Nuno Rodrigues", "Sandro Carvalho", "Andreia Monteiro",
"Daniel Miranda", "Paulo Teixeira", "Joaquim Silva"]
classrooms = ["Room T", "Room E", "Room C", "Room N", "Room IOT", 
"Room Networking", "Room Auditorium", "Room Automation", "Room Electronics"]

# Define the start and goal states as dictionaries
start_state = {"day": "Monday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room T", "teacher": "Joaquim Gonçalves"}

actions = [
{"day": "Monday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Monday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Monday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Monday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Monday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Monday", "hour": "11-13", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves"},
{"day": "Monday", "hour": "14-16", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves"},
{"day": "Monday", "hour": "16-18", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves"},
{"day": "Monday", "hour": "18-20", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves"},
{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
{"day": "Monday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
{"day": "Tuesday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira"},
{"day": "Tuesday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves"},
{"day": "Tuesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Tuesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
{"day": "Wednesday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira"},
{"day": "Wednesday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves"},
{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Wednesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
{"day": "Thursday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira"},
{"day": "Thursday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves"},
{"day": "Thursday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Thursday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
{"day": "Friday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira"},
{"day": "Friday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves"},
{"day": "Friday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite"},
{"day": "Friday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
{"day": "Friday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room E", "teacher": "Teresa Abreu"}
]

goal_states = [
    {"day": "Monday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite"},
    {"day": "Friday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
    {"day": "Friday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room E", "teacher": "Teresa Abreu"}
    ]
