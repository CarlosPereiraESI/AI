from astar import find_optimal_schedule

nodes = []

teachers = ['Patrícia Leite', 'Nuno Mendes', 'Paulo Macedo', 'Joaquim Gonçalves', 'Joaquim Silva', 'Luís Ferreira', 'Paulo Teixeira',
'Nuno Lopes', 'Nuno Rodrigues', 'Duarte Duque', 'Fernando Gomes', 'João Carlos Silva']

subjects = ['IA', 'ISI', 'PA', 'SETR', 'PDM', 'PI', 'LI', 'RC', 'CAL', 'MD', 'AMS', 'AAD', 'PES', 'PL', 'FF', 'POO']

classrooms = ['T', 'E', 'C', 'N', 'IOT', 'ELEC', 'REDES', 'IM', 'AR']

goal_teachers = ['Patricia Leite', 'Nuno Mendes', 'Paulo Macedo', 'Joaquim Gonçalves', 'Luis Ferreira']
goal_subjects = ['PA', 'PDM', 'SETR', 'IA', 'ISI']
goal_classrooms = ['T', 'E', 'C', 'N', 'IOT']

nodes = find_optimal_schedule(teachers, subjects, classrooms, goal_teachers, goal_subjects, goal_classrooms)


print(nodes)