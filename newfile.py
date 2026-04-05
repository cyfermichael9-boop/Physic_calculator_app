def age_future(name, age):
    plus = 35
    nextyear = age + plus
    print("Hello", name, "you will be", nextyear, "in the next 35 years")


def calculator():
    A = int(input("Enter first number: "))
    B = int(input("Enter second number: "))
    operation = input("Choose (+, -, *, /, **): ")

    if operation == "+":
        print("Answer:", A + B)
    elif operation == "-":
        print("Answer:", A - B)
    elif operation == "*":
        print("Answer:", A * B)
    elif operation == "/":
        print("Answer:", A / B)
    elif operation == "**":
        print("Answer:", A ** B)
    else:
        print("Invalid operation")
        
      
def force():
	Acceleration=float(input("Enter acceleration (m/s^2):"))
	Mass=float(input("Enter mass (m/s^2):"))
	print("force = ",Acceleration*Mass,"N")
	
	
def speed():
	Distance=float(input("Enter distance (s):"))
	Time=float(input("Enter Time (t):"))
	print("speed =",Distance/Time, "m/s^1")
	
	
def distance():
	speed=float(input("Enter speed (m/s^1):"))
	Time=float(input("Enter time (t):"))
	print("distance =",speed*Time,"s")
	
	
while True:
	name=input("Enter your name:")
	age=int(input("Enter your age:"))
	
	age_future(name, age)
	calculator()
	
	print("n/physic calculator")
	print("1.force")
	print("2.speed")
	print("3.distance")
	
	choice=input("choose an option(1/2/3):")
	if choice=="1":
		force()
	elif choice=="2":
	    speed()
	elif choice=="3":
	 	distance()
	else:
	 	print ("invalid choice")
	 	
	 	
	 	again=input("continue? (yes/no):")
	 	if again.lower()=="no":
	 		print("Goodbye!")
	 		break
	 	
	 	
	 	


	 	
	 
	 
	 
	
	
	
	
	
