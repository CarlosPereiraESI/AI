from Subject import Subject
from Teacher import Teacher
from Teach import teach
from Form import form
from Classroom import classroom
from Heuristics import heuristic, schedule
import time
from AStar import astar
import numpy as np

PA=Subject(Subject_name="Projeto Aplicado",id=1, period_number=2, specialty_required=True)
ISI=Subject(Subject_name="Integração de Sistemas de Informação",id=2, period_number=2, specialty_required=True)

IA=Subject(Subject_name="Inteligência Artificial",id=3, period_number=2, specialty_required=True)
SETR=Subject(Subject_name="Sistemas Embebidos e de Tempo Real",id=4, period_number=2, specialty_required=True)
PDM=Subject(Subject_name="Programação de Dispositivos Móveis",id=5, period_number=2, specialty_required=True)
AMS=Subject(Subject_name="Análise e Modelação de Software",id=6, period_number=2, specialty_required=True)

AAD=Subject(Subject_name="Armazenamento e Acesso a Dados",id=7, period_number=2, specialty_required=True)
POO=Subject(Subject_name="Programação Orientada a Objetos",id=8, period_number=2, specialty_required=True)
PES=Subject(Subject_name="Projeto de Engenharia de Software",id=9, period_number=2, specialty_required=True)

FF=Subject(Subject_name="Fundamentos de Física",id=10, period_number=2, specialty_required=True)
PI=Subject(Subject_name="Programação Imperativa",id=11, period_number=2, specialty_required=True)
LI=Subject(Subject_name="Laboratórios de Informática",id=12, period_number=2, specialty_required=True)
CAL=Subject(Subject_name="Cálculo",id=13, period_number=2, specialty_required=True)
AL=Subject(Subject_name="Álgebra Linear",id=14, period_number=2, specialty_required=True)

RC=Subject(Subject_name="Redes de Computadores",id=15, period_number=2, specialty_required=True)

First_year=[PI,LI,CAL,AL,RC]
Second_year=[AMS,AAD,POO,PES,FF]
Third_year=[PA,ISI,IA,SETR,PDM]

Form_1=form(Recess_period=1,max_sub_pd=2,period_num=[5,5,5,5,5])
Form_2=form(Recess_period=1,max_sub_pd=2,period_num=[5,5,5,5,5])
Form_3=form(Recess_period=1,max_sub_pd=2,period_num=[5,5,5,5,5])


Form_1.add_subject(First_year)
Form_2.add_subject(Second_year)
Form_3.add_subject(Third_year)


LESI1=classroom(Form_1,class_name="1A1S")
LESI2=classroom(Form_2,class_name="2A1S")
LESI3=classroom(Form_3,class_name="3A1S")

PA_teacher_A=Teacher(subject=PA,subject_name="Projeto Aplicado",teacher_name="Patrícia Leite")

ISI_teacher_A=Teacher(subject=ISI,subject_name="Integração de Sistemas de Informação",teacher_name="Luís Ferreira")
ISI_teacher_B=Teacher(subject=ISI,subject_name="Integração de Sistemas de Informação",teacher_name="Óscar Ribeiro")

IA_teacher_A=Teacher(subject=IA,subject_name="Inteligência Artificial",teacher_name="Joaquim Gonçalves")

SETR_teacher_A=Teacher(subject=SETR,subject_name="Sistemas Embebidos e de Tempo Real",teacher_name="Paulo Macedo")

PDM_teacher_A=Teacher(subject=PDM,subject_name="Programação de Dispositivos Móveis",teacher_name="Nuno Mendes")
AMS_teacher_A=Teacher(subject=AMS,subject_name="Análise e Modelação de Software", teacher_name="Joaquim Silva")

AAD_teacher_A=Teacher(subject=AAD,subject_name="Armazenamento e Acesso a Dados",teacher_name="Paulo Teixeira")
AAD_teacher_B=Teacher(subject=AAD,subject_name="Armazenamento e Acesso a Dados",teacher_name="Joaquim Gonçalves")

POO_techer_A=Teacher(subject=POO,subject_name="Programação Orientada a Objetos",teacher_name="Luís Ferreira")

PES_teacher_A=Teacher(subject=PES,subject_name="Projeto de Engenharia de Software",teacher_name="Manuela Cunha")

FF_teacher_A=Teacher(subject=FF,subject_name="Fundamentos de Física",teacher_name="Daniel Miranda")

PI_teacher_A=Teacher(subject=PI,subject_name="Programação Imperativa",teacher_name="Nuno Rodrigues")

LI_teacher_A=Teacher(subject=LI,subject_name="Laboratórios de Informática",teacher_name="Óscar Ribeiro")

CAL_teacher_A=Teacher(subject=CAL,subject_name="Cálculo",teacher_name="Natália Rego")

AL_teacher_A=Teacher(subject=AL,subject_name="Álgebra Linear",teacher_name="Teresa Abreu")

RC_teacher_A=Teacher(subject=RC,subject_name="Redes de Computadores",teacher_name="Paulo Macedo")

heauristic_instance=heuristic(class_instances=classroom.instances,subject_instances=Subject.instances,
teacher_instances=Teacher.instances,teach_instances=teach.instance)
heauristic_instance.teacher_sufficient()

time0=time.perf_counter()
heauristic_instance.teacher_assignment()
heauristic_instance.print_teacher_assigned()
heauristic_instance.random_sort()
time1=time.perf_counter()

print("1 - Projeto Aplicado ")
print("2 - Integração de Sistemas de Informação")
print("3 - Inteligência Artifical ")
print("4 - Sistemas Embebidos em Tempo Real ")
print("5 - Programação de Dispositivos Moveis ")
print("6 - Análise e Modelação de Software ")
print("7 - Armazenamento e Acesso a Dados ")
print("8 - Programação Orientada a Objetos ")
print("9 - Projeto de Engenharia de Software ")
print("10 - Fundamentos de Física ")
print("11 - Programação Imperativa ")
print("12 - Laboratórios de Informática ")
print("13 - Cálculo")
print("14 - Álgebra Linear ")
print("15 -Redes de Computadores \n")

heauristic_instance.print_schedule()

arr = np.reshape(schedule, (15, 5))       
start = arr
end = [[11,13,-1,0,0],
    [14,12,-1,0,0],
    [13,15,-1,0,0],
    [12,14,-1,0,0],
    [11,15,-1,0,0],
    [6,8,-1,0,0],
    [9,7,-1,0,0],
    [10,6,-1,0,0],
    [7,9,-1,0,0],
    [8,10,-1,0,0],
    [3,2,-1,0,0],
    [5,1,-1,0,0],
    [4,5,-1,0,0],
    [2,1,-1,0,0],
    [4,3,-1,0,0]]

path = astar(arr, start, end)
print(path)
print("The heuristic sort take {} seconds".format(time1-time0))

