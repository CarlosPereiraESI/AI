

class Subject():
    instances = []
    def __init__(self,Subject_name,id,period_number,side2=False,specialty_required=False):
        self.__class__.instances.append(self)
        self.subject_name=Subject_name
        self.period_num=period_number
        self.side_by_side=side2
        self.specialty=specialty_required
        self.id = id

    def __hash__(self):
        return hash((self.subject_name,self.id, self.period_num))

    def __eq__(self, other):
        return (self.subject_name,self.id, self.period_num) == (other.subject_name,other.id, other.period_num)


