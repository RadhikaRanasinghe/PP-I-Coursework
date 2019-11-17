#Initializing variables
student_count = 0
progress_count = 0
trailing_count = 0
retriver_count = 0
excluded_count = 0
passed_credits = 0
deferred_credits = 0
failed_credits = 0
values_approved = False


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

def user_inputs():#Functions to take inputs and count the number of students' credits are entered
    global student_count,passed_credits,deferred_credits,failed_credits,values_approved
    #All three credits category inputs are taken from the user
    passed_credits = int(input("Enter the number of credits student has passed (Including condoned passes)\t:"))
    deferred_credits = int(input("Enter the number of credits student has defered\t\t\t\t\t:"))
    failed_credits = int(input("Enter the number of credits student has failed\t\t\t\t\t:"))
    print()
    print()
    total_credits = (passed_credits + deferred_credits + failed_credits)
    if total_credits ==120: #Checking if the total of the scores entered are equal to 120 if not user has to input again
        if passed_credits % 20 == 0 and deferred_credits % 20 == 0 and failed_credits % 20 == 0:
            #Checking if the values entered are divisible by 20 if not user has to input again
            values_approved = True #If both of the conditions are true, values are approved for processing
            student_count += 1
        else: 
            print("Range Error! Please enter correct credits values.")#Divisible by 20 condition has become false
            print()
            user_inputs()
    else:
        print("Total Error! Please enter correct credits values which sums upto 120.")#Total of 120 condition has become false
        print()
        user_inputs()
    return student_count,passed_credits,deferred_credits,failed_credits,values_approved

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
        print("\t\tProgression outcome of student",student_count,":\tProgress")
        print()
        progress_count +=1
    elif passed_credits == 100: #students who has only 100 credits with deferred or failed 20 credits will have a trailing module
        print("\t\tProgression outcome of student",student_count,":\tProgress- Module trailer")
        print()
        trailing_count += 1
    elif passed_credits <= 80 and failed_credits < 80:#students who has less than or equal to 80 passed credits with less than 80 failed credits will not progress
        print("\t\tProgression outcome of student",student_count,":\tDo not Progress- Module Retriever")
        print()
        retriver_count += 1
    elif failed_credits >= 80:#Students who has 80 or more failed credits will be excluded
        print("\t\tProgression outcome of student",student_count,":\tExclude")
        print()
        excluded_count +=1
    print()
    keypress = str(input("Enter 'Q' to quit or 'N' to add another student\t\t\t\t\t:"))#User input for adding another student/Histogram
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