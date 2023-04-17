class Patient:
#Patient class initialization 
    def __init__(self):
        self.pid = None
        self.name = None
        self.disease = None
        self.gender = None
        self.age = None
#Patient Getters  
    def get_pid(self):
        return self.pid
    
    def get_name(self):
        return self.name
    
    def get_disease(self):
        return self.disease
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    def set_pid(self, pid):
        self.pid = pid
#Patient Setters  
    def set_name(self, name):
        self.name = name
    
    def set_disease(self, disease):
        self.disease = disease
    
    def set_gender(self, gender):
        self.gender = gender
    
    def set_age(self, age):
        self.age = age

#Patient String

    def __str__(self):
        return f'{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}'
