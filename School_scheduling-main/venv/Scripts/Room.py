class Subject():
    instances = []
    def __init__(self,Room_name, specialty_required=False):
        self.__class__.instances.append(self)
        self.room_name=Room_name
        self.specialty=specialty_required
        
    def __hash__(self):
        return hash((self.subject_name))

    def __eq__(self, other):
        return (self.room_name) == (other.room_name)