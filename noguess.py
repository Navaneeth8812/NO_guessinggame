import random
count=0
randvar = random.randint(1,100)
print("____WELCOME TO NUMBER GUESSING GAME___")
print("__YOUVE GOT 5 CHANCES__")
while(count<=5):
        count+=1
        user_Num=int(input("ENTER THE NUMBER\n"))

        if(user_Num==randvar):
            print("CORRCT!\n")
            break
        elif(user_Num>randvar):
                    print("TOO HIGH!\n")
        else:
                    print("TOO LOW!\n")
else:
        print("OUT OF ATTEMTS\n" f"THE CURRECT NUMBER IS {randvar}")

  
