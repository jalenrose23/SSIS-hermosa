# SSIS
# Jalen Rose Hermosa

import csv

STD_attributes = ['Name', 'ID Number', 'Year Level', 'Gender', 'Course']
StudentInformation = 'Studentinfo.csv'

def Main():
    print("--------------------------------------------")
    print("    MSU-IIT STUDENT INFORMATION SYSTEM      ")
    print("--------------------------------------------")
    print("a. ADD A STUDENT")
    print("b. DISPLAY STUDENTS")
    print("c. SEARCH STUDENT")
    print("d. EDIT STUDENT INFORMATION")
    print("e. DELETE STUDENT")
    print("f. EXIT")
    print()

def AddStudent():
    print("---------------------")
    print("    ADD A STUDENT      ")
    print("---------------------")
    
    global STD_attributes 
    global StudentInformation
    
    STD_data = []
    for F in STD_attributes :
        value = input("Enter " + F + ": ")
        STD_data.append(value)
        
    with open(StudentInformation , "a", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([STD_data])
    
    print("Data added successfully!")
    input("Press any key to continue:")
    return

def ViewStudent():
    global STD_attributes 
    global StudentInformation 
    
    print("----------------------")
    print("     STUDENT LIST     ")
    print("----------------------")
    
    with open(StudentInformation , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for j in STD_attributes :
            print( j, end = "\n")
        print("\n-------------------------------------------------")
        
        for row in reader:
            for i in row:
                print( i, end = "\n")
            print()        
    input("Press any key to continue:")

    
def SearchStudent():
    global STD_attributes 
    global StudentInformation 
    
    print("------------------------")
    print("     SEARCH A STUDENT     ")
    print("------------------------")
    
    STD_ID = input("Enter ID Number:")
    with open(StudentInformation , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) > 0:
                if STD_ID == r[1]:
                    print("You found it!")
                    print("Name: ", r[0])
                    print("ID Number: ", r[1])
                    print("Year Level: ", r[2])
                    print("Gender: ", r[3])
                    print("Course: ", r[4])
                    break
        
        else:
            print(" Student not found!")
    input("Press any key to continue:")


# Changing Student's Informations
def EditStudent():
    global STD_attributes 
    global StudentInformation
    
    print("------------------------")
    print("     UPDATE STUDENT INFORMATION     ")
    print("------------------------")
    
    STD_ID = input("Enter ID Number of student you want to change: ")
    Std_index = None
    Edit_data = []
    with open(StudentInformation , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if STD_ID == row[1]:
                    Std_index = counter
                    print("Student Found: at index ", Std_index)
                    STD_data = []
                    for field in STD_attributes :
                        value = input("Enter " + field + ": ")
                        STD_data.append(value)
                    Edit_data.append(STD_data)
                else:
                    Edit_data.append(row)
                counter += 1
                
#To check if Student Records exists
    if Std_index is not None:
        with open(StudentInformation , "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(Edit_data)
    
    else:
        print("ID Number could not be found\n")
        
    input("Press any key to continue:")
    
def DeleteStudent():
    global STD_attributes 
    global StudentInformation
    
    print("------------------------")
    print("      DELETE A STUDENT    ")
    print("------------------------")
    
    STD_ID = input("Enter ID Number of student you want to remove: ")
    Std_Found = False
    Edit_data = []
    with open(StudentInformation , "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if STD_ID != row[1]:
                    Edit_data.append(row)
                    counter += 1
                else:
                    Std_Found = True
    
    if Std_Found is True:
        with open(StudentInformation , "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(Edit_data)
        print("ID Number:\n ", STD_ID, "Removed successfully!")
    
    else:
        print("ID Number not found")
    
    input("Press any key to continue:")


# Main
while True:
    Main()
    
    choice = input("Please Enter a Number:")
    if choice == 'a':
        AddStudent()
    elif choice == 'b':
        ViewStudent()
    elif choice == 'c':
        SearchStudent()
    elif choice == 'd':
        EditStudent()
    elif choice == 'e':
        DeleteStudent()
    else:
        break


# Termination
print("********************************************************************")
print("*  THE SYSTEM HAS BEEN TERMINATED,THANK YOU FOR USING THE SYSTEM!  *")
print("********************************************************************")



