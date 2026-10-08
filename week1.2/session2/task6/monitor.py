# Week 1.2, Session 2: Task 6

temperature = int(input("Enter the machine's temperature in degrees Celsius : "))
pressure = int(input("Enter the machine's pressure in PSI : "))
operational_status = int(input("Enter status : (1/0)"))

if temperature > 80 :
    print(" Warning! The temperature is too high, Please shut it down ")
elif 50 < temperature < 80 :
    print("The temperature is within safe limits")
elif temperature < 50 :
    print("The machine's temperature is low and no action needed")

if pressure > 100 :
    print("high pressure is detected and recommend maintenance")
elif 70 > pressure > 100 :
    print("the pressure is stable")
elif pressure < 70 :
    print("the pressure is low and the system is operating normally")

if operational_status == 1:
    if temperature > 80 :
        if pressure > 100 :
            print("the machine is running in unsafe conditions and recommend shutting it down")
if operational_status == 0 :
    print("it is stopped and no immediate action is needed")