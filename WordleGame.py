print("Wordle - Color + Preset Word".center(150))

"""TO BE IMPLEMENTED ON OTHER COMPUTER"""
#1 - #If an1+ans2+an3...+ans5 != any word from library, print("Not a valid number, try again") and iteration +=-0 
#2 - #Do you want to play again --> reset (q for quit, maybe?, anything else = 'I want to play again')


print("X | X | X | X | X")
print()

print("Why are you looking at this, I thought you wanted the element of surprise?")
print()
print("Current Rules - enter in one letter at a time, HAS strip, must be in all caps (caps not yet implemented - on other computer will be all lowercase)")
print()
#word = yeast  

X1 = "Y"
X2 = "E"
X3 = "A"
X4 = "S"
X5 = "T"

import string

iterations = 6 
iteration = 0


while (iteration <6): #runs for 6 iterations then ends
    iteration += 1
    end = False

    print()
    L1 = input("Guess letter 1: ")
    L1 = L1.strip() #strip for extra spaces - Not yet in other computer 
    L2 = input("Guess letter 2: ")
    L2 = L2.strip()
    L3 = input("Guess letter 3: ")
    L3 = L3.strip()
    L4 = input("Guess letter 4: ")
    L4 = L4.strip()
    L5 = input("Guess letter 5: ")
    L5 = L5.strip()

    def color_string(text, color_code):
        return f"\033[{color_code}m{text}\033[0m"


    if (L1 == X1):
        ans1 = str(X1) #if its correct store answer as x1 
    elif (L1 == X2 or L1 == X3 or L1 == X4 or L1 == X5):
        ans1 = str(L1) #if its in the wrong spot, store answer as your input
    else:
        ans1 = str(L1) #if its wrong, store answer also as input
        
    
    if (L2 == X2):
        ans2 = str(X2)
    elif (L2 == X1 or L2 ==X3 or L2 == X4 or L2 == X5 ):
        ans2 = str(L1)
    else:
        ans2 = str(L2)
    
    if (L3 == X3):
        ans3 = str(X3)
    elif (L3 == X2 or L3 ==X1 or L3 == X4 or L3 == X5 ):
        ans3 = str(L3)
    else:
        ans3 = str(L3)
    
    if (L4 == X4):
        ans4 = str(X4)
    elif (L4 == X2 or L4 == X3 or L4 == X1 or L4 == X5 ):
        ans4 = str(L4)
    else:
        ans4 = str(L4)
    
    if (L5 == X5):
        ans5 = str(X5)
    elif (L5 == X2 or L5 == X3 or L5 == X1 or L5 == X4 ):
        ans5 = str(L5)
    else:
        ans5 = str(L5)

    #COLOR BLOCKING SLAYYY
        #Printing in Yellow for wrong spot is not working 
        
    print()
    def color_string(text, color_code):
        return f"\033[{color_code}m{text}\033[0m"

    if ans1 == str(X1):
        ans1 = color_string(str(X1), "32") #if its the same as X1 (correct letter) store answer as green
    elif (L1 == X2 or L1 ==X3 or L1 == X4 or L1 == X5 ):
        ans1 = color_string(str(L1), "33") #yellow
    else:
        ans1 == color_string(str(L1), "90") #green

    if ans2 == str(X2):
        ans2 = color_string((str(X2)), "32")
    elif (L2 == X1 or L2 ==X3 or L2 == X4 or L2 == X5 ):
        ans2 = color_string(str(L2), "33")
    else:
        ans2 == color_string(str(L2), "90")

    if ans3 == str(X3):
        ans3 = color_string(str(X3), "32")
    elif (L3 == X2 or L3 ==X1 or L3 == X4 or L3 == X5 ):
        ans3 = color_string(str(L3), "33")
    else:
        ans3 == color_string(str(L3), "90")

    if ans4 == str(X4):
        ans4 = color_string(str(X4), "32")
    elif (L4 == X2 or L4 == X3 or L4 == X1 or L4 == X5 ):
        ans4 = color_string(str(L4), "33")
    else: 
        ans4 == color_string(str(L4), "90")

    if ans5 == str(X5):
        ans5 = color_string(str(X5), "32")
    elif (L5 == X2 or L5 == X3 or L5 == X1 or L5 == X4 ):
        ans5 = color_string(str(L5), "33")
    else:
        ans5 == color_string(str(L5), "90")

    
    answer = (ans1+" | "+ans2+" | "+ans3+" | "+ans4+" | "+ans5)
    print(answer) #print the whole thing together
    alphabet = list(string.ascii_uppercase) #list of all alphabet
    print(alphabet)
    for i, item in enumerate(alphabet):
        if item == X1:
            alphabet[i] = color_string(str(X1), "33")  # Replace X1 in list with yellow X1 in list

    print(alphabet)

    print()
    if (L1 ==X1 and L2 == X2 and L3 ==X3 and L4 == X4 and L5 == X5) and iteration == 1:
        print ("Genius") #first try
        print()
        end = True
    elif (L1 ==X1 and L2 == X2 and L3 ==X3 and L4 == X4 and L5 == X5) and iteration == 2:
        print ("Magnificent") #second try
        print()
        end = True
    elif (L1 ==X1 and L2 == X2 and L3 ==X3 and L4 == X4 and L5 == X5) and iteration == 3:
        print ("Impressive") #third try
        print()
        end = True
    elif (L1 ==X1 and L2 == X2 and L3 ==X3 and L4 == X4 and L5 == X5) and iteration == 4:
        print ("Splendid") #fourth try
        print()
        end = True
    elif (L1 ==X1 and L2 == X2 and L3 ==X3 and L4 == X4 and L5 == X5) and iteration == 5:
        print ("Great") #fifth try
        print()
        end = True
    elif (L1 ==X1 and L2 == X2 and L3 ==X3 and L4 == X4 and L5 == X5) and iteration == 6:
        print ("Phew") #sixth try
        print()
        end = True
    elif (L1 !=X1 or L2 != X2 or L3 !=X3 or L4 != X4 or L5 != X5) and iteration <= 5:
        print("Tough Luck! Try again") #not the answer 'tough luck' 
    elif (L1 !=X1 or L2 != X2 or L3 !=X3 or L4 != X4 or L5 != X5):
        print("Bruh") #not the answer and you lost = 'bruh' 
        print()
        print(X1,X2,X3,X4,X5)
        print()
        



    if (end == True): #if the answer = the Word, iteration = 6, which triggers the quit 
        iteration = 6
