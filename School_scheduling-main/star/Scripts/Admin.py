from Subject import Subject
from Teacher import Teacher
from Teach import teach
from Form import form
from Classroom import classroom
from Heuristics import heuristic
import time

PA=Subject(Subject_name="Projeto Aplicado",period_number=2, specialty_required=True)
ISI=Subject(Subject_name="Integração de Sistemas de Informação",period_number=2, specialty_required=True)

IA=Subject(Subject_name="Inteligência Artificial",period_number=2, specialty_required=True)
SETR=Subject(Subject_name="Sistemas Embebidos e de Tempo Real",period_number=2, specialty_required=True)
PDM=Subject(Subject_name="Programação de Dispositivos Móveis",period_number=2, specialty_required=True)
AMS=Subject(Subject_name="Análise e Modelação de Software",period_number=2, specialty_required=True)

AAD=Subject(Subject_name="Armazenamento e Acesso a Dados",period_number=2, specialty_required=True)
POO=Subject(Subject_name="Programação Orientada a Objetos",period_number=2, specialty_required=True)
PES=Subject(Subject_name="Projeto de Engenharia de Software",period_number=2, specialty_required=True)

FF=Subject(Subject_name="Fundamentos de Física",period_number=2, specialty_required=True)
PI=Subject(Subject_name="Programação Imperativa",period_number=2, specialty_required=True)
LI=Subject(Subject_name="Laboratórios de Informática",period_number=2, specialty_required=True)
CAL=Subject(Subject_name="Cálculo",period_number=2, specialty_required=True)
AL=Subject(Subject_name="Álgebra Linear",period_number=2, specialty_required=True)

RC=Subject(Subject_name="Redes de Computadores",period_number=2, specialty_required=True)

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

PA_teacher_A=Teacher(subject=PA,teacher_name="Patrícia Leite")

ISI_teacher_A=Teacher(subject=ISI,teacher_name="Luís Ferreira")
ISI_teacher_B=Teacher(subject=ISI,teacher_name="Óscar Ribeiro")

IA_teacher_A=Teacher(subject=IA,teacher_name="Joaquim Gonçalves")

SETR_teacher_A=Teacher(subject=SETR,teacher_name="Paulo Macedo")

PDM_teacher_A=Teacher(subject=PDM,teacher_name="Nuno Mendes")
AMS_teacher_A=Teacher(subject=AMS,teacher_name="Joaquim Silva")

AAD_teacher_A=Teacher(subject=AAD,teacher_name="Paulo Teixeira")
AAD_teacher_B=Teacher(subject=AAD,teacher_name="Joaquim Gonçalves")

POO_techer_A=Teacher(subject=POO,teacher_name="Luís Ferreira")

PES_teacher_A=Teacher(subject=PES,teacher_name="Manuela Cunha")

FF_teacher_A=Teacher(subject=FF,teacher_name="Daniel Miranda")

PI_teacher_A=Teacher(subject=PI,teacher_name="Nuno Rodrigues")

LI_teacher_A=Teacher(subject=LI,teacher_name="Óscar Ribeiro")

CAL_teacher_A=Teacher(subject=CAL,teacher_name="Natália Rego")

AL_teacher_A=Teacher(subject=AL,teacher_name="Teresa Abreu")

RC_teacher_A=Teacher(subject=RC,teacher_name="Paulo Macedo")

heauristic_instance=heuristic(class_instances=classroom.instances,subject_instances=Subject.instances,
teacher_instances=Teacher.instances,teach_instances=teach.instance)
heauristic_instance.teacher_sufficient()

time0=time.perf_counter()
heauristic_instance.teacher_assignment()
heauristic_instance.print_teacher_assigned()
heauristic_instance.random_sort()
time1=time.perf_counter()

print("The heuristic sort take {} seconds".format(time1-time0))

heauristic_instance.print_schedule()
