#Daniel Ortega Rubio
#My code takes the data from the file and asks the user to input the state, disease and year they would like to inquire.
#I then make a couple of if statements to check conditions in case the user leave a blank entry.
#I also added an extra feature that will print out the highest and lowest number of cases depending on what info the user inputs

#ANSWERS TO QUESTIONS
#1) 59
#2) 47,743
#3) 631,797

#i only made the main function because i felt it was not necessary to make multiple functions
def main():
    file = open("health-no-head.csv", "r")

    total = 0
    comma_total = 0
    high = 0
    low = float('inf')

    state_input = input("Enter state: ").upper()
    disease_input = input("Enter disease: ").upper()
    year_input = input("Enter year: ")
        
    print("State               ", "Disease ", "       Number", "   Year")
    
    data = file.readline()
    
    #used a while loop in order to read each line in order
    #i then split then sliced each piece of relevant information and assigned it to a variable
    while data:
        values = data.split(',')    
        disease = values[0]
        state = values[2]
        number = values[3]
        year = values[5].strip()
        
        num = int(number)
        comma_num = "{:,}".format(num)
        
        #Here are the if statements. each one checks the conditions in case the user leaves an entry blank
        #this eventually prints out a formatted table 
        if state_input == state:
            if year_input == '' or year_input == year:
                if disease_input == '' or disease_input == disease:
                    total += num
                    info = "{:<20} {:<11} {:>10} {:>7}".format(state, disease, comma_num, year)
                    print(info)
                    #the following is the code that checks for the highest and lowest number of cases
                    number = int(number)
                    if high < number:
                        high = number
                    if low > number:
                        low = number
                
        elif year_input == year:
            if disease_input == '' or disease_input == disease:
                if state_input == '' or state_input == state:
                    total += num
                    info = "{:<20} {:<11} {:>10} {:>7}".format(state, disease, comma_num, year)
                    print(info)
                    number = int(number)
                    if high < number:
                        high = number
                    if low > number:
                        low = number
            
        elif disease_input == disease:
            if state_input == '' or state_input == state:
                if year_input == '' or year_input == year:
                    total += num
                    info = "{:<20} {:<11} {:>10} {:>7}".format(state, disease, comma_num, year)
                    print(info)
                    number = int(number)
                    if high < number:
                        high = number
                    if low > number:
                        low = number

        data = file.readline()
    
    #Here I made sure that any thousand number will have a comma
    comma_total = "{:,}".format(total)
    
    #finally we print the total by formatting it the same as our output
    print("{:<20} {:<11} {:>{}}".format(" ", "Total:", comma_total, 10))
    
    comma_high = "{:,}".format(high)
    comma_low = "{:,}".format(low)
    
    #Here is the printed highest and lowest numbers for the cases
    print(" ")
    print("The largest number of cases is:  ", comma_high)
    print("the smallest number of cases is: ", comma_low)
    
    file.close()
    
main()