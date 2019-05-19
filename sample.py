#Sample program with fixed traffic light scheme
cycle_input = input("Please input how many cycles:")
cycles = int(cycle_input)
redlight = input("Red light duration: ")
greenlight = input("Green light duration: ")

total = 0
#create list for storing the 4 lanes and these lanes containing
#the number of cars queued
for x in range(cycles):
    print("Enter number of cars")
    abanao = int(input("Abanao: " ))
    harrison = int(input("Harrison: " ))
    magsaysay = int(input("Magsaysay: " ))
    venice = int(input("Venice: " ))
    total += abanao + harrison + magsaysay + venice
    print("")
    print("-----------")
print(total)