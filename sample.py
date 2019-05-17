#Sample program with fixed traffic light scheme
cycle_input = input("Please input how many cycles:")
cycles = int(cycle_input)
redlight = input("Red light duration:")
greenlight = input("Green light duration:")
abanao = 37.28571429
harrison = 40.14285714
magsaysay = 57.42857143
venice = 36.28571429
total = 0
#create list for storing the 4 lanes and these lanes containing
#the number of cars queued
for x in range(cycles):
    total += abanao + harrison + magsaysay + venice
print(total)