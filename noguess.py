import random
randvar = random.randint(1,100)
while(True):
    user_Num=int(input("enter the number"))
    if (user_Num>randvar):
                    print("a little less")
    elif(user_Num<randvar):
                    print("a little higher")
    else:
        print("you've guessed it correctly")
        break
        
          
