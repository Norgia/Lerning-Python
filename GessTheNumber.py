#rep
import random

#random var
ran = random.randint(0,99)
print("I am thinking about a number between 0 and 100, gess the number ")

roler = 0 #Stop loop var
while roler == 0:
    while True: #chacking for input error
        try:
            guss = int(input())
            break
        except ValueError:
            print("Oops, try again ")

    if(guss == ran): #coreccet
        print("yes corect ",ran," was the number ")
        roler = 1
    elif(guss <= ran): #to low
        print("Nope to low, try again!")
    elif(guss >= ran): #to high
        print("Nope to high, try again!")
#how to fucking easy
