class Doctor:
    def __init__(self,id = 0,name = None,specialization = None,working_time = 0,qualification= None,room_number = 0):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.timing = working_time
        self.qualification = qualification
        self.roomNb = room_number
    
    def get_doctor_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_specialization(self):
        return self.specialization

    def get_working_time(self):
        return self.timing 

    def get_qualification(self):
        return self.qualification

    def get_room_number(self):
        return self.roomNb
    
    def set_doctor_id(self,new_id):
        self.id = new_id

    def set_name(self,new_name):
        self.name = new_name

    def set_specialization(self,new_specialization):
        self.specialization = new_specialization

    def set_working_time(self,new_working_time):
        self.timing = new_working_time

    def set_qualification(self,new_qualification):
        self.qualification = new_qualification

    def set_room_number(self,new_room_number):
        self.roomNb = new_room_number

    def __str__(self):
        return f"{self.id}_{self.name}_{self.specialization}_{self.timing}_{self.qualification}_{self.roomNb}"