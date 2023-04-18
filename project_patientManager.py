from project_patient import Patient


class PatientManager:
    def __init__(self):
        self.patient_list = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self,object):
        return f"{object.get_pid()}_{object.get_name()}_{object.get_disease()}_{object.get_gender()}_{object.get_age()}"
    
    def enter_patient_info(self):
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        objects = Patient(pid,name,disease,gender,age)
        print(f"Patient whose ID is {pid} has been added.\n")
        return self.add_patient_to_file(objects)

    def read_patients_file(self):
        f = open("patients.txt","r")
        for i in f:
            data = i.strip().split("_")
            patient = Patient(data[0],data[1],data[2],data[3],data[4])
            self.patient_list.append(patient)

    def search_patient_by_id(self,id = 0): # if id is 0 then it will call the display_patient_info fiction. if id is not 0 then it will return the object
        display_id = 0
        if id == 0:
            display_id = input("Enter Patient Id: ")
        for i in self.patient_list:
            if i.get_pid() == id:
                return i
            elif i.get_pid() == display_id:
                self.display_patient_info(self.patient_list[0])
                return self.display_patient_info(i)
        print("Can't find the Patient with the same id on the system\n")
    
    def display_patient_info(self,object):
        print(f"{object.get_pid():<20} {object.get_name():<20} {object.get_disease():<20} {object.get_age():<20}")
        pass

    def edit_patient_info_by_id(self):
        edit_id = input("Please enter the id of the Patient that you want to edit their information: ")
        patient_object = self.search_patient_by_id(edit_id)
        patient_object.set_name(input("Enter new Name: "))
        patient_object.set_disease(input("Enter new disease: "))
        patient_object.set_gender(input("Enter new gender: "))
        patient_object.set_age(input("Enter new age: "))
        print(f"Patient whose ID is {edit_id} has been edited.")
        self.write_list_of_patients_to_file(edit_id,patient_object)


    def display_patients_list(self):
        for i in self.patient_list:
            self.display_patient_info(i)

    def write_list_of_patients_to_file(self,id,object):
        format_object = self.format_patient_info_for_file(object)
        with open("patients.txt", "r") as f:
            lines = f.readlines()

        with open("patients.txt", "w") as f:
            for line in lines:
                if line.startswith(str(id)):
                    f.write(format_object + "\n")
                else:
                    f.write(line)

    def add_patient_to_file(self,object):
        format_object = self.format_patient_info_for_file(object)
        f = open("patients.txt", "a")
        f.write(f"\n{format_object}")
        f.close()
        self.read_patients_file()
