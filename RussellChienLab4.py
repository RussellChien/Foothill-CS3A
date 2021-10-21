################################################
# Program Header                               #
# Course: CS 3A Object-Oriented Programming    #
#         Methodologies in Python              #
# Name:   Russell Chien                        #
# Description: Programming with Dictionaries   #
# Application: Spelling Digits                 #
# Date:  07/11/2019                            #
################################################

# Program Source Statements
#program constants 
Z = 'zero'
O = 'one'
T = 'two'
TH = 'three'
F = 'four'
FI = 'five'
S = 'six'
SE = 'seven'
E = 'eight'
N = 'nine'

#digit dictionary (unsorted)
digits = {9 : N, 8 : E, 7 : SE, 6 : S, 
5 : FI, 0 : Z, 1 : O, 2 : T, 3 : TH, 4 : F}

#print sorted dictionary for reference  
print('SPELLING DIGITS')
nums = list(digits.keys())
nums.sort()
for i in digits:
    print(nums[i], digits[i])
    
def main():
    ui = input("Enter digit 0-9:")
    
    #validate user input
    while not ui.isdigit() or int(ui) < 0 or int(ui) > 9:
        ui = input("Oops...Enter digit [0-9]:")

    #print result 
    ui = int(ui)
    print(ui, "is spelled:", digits[ui])
    
#test suite
for i in range (0, 3):
    main()

# Program Output#####################
# SPELLING DIGITS                   #                         
# 0 zero                            #
# 1 one                             #
# 2 two                             #
# 3 three                           #
# 4 four                            #
# 5 five                            #
# 6 six                             #
# 7 seven                           #
# 8 eight                           #
# 9 nine                            #
# Enter digit [0-9]:                #
# Oops...Enter digit [0-9]:abc      #
# Oops...Enter digit [0-9]:-5       #
# Oops...Enter digit [0-9]:50       #
# Oops...Enter digit [0-9]:2        #
# 2 is spelled: two                 #
# Enter digit [0-9]: 4              #
# 4 is spelled: four                #
# Enter digit [0-9]: 8              #
# 8 is spelled: eight               #
#####################################
