from project_doctorManager import DoctorManager
from PatientManager import PatientManager
class Management:
    def display_menu(self): # This function is going to intract with the user.
        option = int(input("\nWelcome to Alberta Hospital (AH) Managment system \nSelect from the following options, or select 3 to stop:  \n1 - Doctors \n2 - Patients \n3 - Exit Program\n"))
        while option == 1: 
            doctor_option = int(input("\nDoctors Menu: \n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor  info \n6 - Back to the Main Menu\n"))
            if doctor_option == 6:
                self.display_menu() # if the doctor_option is 6 then it will call the function again
                break # this break because this while loop will never end even the function called in line 9.
            doctor_dictinory = {1:DoctorManager().display_doctor_list, 2: DoctorManager().search_doctor_by_id,3: DoctorManager().search_doctor_by_name,4:DoctorManager().enter_dr_info,5:DoctorManager().edit_doctor_info}
            doctor_dictinory[doctor_option]() # this will just call the function accouring to the doctor_option, it will call the function by taking the value from doctor_dictinory and calling it.

        while option ==2:
            patient_option = int(input("\nPatients Menu: \n1 - Display patients list\n2 -Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n"))
            if patient_option == 5:
                self.display_menu()  # if the patient_option is 5 then it will call the function (display_menu)again
                break  # this break because this while loop will never end even the function called in line 17.
            patient_dictinory = {1:PatientManager().display_patients_list, 2: PatientManager().search_patient_by_id,3:PatientManager().enter_patient_info,4:PatientManager().edit_patient_info_by_id}
            patient_dictinory[patient_option]()# this will just call the function accouring to the patient_option, it will call the function by taking the value from patient_dictinory and calling it.
        
        if option ==3:
            print("Thanks for using the program. Bye!")

Management().display_menu()
