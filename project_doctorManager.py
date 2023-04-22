from project_doctor import Doctor
class DoctorManager:

    def __init__(self):
        self.doctor_list = []
        self.read_doctors_file()
    
    def format_dr_info(self,doctor_object): # Function it is going to take a object and format it the same way it is in doctor.txt file
        return f"{doctor_object.get_doctor_id()}_{doctor_object.get_name()}_{doctor_object.get_specialization()}_{doctor_object. get_working_time()}_{doctor_object.get_qualification()}_{doctor_object.get_room_number()}"
    
    def enter_dr_info(self): # This function is basically when a user want to add a new doctor to the file. this will ask all the doctor information 
        id = (input("Enter the doctor's ID: "))
        name = (input("Enter the doctor's name: "))
        specialization = (input("Enter the doctor's specility: "))
        timimg = (input("Enter the doctor's timing (e.g., 7am-10pm): "))
        qualification = (input("Enter doctor's qualification: "))
        roomNb = (input("Enter doctor's room number: "))
        new_object = Doctor(id,name,specialization,timimg,qualification,roomNb) # Then create an object with that information
        self.add_dr_to_file(self.format_dr_info(new_object),id) # then formet that object by calling( format_dr_info) then send that formeted information to (add_dr_to_file)

    
    def read_doctors_file(self):  # this function just simple read the doctors.txt file and create an object regarding to it and store it in doctor_list.
        f = open("doctors.txt","r")
        self.doctor_list = []
        for i in f:
            data = i.strip().split("_") # in each line word is seprated by _ and stored in an array.
            doctor = Doctor(data[0],data[1],data[2],data[3],data[4],data[5]) 
            self.doctor_list.append(doctor) 

    def search_doctor_by_id(self,id =0):# this function search doctor by id but it has a option to take a perimeter, if perimeter of (id) is send then this function return the object which contains that id, else if no perimeter is sent then this function will ask user for an id then call the funtion to PRINT that doctor information.
        display_id = 0 # if this variable has an value then this function will call the function display_doctor_info which will print the doctor information.
        if id == 0:
            display_id = str(input("Enter doctor id: "))
        for i in self.doctor_list: 
            if i.get_doctor_id() == id: 
                return i
            elif i.get_doctor_id() == display_id:
                self.display_doctor_info(self.doctor_list[0])
                return self.display_doctor_info(i)
        print("Can't find the doctor with the same ID on the system.\n")

    def search_doctor_by_name(self): # this function is same as before but it doesnot take any perimeters means, it will always calls the function display_doctor_info by sending the perimeters of the object which have same name as user input. if not then it would just simple say that doctor does not exist.
        name = (input("Enter doctor name:"))
        for i in self.doctor_list:
            if i.get_name() == name:
                self.display_doctor_info(self.doctor_list[0])
                return self.display_doctor_info(i)
                print(i)
        print("Can't find the doctor with the same name on the system\n")
                
    def display_doctor_info(self,information): # this funtion take the information as a perimeter(doctor object) and format it by putting 20 space after each char (kinda like formating it as asked in instructions).
      print(f"{information.get_doctor_id():<20} {information.get_name():<20} {information.get_specialization():<20} {information.get_working_time():<20} {information.get_qualification():<20} {information.get_room_number():<20}")   
    
    def edit_doctor_info(self): # this function works to edit doctor information of the id the user inputs. 
        id_edit = input("Please enter the id of the doctor that you want to edit their information: ") # ask user docotr id
        doctor_memory = self.search_doctor_by_id(id_edit) # then search that doctor from doctor_list by calling search_doctor_by_id function
        doctor_memory.set_name(input("Enter new Name: "))
        doctor_memory.set_specialization(input("Enter new Specilist in: "))
        doctor_memory.set_working_time(input("Enter new Timing: "))
        doctor_memory.set_qualification(input("Enter new Qualification: "))
        doctor_memory.set_room_number(input("Enter new Room number: "))
        self.Write_list_of_doctors_to_file(id_edit,self.format_dr_info(doctor_memory)) # then this will send that id and that matching doctor object (after formating) to writ_list_of_doctors_to_file
        print(f"\nDoctor whose ID is {id_edit} has been edited\n")
    
    def display_doctor_list(self): # this will loop through doctor_list and send each and every object (one at a time) to display_doctor_info function
        for i in self.doctor_list:
            self.display_doctor_info(i)
    
    def Write_list_of_doctors_to_file(self, id_edit, edit_information):# this function only take the object that has been edited, it will take two perimeters id and the object. first it will read through the file(each line at a time). then it will check if that line startswith that asked id if yes, then then it will take the " edit_information" and put that in the file. if not, then it will just re-write the old line again (kinda like the line never changed).
        with open("doctors.txt", "r") as f:
            lines = f.readlines()

        with open("doctors.txt", "w") as f:
            for line in lines:
                if line.startswith(str(id_edit)):
                    f.write(edit_information + "\n")
                else:
                    f.write(line)

    
    def add_dr_to_file(self,new_doctor,doctor_id): # this function take two parimeter the new_doctor: which is the information that is going to get append in the file, the doctor_id is simply used for the print message (it server no other purpose :|).
        f = open("doctors.txt", "a")
        f.write(f"\n{new_doctor}")
        f.close()
        print(f"Doctor whose ID is {doctor_id} has been added\n")
        self.read_doctors_file() # this function is called only because i also have to update that information into the doctor_list too
    
    
