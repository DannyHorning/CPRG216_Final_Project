class Doctor:

#Initialization for the Doctor Class
    def __init__(self):
        self.name = None
        self.id = None
        self.specialization = None
        self.working_time = None
        self.qualification = None
        self.room_number = None

#Getters for Doctor Class
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.room_number
        
#Setters for the Doctor Class

    def set_name(self, name):
        self.name = name
    
    def set_id(self, id):
        self.id = id

    def set_specialization(self,specialization):
        self.specialization = specialization
    
    def set_working_time(self, time):
        self.working_time = time

    def set_qualification(self, qualification):
        self.qualification = qualification
    
    def set_room_number(self, room_number):
        self.room_number = room_number

#print string for Doctor Class

    def __str__(self):
        return f'{self.id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}'
    