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
start_state = {"day": "Monday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves"}

actions = [
# -------------------------------------- Terceiro Ano ------------------------------------------------------------

{"day": "Monday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", },
{"day": "Monday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", },
{"day": "Monday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", },
{"day": "Monday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", },
{"day": "Monday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room E", "teacher": "Patrícia Leite", },
{"day": "Wednesday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Wednesday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Wednesday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Wednesday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Wednesday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Friday", "hour": "9-11", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Friday", "hour": "11-13", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Friday", "hour": "14-16", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Friday", "hour": "16-18", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Friday", "hour": "18-20", "subject": "Applied Project", "class": "LESI3", "classroom": "Room T", "teacher": "Patrícia Leite", },
{"day": "Monday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Monday", "hour": "11-13", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Monday", "hour": "14-16", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Monday", "hour": "16-18", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Monday", "hour": "18-20", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Wednesday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Wednesday", "hour": "11-13", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Wednesday", "hour": "14-16", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Wednesday", "hour": "16-18", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Wednesday", "hour": "18-20", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Thursday", "hour": "9-11", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Thursday", "hour": "11-13", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Thursday", "hour": "14-16", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Thursday", "hour": "16-18", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Thursday", "hour": "18-20", "subject": "Artificial Inteligence", "class": "LESI3", "classroom": "Room C", "teacher": "Joaquim Gonçalves", },
{"day": "Monday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Monday", "hour": "11-13", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Monday", "hour": "14-16", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Monday", "hour": "16-18", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Monday", "hour": "18-20", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Thursday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Thursday", "hour": "11-13", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Thursday", "hour": "14-16", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Thursday", "hour": "16-18", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Thursday", "hour": "18-20", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Friday", "hour": "9-11", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Friday", "hour": "11-13", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Friday", "hour": "14-16", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Friday", "hour": "16-18", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Friday", "hour": "18-20", "subject": "Systems Integration", "class": "LESI2", "classroom": "Room Auditorium", "teacher": "Luís Ferreira", },
{"day": "Tuesday", "hour": "9-11", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Tuesday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Tuesday", "hour": "14-16", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Tuesday", "hour": "16-18", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Tuesday", "hour": "18-20", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Thursday", "hour": "9-11", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Thursday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Thursday", "hour": "14-16", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Thursday", "hour": "16-18", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Thursday", "hour": "18-20", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Monday", "hour": "9-11", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Monday", "hour": "11-13", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Monday", "hour": "14-16", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Monday", "hour": "16-18", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Monday", "hour": "18-20", "subject": "Mobile Programming", "class": "LESI3", "classroom": "Room C", "teacher": "Nuno Mendes", },
{"day": "Tuesday", "hour": "9-11", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Tuesday", "hour": "11-13", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Tuesday", "hour": "14-16", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Tuesday", "hour": "16-18", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Tuesday", "hour": "18-20", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Thursday", "hour": "9-11", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Thursday", "hour": "11-13", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Thursday", "hour": "14-16", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Thursday", "hour": "16-18", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo", },
{"day": "Thursday", "hour": "18-20", "subject": "Embedded Systems", "class": "LESI3", "classroom": "Room Electronics", "teacher": "Paulo Macedo"},

# ----------------------------------------------- Segundo Ano ---------------------------------------------

{"day": "Monday", "hour": "9-11", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room E", "teacher": "Luís Ferreira"},
{"day": "Monday", "hour": "11-13", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room E", "teacher": "Luís Ferreira"},
{"day": "Monday", "hour": "14-16", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room E", "teacher": "Luís Ferreira"},
{"day": "Monday", "hour": "16-18", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room E", "teacher": "Luís Ferreira"},
{"day": "Monday", "hour": "18-20", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room E", "teacher": "Luís Ferreira"},
{"day": "Tuesday", "hour": "9-11", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Tuesday", "hour": "11-13", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Tuesday", "hour": "14-16", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Tuesday", "hour": "16-18", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Tuesday", "hour": "18-20", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Friday", "hour": "9-11", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Friday", "hour": "11-13", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Friday", "hour": "14-16", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Friday", "hour": "16-18", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Friday", "hour": "18-20", "subject": "Object-Oriented Programming", "class": "LESI2", "classroom": "Room T", "teacher": "Luís Ferreira"},
{"day": "Tuesday", "hour": "9-11", "subject": "Statistics", "class": "LESI2", "classroom": "Room N", "teacher": "Andreia Monteiro"},
{"day": "Tuesday", "hour": "11-13", "subject": "Statistics", "class": "LESI2", "classroom": "Room N", "teacher": "Andreia Monteiro"},
{"day": "Tuesday", "hour": "14-16", "subject": "Statistics", "class": "LESI2", "classroom": "Room IOT", "teacher": "Andreia Monteiro"},
{"day": "Tuesday", "hour": "16-18", "subject": "Statistics", "class": "LESI2", "classroom": "Room T", "teacher": "Andreia Monteiro"},
{"day": "Tuesday", "hour": "18-20", "subject": "Statistics", "class": "LESI2", "classroom": "Room C", "teacher": "Andreia Monteiro"},
{"day": "Wednesday", "hour": "9-11", "subject": "Statistics", "class": "LESI2", "classroom": "Room E", "teacher": "Andreia Monteiro"},
{"day": "Wednesday", "hour": "11-13", "subject": "Statistics", "class": "LESI2", "classroom": "Room E", "teacher": "Andreia Monteiro"},
{"day": "Wednesday", "hour": "14-16", "subject": "Statistics", "class": "LESI2", "classroom": "Room E", "teacher": "Andreia Monteiro"},
{"day": "Wednesday", "hour": "16-18", "subject": "Statistics", "class": "LESI2", "classroom": "Room N", "teacher": "Andreia Monteiro"},
{"day": "Wednesday", "hour": "18-20", "subject": "Statistics", "class": "LESI2", "classroom": "Room T", "teacher": "Andreia Monteiro"},
{"day": "Thursday", "hour": "9-11", "subject": "Statistics", "class": "LESI2", "classroom": "Room E", "teacher": "Andreia Monteiro"},
{"day": "Thursday", "hour": "11-13", "subject": "Statistics", "class": "LESI2", "classroom": "Room E", "teacher": "Andreia Monteiro"},
{"day": "Thursday", "hour": "14-16", "subject": "Statistics", "class": "LESI2", "classroom": "Room N", "teacher": "Andreia Monteiro"},
{"day": "Thursday", "hour": "16-18", "subject": "Statistics", "class": "LESI2", "classroom": "Room IOT", "teacher": "Andreia Monteiro"},
{"day": "Thursday", "hour": "18-20", "subject": "Statistics", "class": "LESI2", "classroom": "Room C", "teacher": "Andreia Monteiro"},
{"day": "Tuesday", "hour": "9-11", "subject": "Physics", "class": "LESI2", "classroom": "Room IOT", "teacher": "Daniel Miranda"},
{"day": "Tuesday", "hour": "11-13", "subject": "Physics", "class": "LESI2", "classroom": "Room IOT", "teacher": "Daniel Miranda"},
{"day": "Tuesday", "hour": "14-16", "subject": "Physics", "class": "LESI2", "classroom": "Room IOT", "teacher": "Daniel Miranda"},
{"day": "Tuesday", "hour": "16-18", "subject": "Physics", "class": "LESI2", "classroom": "Room N", "teacher": "Daniel Miranda"},
{"day": "Tuesday", "hour": "18-20", "subject": "Physics", "class": "LESI2", "classroom": "Room N", "teacher": "Daniel Miranda"},
{"day": "Thursday", "hour": "9-11", "subject": "Physics", "class": "LESI2", "classroom": "Room T", "teacher": "Daniel Miranda"},
{"day": "Thursday", "hour": "11-13", "subject": "Physics", "class": "LESI2", "classroom": "Room N", "teacher": "Daniel Miranda"},
{"day": "Thursday", "hour": "14-16", "subject": "Physics", "class": "LESI2", "classroom": "Room C", "teacher": "Daniel Miranda"},
{"day": "Thursday", "hour": "16-18", "subject": "Physics", "class": "LESI2", "classroom": "Room C", "teacher": "Daniel Miranda"},
{"day": "Thursday", "hour": "18-20", "subject": "Physics", "class": "LESI2", "classroom": "Room E", "teacher": "Daniel Miranda"},
{"day": "Friday", "hour": "9-11", "subject": "Physics", "class": "LESI2", "classroom": "Room T", "teacher": "Daniel Miranda"},
{"day": "Friday", "hour": "11-13", "subject": "Physics", "class": "LESI2", "classroom": "Room T", "teacher": "Daniel Miranda"},
{"day": "Friday", "hour": "14-16", "subject": "Physics", "class": "LESI2", "classroom": "Room T", "teacher": "Daniel Miranda"},
{"day": "Friday", "hour": "16-18", "subject": "Physics", "class": "LESI2", "classroom": "Room T", "teacher": "Daniel Miranda"},
{"day": "Friday", "hour": "18-20", "subject": "Physics", "class": "LESI2", "classroom": "Room N", "teacher": "Daniel Miranda"},
{"day": "Monday", "hour": "9-11", "subject": "Data Storage", "class": "LESI2", "classroom": "Room E", "teacher": "Paulo Teixeira"},
{"day": "Monday", "hour": "11-13", "subject": "Data Storage", "class": "LESI2", "classroom": "Room E", "teacher": "Paulo Teixeira"},
{"day": "Monday", "hour": "14-16", "subject": "Data Storage", "class": "LESI2", "classroom": "Room C", "teacher": "Paulo Teixeira"},
{"day": "Monday", "hour": "16-18", "subject": "Data Storage", "class": "LESI2", "classroom": "Room T", "teacher": "Paulo Teixeira"},
{"day": "Monday", "hour": "18-20", "subject": "Data Storage", "class": "LESI2", "classroom": "Room T", "teacher": "Paulo Teixeira"},
{"day": "Wednesday", "hour": "9-11", "subject": "Data Storage", "class": "LESI2", "classroom": "Room N", "teacher": "Paulo Teixeira"},
{"day": "Wednesday", "hour": "11-13", "subject": "Data Storage", "class": "LESI2", "classroom": "Room T", "teacher": "Paulo Teixeira"},
{"day": "Wednesday", "hour": "14-16", "subject": "Data Storage", "class": "LESI2", "classroom": "Room T", "teacher": "Paulo Teixeira"},
{"day": "Wednesday", "hour": "16-18", "subject": "Data Storage", "class": "LESI2", "classroom": "Room IOT", "teacher": "Paulo Teixeira"},
{"day": "Wednesday", "hour": "18-20", "subject": "Data Storage", "class": "LESI2", "classroom": "Room C", "teacher": "Paulo Teixeira"},
{"day": "Friday", "hour": "9-11", "subject": "Data Storage", "class": "LESI2", "classroom": "Room E", "teacher": "Paulo Teixeira"},
{"day": "Friday", "hour": "11-13", "subject": "Data Storage", "class": "LESI2", "classroom": "Room E", "teacher": "Paulo Teixeira"},
{"day": "Friday", "hour": "14-16", "subject": "Data Storage", "class": "LESI2", "classroom": "Room E", "teacher": "Paulo Teixeira", },
{"day": "Friday", "hour": "16-18", "subject": "Data Storage", "class": "LESI2", "classroom": "Room N", "teacher": "Paulo Teixeira"},
{"day": "Friday", "hour": "18-20", "subject": "Data Storage", "class": "LESI2", "classroom": "Room N", "teacher": "Paulo Teixeira"},
{"day": "Wednesday", "hour": "9-11", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},
{"day": "Wednesday", "hour": "11-13", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},
{"day": "Wednesday", "hour": "14-16", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},
{"day": "Wednesday", "hour": "16-18", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},
{"day": "Wednesday", "hour": "18-20", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},
{"day": "Friday", "hour": "9-11", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room IOT", "teacher": "Joaquim Silva"},
{"day": "Friday", "hour": "11-13", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room IOT", "teacher": "Joaquim Silva"},
{"day": "Friday", "hour": "14-16", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},
{"day": "Friday", "hour": "16-18", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room T", "teacher": "Joaquim Silva"},
{"day": "Friday", "hour": "18-20", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room T", "teacher": "Joaquim Silva"},
{"day": "Thursday", "hour": "9-11", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room C", "teacher": "Joaquim Silva"},
{"day": "Thursday", "hour": "11-13", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room C", "teacher": "Joaquim Silva"},
{"day": "Thursday", "hour": "14-16", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room N", "teacher": "Joaquim Silva"},
{"day": "Thursday", "hour": "16-18", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room T", "teacher": "Joaquim Silva"},
{"day": "Thursday", "hour": "18-20", "subject": "Software Engineering", "class": "LESI2", "classroom": "Room T", "teacher": "Joaquim Silva"},

# ----------------------------------------------- Primeiro Ano ---------------------------------------------

{"day": "Monday", "hour": "9-11", "subject": "Calculus", "class": "LESI1", "classroom": "Room T", "teacher": "Natália Rego"},
{"day": "Monday", "hour": "11-13", "subject": "Calculus", "class": "LESI1", "classroom": "Room T", "teacher": "Natália Rego"},
{"day": "Monday", "hour": "14-16", "subject": "Calculus", "class": "LESI1", "classroom": "Room T", "teacher": "Natália Rego"},
{"day": "Monday", "hour": "16-18", "subject": "Calculus", "class": "LESI1", "classroom": "Room T", "teacher": "Natália Rego"},
{"day": "Monday", "hour": "18-20", "subject": "Calculus", "class": "LESI1", "classroom": "Room T", "teacher": "Natália Rego"},
{"day": "Tuesday", "hour": "9-11", "subject": "Calculus", "class": "LESI1", "classroom": "Room IOT", "teacher": "Natália Rego"},
{"day": "Tuesday", "hour": "11-13", "subject": "Calculus", "class": "LESI1", "classroom": "Room IOT", "teacher": "Natália Rego"},
{"day": "Tuesday", "hour": "14-16", "subject": "Calculus", "class": "LESI1", "classroom": "Room IOT", "teacher": "Natália Rego"},
{"day": "Tuesday", "hour": "16-18", "subject": "Calculus", "class": "LESI1", "classroom": "Room N", "teacher": "Natália Rego"},
{"day": "Tuesday", "hour": "18-20", "subject": "Calculus", "class": "LESI1", "classroom": "Room N", "teacher": "Natália Rego"},
{"day": "Thursday", "hour": "9-11", "subject": "Calculus", "class": "LESI1", "classroom": "Room N", "teacher": "Natália Rego"},
{"day": "Thursday", "hour": "11-13", "subject": "Calculus", "class": "LESI1", "classroom": "Room C", "teacher": "Natália Rego"},
{"day": "Thursday", "hour": "14-16", "subject": "Calculus", "class": "LESI1", "classroom": "Room E", "teacher": "Natália Rego"},
{"day": "Thursday", "hour": "16-18", "subject": "Calculus", "class": "LESI1", "classroom": "Room E", "teacher": "Natália Rego"},
{"day": "Thursday", "hour": "18-20", "subject": "Calculus", "class": "LESI1", "classroom": "Room E", "teacher": "Natália Rego"},
{"day": "Tuesday", "hour": "9-11", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room C", "teacher": "Teresa Abreu"},
{"day": "Tuesday", "hour": "11-13", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room C", "teacher": "Teresa Abreu"},
{"day": "Tuesday", "hour": "14-16", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room N", "teacher": "Teresa Abreu"},
{"day": "Tuesday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room N", "teacher": "Teresa Abreu"},
{"day": "Tuesday", "hour": "18-20", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room C", "teacher": "Teresa Abreu"},
{"day": "Wednesday", "hour": "9-11", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room E", "teacher": "Teresa Abreu"},
{"day": "Wednesday", "hour": "11-13", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room E", "teacher": "Teresa Abreu"},
{"day": "Wednesday", "hour": "14-16", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room E", "teacher": "Teresa Abreu"},
{"day": "Wednesday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room N", "teacher": "Teresa Abreu"},
{"day": "Wednesday", "hour": "18-20", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room T", "teacher": "Teresa Abreu"},
{"day": "Thursday", "hour": "9-11", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room N", "teacher": "Teresa Abreu"},
{"day": "Thursday", "hour": "11-13", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room N", "teacher": "Teresa Abreu"},
{"day": "Thursday", "hour": "14-16", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room N", "teacher": "Teresa Abreu"},
{"day": "Thursday", "hour": "16-18", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room E", "teacher": "Teresa Abreu"},
{"day": "Thursday", "hour": "18-20", "subject": "Discrete Maths", "class": "LESI1", "classroom": "Room T", "teacher": "Teresa Abreu"},
{"day": "Tuesday", "hour": "9-11", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room C", "teacher": "Nuno Rodrigues"},
{"day": "Tuesday", "hour": "11-13", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room E", "teacher": "Nuno Rodrigues"},
{"day": "Tuesday", "hour": "14-16", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room E", "teacher": "Nuno Rodrigues"},
{"day": "Tuesday", "hour": "16-18", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room T", "teacher": "Nuno Rodrigues"},
{"day": "Tuesday", "hour": "18-20", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room N", "teacher": "Nuno Rodrigues"},
{"day": "Monday", "hour": "9-11", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room Networking", "teacher": "Nuno Rodrigues"},
{"day": "Monday", "hour": "11-13", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room Networking", "teacher": "Nuno Rodrigues"},
{"day": "Monday", "hour": "14-16", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room Networking", "teacher": "Nuno Rodrigues"},
{"day": "Monday", "hour": "16-18", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room Networking", "teacher": "Nuno Rodrigues"},
{"day": "Monday", "hour": "18-20", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room Networking", "teacher": "Nuno Rodrigues"},
{"day": "Friday", "hour": "9-11", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room T", "teacher": "Nuno Rodrigues"},
{"day": "Friday", "hour": "11-13", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room C", "teacher": "Nuno Rodrigues"},
{"day": "Friday", "hour": "14-16", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room T", "teacher": "Nuno Rodrigues"},
{"day": "Friday", "hour": "16-18", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room C", "teacher": "Nuno Rodrigues"},
{"day": "Friday", "hour": "18-20", "subject": "Informatics Labs", "class": "LESI1", "classroom": "Room T", "teacher": "Nuno Rodrigues"},
{"day": "Monday", "hour": "9-11", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room E", "teacher": "Óscar Ribeiro"},
{"day": "Monday", "hour": "11-13", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room E", "teacher": "Óscar Ribeiro"},
{"day": "Monday", "hour": "14-16", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room C", "teacher": "Óscar Ribeiro"},
{"day": "Monday", "hour": "16-18", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room T", "teacher": "Óscar Ribeiro"},
{"day": "Monday", "hour": "18-20", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room T", "teacher": "Óscar Ribeiro"},
{"day": "Tuesday", "hour": "9-11", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room IOT", "teacher": "Óscar Ribeiro"},
{"day": "Tuesday", "hour": "11-13", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room IOT", "teacher": "Óscar Ribeiro"},
{"day": "Tuesday", "hour": "14-16", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room T", "teacher": "Óscar Ribeiro"},
{"day": "Tuesday", "hour": "16-18", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room IOT", "teacher": "Óscar Ribeiro"},
{"day": "Tuesday", "hour": "18-20", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room C", "teacher": "Óscar Ribeiro"},
{"day": "Thursday", "hour": "9-11", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room E", "teacher": "Óscar Ribeiro"},
{"day": "Thursday", "hour": "11-13", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room E", "teacher": "Óscar Ribeiro"},
{"day": "Thursday", "hour": "14-16", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room E", "teacher": "Óscar Ribeiro"},
{"day": "Thursday", "hour": "16-18", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room N", "teacher": "Óscar Ribeiro"},
{"day": "Thursday", "hour": "18-20", "subject": "Imperative Programming", "class": "LESI1", "classroom": "Room N", "teacher": "Óscar Ribeiro"},
{"day": "Monday", "hour": "9-11", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Monday", "hour": "11-13", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Monday", "hour": "14-16", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Monday", "hour": "16-18", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Monday", "hour": "18-20", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Friday", "hour": "9-11", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Friday", "hour": "11-13", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Friday", "hour": "14-16", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Friday", "hour": "16-18", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Friday", "hour": "18-20", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Thursday", "hour": "9-11", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Thursday", "hour": "11-13", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Thursday", "hour": "14-16", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Thursday", "hour": "16-18", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"},
{"day": "Thursday", "hour": "18-20", "subject": "Computers Architecture", "class": "LESI1", "classroom": "Room Electronics", "teacher": "Sandro Carvalho"}
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
