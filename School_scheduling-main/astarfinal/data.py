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


# AP, AI, MP, SI, ES
#
#
#
#
#
#
#
#
actions = [
{"day": "Monday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 1},
{"day": "Monday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 6},
{"day": "Monday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 10},
{"day": "Monday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 15},
{"day": "Monday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 20},

{"day": "Monday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 1},
{"day": "Monday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 6},
{"day": "Monday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 10},
{"day": "Monday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 15},
{"day": "Monday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 20},

{"day": "Monday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room N", "teacher": "Patrícia Leite", "cost": 1},
{"day": "Monday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room N", "teacher": "Patrícia Leite", "cost": 6},
{"day": "Monday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room N", "teacher": "Patrícia Leite", "cost": 10},
{"day": "Monday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room N", "teacher": "Patrícia Leite", "cost": 15},
{"day": "Monday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room N", "teacher": "Patrícia Leite", "cost": 20},

{"day": "Tuesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 1},
{"day": "Tuesday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 5},
{"day": "Tuesday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 12},
{"day": "Tuesday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 15},
{"day": "Tuesday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 20},

{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 2},
{"day": "Wednesday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 7},
{"day": "Wednesday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 15},
{"day": "Wednesday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 16},
{"day": "Wednesday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 20},

{"day": "Thusrday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 2},
{"day": "Thusrday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 7},
{"day": "Thusrday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 15},
{"day": "Thusrday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 16},
{"day": "Thusrday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 20},

{"day": "Monday", "hour": "11-13", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", "cost": 5},
{"day": "Monday", "hour": "14-16", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", "cost": 10},
{"day": "Monday", "hour": "16-18", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", "cost": 15},
{"day": "Monday", "hour": "18-20", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", "cost": 20},
{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 1},
{"day": "Wednesday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 5},
{"day": "Wednesday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 10},
{"day": "Wednesday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 15},
{"day": "Wednesday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", "cost": 20},
{"day": "Monday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 6},
{"day": "Tuesday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 5},
{"day": "Tuesday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 3},
{"day": "Tuesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 4},
{"day": "Tuesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 1},
{"day": "Wednesday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 6},
{"day": "Wednesday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 7},
{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 2},
{"day": "Wednesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 5},
{"day": "Thursday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 4},
{"day": "Thursday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 6},
{"day": "Thursday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 8},
{"day": "Thursday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 3},
{"day": "Friday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", "cost": 1},
{"day": "Friday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI1", "classroom": "Room T", "teacher": "Joaquim Gonçalves", "cost": 8},
{"day": "Friday", "hour": "9-11", "subject": "Applied Project", "class": "LESI2", "classroom": "Room E", "teacher": "Patrícia Leite", "cost": 2},
{"day": "Friday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", "cost": 3},
{"day": "Friday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room E", "teacher": "Teresa Abreu", "cost": 20}
]

goal_states = [
    #1ano
    {"day": "Monday", "hour": "9-11", "subject": "Calculus", "class": "LESI1", "classroom": "Room T", "teacher": "Natália Rego"},
    {"day": "Monday", "hour": "11-13", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room Networking", "teacher": "Nuno Rodrigues"},
    {"day": "Monday", "hour": "14-16", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},

    {"day": "Tuesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI1", "classroom": "Room E", "teacher": "Patrícia Leite"},
    {"day": "Tuesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI1", "classroom": "Room C", "teacher": "Nuno Mendes"},
    
    {"day": "Thursday", "hour": "9-11", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room N", "teacher": "Teresa Abreu"},
    {"day": "Thursday", "hour": "11-13", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room E", "teacher": "Óscar Ribeiro"},
    {"day": "Thursday", "hour": "14-16", "subject": "Calculus", "class": "LESI1", "classroom": "Room E", "teacher": "Natália Rego"},

    {"day": "Friday", "hour": "9-11", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room E", "teacher": "Sandro Carvalho"},
    {"day": "Friday", "hour": "11-13", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room C", "teacher": "Nuno Rodrigues"},
    

    #2ano
    {"day": "Tuesday", "hour": "9-11", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
    {"day": "Tuesday", "hour": "11-13", "subject": "Statistics", "class": "LESI2", "classroom": "Room E", "teacher": "Andreia Monteiro"},
    {"day": "Tuesday", "hour": "14-16", "subject": "Physics", "class": "LESI2", "classroom": "Room IOT", "teacher": "Daniel Miranda"},

    {"day": "Wednesday", "hour": "9-11", "subject": "Data Storage", "class": "LESI2", "classroom": "Room T", "teacher": "Paulo Teixeira"},
    {"day": "Wednesday", "hour": "11-13", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},

    {"day": "Thursday", "hour": "9-11", "subject": "Statistics", "class": "LESI2", "classroom": "Room E", "teacher": "Andreia Monteiro"},
    {"day": "Thursday", "hour": "11-13", "subject": "Physics", "class": "LESI2", "classroom": "Room C", "teacher": "Daniel Miranda"},

    {"day": "Friday", "hour": "9-11", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room IOT", "teacher": "Joaquim Silva"},
    {"day": "Friday", "hour": "11-13", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
    {"day": "Friday", "hour": "14-16", "subject": "Data Storage", "class": "LESI2", "classroom": "Room E", "teacher": "Paulo Teixeira"},


    #3ano
    {"day": "Monday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI3", "classroom": "Room Auditorium", "teacher": "Paulo Macedo"},
    {"day": "Monday", "hour": "11-13", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves"},
    {"day": "Monday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite"},

    {"day": "Tuesday", "hour": "9-11", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo"},
    {"day": "Tuesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},

    {"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite"},
    {"day": "Wednesday", "hour": "11-13", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves"},

    {"day": "Thursday", "hour": "9-11", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes"},
    {"day": "Thursday", "hour": "11-13", "subject": "Systems Integration", "class": "LESI3", "classroom": "Room Auditorium", "teacher": "Luís Ferreira"},
    {"day": "Thursday", "hour": "14-16", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo"}
    ]


