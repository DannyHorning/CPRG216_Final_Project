from project_doctor import Doctor
class DoctorManager:

    def __init__(self):
        self.doctor_list = []
        self.read_doctors_file()
    
    def format_dr_info(self,doctor_object):
        return f"{doctor_object.get_doctor_id()}_{doctor_object.get_name()}_{doctor_object.get_specialization()}_{doctor_object. get_working_time()}_{doctor_object.get_qualification()}_{doctor_object.get_room_number()}"
    
    def enter_dr_info(self):
        id = (input("Enter the doctor's ID: "))
        name = (input("Enter the doctor's name: "))
        specialization = (input("Enter the doctor's specility: "))
        timimg = (input("Enter the doctor's timing (e.g., 7am-10pm): "))
        qualification = (input("Enter doctor's qualification: "))
        roomNb = (input("Enter doctor's room number: "))
        new_object = Doctor(id,name,specialization,timimg,qualification,roomNb)
        self.add_dr_to_file(self.format_dr_info(new_object),id)

    
    def read_doctors_file(self): 
        f = open("doctors.txt","r")
        for i in f:
            data = i.strip().split("_")
            doctor = Doctor(data[0],data[1],data[2],data[3],data[4],data[5]) 
            self.doctor_list.append(doctor) 

    def search_doctor_by_id(self,id =0):
        display_id = 0
        if id == 0:
            display_id = str(input("Enter doctor id: "))
        for i in self.doctor_list: 
            if i.get_doctor_id() == id: 
                return i
            elif i.get_doctor_id() == display_id:
                self.display_doctor_info(self.doctor_list[0])
                return self.display_doctor_info(i)
        print("Can't find the doctor with the same ID on the system.\n")

    def search_doctor_by_name(self):
        name = (input("Enter doctor name:"))
        for i in self.doctor_list:
            if i.get_name() == name:
                return self.display_doctor_info(i)
                print(i)
        print("Can't find the doctor with the same name on the system\n")
                
    def display_doctor_info(self,information):
      print(f"{information.get_doctor_id():<20} {information.get_name():<20} {information.get_specialization():<20} {information.get_working_time():<20} {information.get_qualification():<20} {information.get_room_number():<20}")   
    
    def edit_doctor_info(self):
        id_edit = input("Please enter the id of the doctor that you want to edit their information: ")
        doctor_memory = self.search_doctor_by_id(id_edit)
        doctor_memory.set_name(input("Enter new Name: "))
        doctor_memory.set_specialization(input("Enter new Specilist in: "))
        doctor_memory.set_working_time(input("Enter new Timing: "))
        doctor_memory.set_qualification(input("Enter new Qualification: "))
        doctor_memory.set_room_number(input("Enter new Room number: "))
        self.Write_list_of_doctors_to_file(id_edit,self.format_dr_info(doctor_memory))
        print(f"\nDoctor whose ID is {id_edit} has been edited\n")
    
    def display_doctor_list(self):
        for i in self.doctor_list:
            self.display_doctor_info(i)
    
    def Write_list_of_doctors_to_file(self, id_edit, edit_information):
        with open("doctors.txt", "r") as f:
            lines = f.readlines()

        with open("doctors.txt", "w") as f:
            for line in lines:
                if line.startswith(str(id_edit)):
                    f.write(edit_information + "\n")
                else:
                    f.write(line)

    
    def add_dr_to_file(self,new_doctor,doctor_id):
        f = open("doctors.txt", "a")
        f.write(f"\n{new_doctor}")
        f.close()
        print(f"Doctor whose ID is {doctor_id} has been added\n")
        self.read_doctors_file()
    
    