print("Welcome to uber services!!!")
sp= int(input("Enter starting point in km"))      #user input for starting point in integer
dp= int(input("Enter destination point in km"))   #user input for destination point in integer
dist=dp-sp                                        #computing total distance
print("1.Two wheeler")
print("2.Car")
print("3.Auto")
ch = (input("Enter your choice of travel"))       #getting user choice
if(ch=="1" or ch=="Two wheeler"):
        amount=5*dist                             #two wheeler cost per km is 5
        print("-------Billing Info-------")
        print("starting point is ",sp)
        print("destination point is ",dp)
        print("Total distance is ",dist)
        print("Total amount to be paid",amount)
        print("Enjoy your Ride")
elif(ch=="2" or ch=="Car"):
        amount=9*dist                             #cab per km is 5
        print("------Billing Info-------")
        print("starting point is ",sp)
        print("destination point is ",dp)
        print("Total distance is ",dist)
        print("Total amount to be paid",amount)
        print("Enjoy your Ride")
elif(ch=="3" or ch=="Auto"):                    
        amount=12*dist                           #Auto km is 5
        print("------Billing Info-------")
        print("starting point is ",sp)
        print("destination point is ",dp)
        print("Total distance is ",dist)
        print("Total amount to be paid",amount)
        print("Enjoy your Ride")
else:
        print("Enter a valid input")
