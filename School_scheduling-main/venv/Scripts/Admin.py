from Subject import Subject
from Teacher import Teacher
from Teach import teach
from Form import form
from Classroom import classroom
from Heuristics import heuristic
import time

PA=Subject(Subject_name="Projeto Aplicado",period_number=2, specialty_required=False)
ISI=Subject(Subject_name="Integração de Sistemas de Informação",period_number=2, specialty_required=False)

IA=Subject(Subject_name="Inteligência Artificial",period_number=2)
SETR=Subject(Subject_name="Sistemas Embebidos e de Tempo Real",period_number=2)
PDM=Subject(Subject_name="Programação de Dispositivos Móveis",period_number=2)
AMS=Subject(Subject_name="Análise e Modelação de Software",period_number=2)

AAD=Subject(Subject_name="Armazenamento e Acesso a Dados",period_number=2)
POO=Subject(Subject_name="Programação Orientada a Objetos",period_number=2)
PES=Subject(Subject_name="Projeto de Engenharia de Software",period_number=2)

FF=Subject(Subject_name="Fundamentos de Física",period_number=4)
PI=Subject(Subject_name="Programação Imperativa",period_number=4,side2=False)
Geografi=Subject(Subject_name="Geografi",period_number=4)
KH=Subject(Subject_name="Kemahiran Hidup",period_number=4,specialty_required=False)
Pendidikan_Seni=Subject(Subject_name="Pendidikan Seni",period_number=4,specialty_required=False)

PJK_lower=Subject(Subject_name="PJK_lower",period_number=4, specialty_required=False)
PJK_upper=Subject(Subject_name="PJK_upper",period_number=4, specialty_required=False)

Lower_form_subject=[Maths,Science,English,Malay,Chinese,Moral,Sejarah,Geografi,KH, Pendidikan_Seni,PJK_lower]
Upper_form_subject=[Maths,Add_Maths,English,Malay,Chinese,Moral,Sejarah,PJK_upper,Biology,Chemistry,Physics]

Form_1=form(Recess_period=4,max_sub_pd=2,period_num=[11,11,10,10,7])
Form_2=form(Recess_period=4,max_sub_pd=2,period_num=[11,11,10,10,7])
Form_3=form(Recess_period=4,max_sub_pd=2,period_num=[11,11,10,10,7])
Form_4=form(Recess_period=5,max_sub_pd=2,period_num=[11,11,11,11,7])
Form_5=form(Recess_period=5,max_sub_pd=2,period_num=[11,11,11,11,7])


Form_1.add_subject(Lower_form_subject)
Form_2.add_subject(Lower_form_subject)
Form_3.add_subject(Lower_form_subject)
Form_4.add_subject(Upper_form_subject)
Form_5.add_subject(Upper_form_subject)


OneA1=classroom(Form_1,class_name="1A2")
TwoA1=classroom(Form_2,class_name="2A1")
ThreeA1=classroom(Form_3,class_name="3A1")
FourS1=classroom(Form_4,class_name="4Sc1")
FiveS1=classroom(Form_5,class_name="5Sc1")


Geografi_teacher_A=Teacher(subject=Geografi,teacher_name="Geografi_teacher_A")

Sejarah_teacher_A=Teacher(subject=Sejarah,teacher_name="Sejarah_teacher_A")
Sejarah_teacher_B=Teacher(subject=Sejarah,teacher_name="Sejarah_teacher_B")

Physics_teacher_A=Teacher(subject=Physics,teacher_name="Physics_teacher_A")

Moral_teacher_A=Teacher(subject=Moral,teacher_name="Moral_teacher_A")
Moral_teacher_B=Teacher(subject=Moral,teacher_name="Moral_teacher_B")


Biology_teacher_A=Teacher(subject=Biology,teacher_name="Biology_teacher_A")
Chemistry_teacher_A=Teacher(subject=Chemistry,teacher_name="Chemistry_teacher_A")

Science_teacher_A=Teacher(subject=Science,teacher_name="Science_teacher_A")
Science_teacher_B=Teacher(subject=Science,teacher_name="Science_teacher_B")



Maths_techer_A=Teacher(subject=Maths,teacher_name="Maths_techer_A")
Maths_techer_B=Teacher(subject=Maths,teacher_name="Maths_techer_B")
Maths_techer_C=Teacher(subject=Maths,teacher_name="Maths_techer_C")



Add_maths_teacher_A=Teacher(subject=Add_Maths,teacher_name="Add_maths_teacher_A")

Chinese_teacher_A=Teacher(subject=Chinese,teacher_name="Chinese_teacher_A")
Chinese_teacher_B=Teacher(subject=Chinese,teacher_name="Chinese_teacher_B")
Chinese_teacher_C=Teacher(subject=Chinese,teacher_name="Chinese_teacher_C")


Malay_teacher_A=Teacher(subject=Malay,teacher_name="Malay_teacher_A")
Malay_teacher_B=Teacher(subject=Malay,teacher_name="Malay_teacher_B")
Malay_teacher_C=Teacher(subject=Malay,teacher_name="Malay_teacher_C")


English_teacher_A=Teacher(subject=English,teacher_name="English_teacher_A")
English_teacher_B=Teacher(subject=English,teacher_name="English_teacher_B")
English_teacher_C=Teacher(subject=English,teacher_name="English_teacher_C")


heauristic_instance=heuristic(class_instances=classroom.instances,subject_instances=Subject.instances,teacher_instances=Teacher.instances,teach_instances=teach.instance)
heauristic_instance.teacher_sufficient()

time0=time.perf_counter()
heauristic_instance.teacher_assignment()
heauristic_instance.print_teacher_assigned()
heauristic_instance.random_sort()
time1=time.perf_counter()

print("The heuristic sort take {} seconds".format(time1-time0))

heauristic_instance.print_schedule()
