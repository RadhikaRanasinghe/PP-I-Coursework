#Initializing variables
student_count = 0
progress_count = 0
trailing_count = 0
retriver_count = 0
excluded_count = 0
passed_credits = 0
deferred_credits = 0
failed_credits = 0
values_approved = None


#Unicode characters for creation of the table
top_left_corner = "\u2554"
top_right_corner = "\u2557"
horizontal = "\u2550"
vertical = "\u2551"
bottom_left_corner = "\u255A"
bottom_right_corner = "\u255D"
right_junction = "\u2563"
left_junction = "\u2560"

print(top_left_corner+horizontal*100+top_right_corner)
print(vertical+"     P R O G R E S S I O N   O U T C O M E S  :  S T A F F  V E R S I O N   ( V E R T I C A L )     "+vertical)
print(bottom_left_corner+horizontal*100+bottom_right_corner)
print()

def passed_credits_check():
    global passed_credits,total_credits
    passed_credits = int(input("Enter the number of credits student has passed (Including condoned passes)\t:"))
    while passed_credits % 20 != 0: #Checking if the values entered are divisible by 20 if not user has to input again
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
    total_credits = (passed_credits + deferred_credits)
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
            student_count +=1
        else:
            values_approved = False
            deferred_credits_check()
            if total_credits == 120:
                values_approved = True#If both of the conditions are true, values are approved for processing
                student_count +=1
            else:
                values_approved = False 
                failed_credits_check()        
                if total_credits == 120:
                    values_approved = True#If both of the conditions are true, values are approved for processing
                    student_count +=1
                else:#Total of 120 condition has become false
                    values_approved = False
                    print("Total Error! Please enter correct credits values which sums upto 120.")#Total of 120 condition has become false
                    print()
                    user_inputs()#Calling for correct user inputs
    total_credits = 0
    return passed_credits,deferred_credits,failed_credits,values_approved,student_count,total_credits

def add_or_exit_menu():#Giving user the option of choosing to add another student's records or choosing to display the histogram
    global keypress,student_count,passed_credits,deferred_credits,failed_credits
    while keypress == "N" or keypress == "n": #Since its case sensitive, both 'N' and 'n' are considered
        #add another student's data
        user_inputs()
        progress_outcome()
    else:
        if keypress == "Q" or keypress == "q":#Since its case sensitive, both 'Q' and 'q' are considered
            printing_histogram()
        else:
            print("Try again! Invalid Selection") #If neither 'Q' nor 'N' was selected, user has to input again
            keypress = str(input("Enter 'Q' to quit or 'N' to add another student\t\t\t\t\t:"))
            add_or_exit_menu()

def progress_outcome():#Student's progress outcome prediction is printed on the console
    global progress_count,trailing_count,retriver_count,excluded_count,keypress,student_count
    if passed_credits == 120: #Students who has passed all credits will progress
        print("\t\tProgression outcome of student",student_count,":\tP R O G R E S S ")
        print()
        progress_count +=1
    elif passed_credits == 100: #students who has only 100 credits with deferred or failed 20 credits will have a trailing module
        print("\t\tProgression outcome of student",student_count,":\tP R O G R E S S  -  M O D U L E  T R A I L E R ")
        print()
        trailing_count += 1
    elif passed_credits <= 80 and (failed_credits < 80 or deferred_credits >=40):#students who has less than or equal to 80 passed credits with less than 80 failed credits will not progress
        print("\t\tProgression outcome of student",student_count,":\tP R O G R E S S  -  M O D U L E  R E T R I E V E R")
        print()
        retriver_count += 1
    elif (failed_credits >= 80 or deferred_credits < 40):#Students who has 80 or more failed credits will be excluded
        print("\t\tProgression outcome of student",student_count,":\tE X C L U D E ")
        print()
        excluded_count +=1
    print()
    keypress = str(input("Enter 'Q' to quit or 'N' to add another student\t\t\t\t\t:"))
    return progress_count, retriver_count, excluded_count, keypress

def printing_histogram():#Printing the vertical histogram with a border
    global progress_count,trailing_count,retriver_count,excluded_count,student_count
    print(top_left_corner+horizontal*100+top_right_corner)
    print(vertical+"                                V E R T I C A L   H I S T O G R A M                                 "+vertical)
    print(left_junction+horizontal*100+right_junction)
    print(vertical+f'{vertical:>101}')
    print(vertical+"        Progress        ","        Trailing        ","        Retriever       ","        Excluded        ",vertical)
    print(vertical+" "*100+vertical)
    while progress_count!=0 or trailing_count !=0 or retriver_count !=0 or excluded_count !=0:
        if progress_count > 0:
            print(vertical+"           *    ",end="\t")
            progress_count -=1
        else:
            print(vertical+"                ",end="\t")
        if trailing_count > 0:
            print("             *    ",end="\t")
            trailing_count -=1
        else:
            print("                 ",end="\t")
        if retriver_count > 0:
            print("\t       *        ",end="\t")
            retriver_count -=1
        else:
            print("\t                ",end="\t")
        if excluded_count > 0:
            print("       *            ",vertical,end="\n")
            excluded_count -=1
        else:
            print("                    ",vertical,end="\n")
    print(vertical+" "*100+vertical)
    print(left_junction+horizontal*100+right_junction)
    print(vertical+"Total number of outcomes:",f'{student_count:02}',f'{vertical:>72}')
    print(bottom_left_corner+horizontal*100+bottom_right_corner)

#MAIN PROGRAM
def main_program():
    try:
        user_inputs()
        if values_approved == True:
            progress_outcome() 
            add_or_exit_menu()
    except: 
        print()
        print("Integers Required!")
        print()
        main_program()

main_program()