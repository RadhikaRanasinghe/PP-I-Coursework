#Declaring variables
passed_credits = 0
deferred_credits = 0
failed_credits = 0
total_credits = 0
values_approved = False
#comments
#Unicode characters for creation of the table
top_left_corner = "\u2554"
top_right_corner = "\u2557"
horizontal = "\u2550"
vertical = "\u2551"
bottom_left_corner = "\u255A"
bottom_right_corner = "\u255D"

print(top_left_corner+horizontal*100+top_right_corner)
print(vertical+"             P R O G R E S S I O N   O U T C O M E S  :  S T U D E N T   V E R S I O N              "+vertical)
print(bottom_left_corner+horizontal*100+bottom_right_corner)
print()

def passed_credits_check():
    global passed_credits,total_credits
    passed_credits = int(input("Enter the number of credits student has passed (Including condoned passes)\t:"))
    while passed_credits % 20 != 0:#Checking if the values entered are divisible by 20 if not user has to input again
        print()
        print("Range Error! Please enter correct passed credits values.")#Divisible by 20 condition has become false
        passed_credits = int(input("Enter the number of credits student has passed (Including condoned passes)\t:"))
    print()
    total_credits = passed_credits 
    return passed_credits, total_credits

def deferred_credits_check():
    global deferred_credits,total_credits
    deferred_credits = int(input("Enter the number of credits student has defered\t\t\t\t\t:"))
    while deferred_credits % 20 != 0:
        print()
        print("Range Error! Please enter correct deferred credits values.")#Divisible by 20 condition has become false
        deferred_credits = int(input("Enter the number of credits student has defered\t\t\t\t\t:"))
    print()
    total_credits = passed_credits + deferred_credits
    return deferred_credits, total_credits

def failed_credits_check():
    global failed_credits,total_credits
    failed_credits = int(input("Enter the number of credits student has failed\t\t\t\t\t:"))
    while failed_credits % 20 != 0:
        print()
        print("Range Error! Please enter correct failed credits values.")#Divisible by 20 condition has become false
        failed_credits = int(input("Enter the number of credits student has failed\t\t\t\t\t:"))
    print()
    total_credits = (passed_credits + deferred_credits + failed_credits)
    return failed_credits,total_credits

def user_inputs():#Functions to take inputs and count the number of students' credits are entered
    global passed_credits,deferred_credits,failed_credits,values_approved,student_count,total_credits
    total_credits = 0  
    #All three credits category inputs are taken from the user
    if total_credits != 120:
        passed_credits_check()
        if total_credits ==120:
            values_approved = True #If both of the conditions are true, values are approved for processing
        else:
            values_approved = False
            deferred_credits_check()
            if total_credits == 120:
                values_approved = True#If both of the conditions are true, values are approved for processing
            else:
                values_approved = False 
                failed_credits_check()        
                if total_credits == 120:
                    values_approved = True#If both of the conditions are true, values are approved for processing
                else:#Total of 120 condition has become false
                    values_approved = False
                    print("Total Error! Please enter correct credits values which sums upto 120.")#Total of 120 condition has become false
                    print()
                    user_inputs()#Calling for correct user inputs
    total_credits = 0
    return passed_credits,deferred_credits,failed_credits,values_approved,total_credits
    
def progress_outcome(): #Student's progress outcome prediction is printed on the console
    global passed_credits,deferred_credits,failed_credits
    print(top_left_corner+horizontal*100+top_right_corner)
    if passed_credits == 120:
        print(vertical+"                                  Progression outcome :  P R O G R E S S                           ",vertical)
    elif passed_credits == 100:
        print(vertical+"               Progression outcome :  P R O G R E S S  -  M O D U L E   T R A I L E R              ",vertical)
    elif passed_credits <= 80 and (failed_credits < 80 or deferred_credits >=40):
        print(vertical+"         Progression outcome : D O  N O T  P R O G R E S S - M O D U L E  R E T R I E V E R        ",vertical)
    elif (failed_credits >= 80 or deferred_credits < 40):
        print(vertical+"                                  Progression outcome : E X C L U D E                              ",vertical)
    print(bottom_left_corner+horizontal*100+bottom_right_corner)

#Main Program calling the user defined fucntions 
def main_program():
    try: 
        user_inputs()
        if values_approved == True:
            progress_outcome()    
    except: 
        print("Integers Required!")
        main_program()

main_program()

