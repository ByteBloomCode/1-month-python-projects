print("Hello, I am the solver of your math problems.")

process1 = "1)Calculate the area of the square"
process2 = "2)Calculate the area of the circle"
process3 = "3)Calculate the circumference of the circle"
process4 = "4)Calculate the area of the triangle"
PI = 3.14 

print ("All the actions I can do, please choose one of them:\n" + process1 + "\n" + process2 + "\n" + process3 + "\n" + process4)

process = int( input ("Please select one of the following processes(1/2/3/4):") )

if process == 1:
    number1 = float (input("Good choice, now we need a number. What is the length of the side of the square?:"))
    print("When calculating the area of ​​a square, we square the side length.Here is the result:\n", number1*number1)

elif process == 2:
    number2 = float (input("Great choice . When calculating the area of ​​a circle, we use the following formula: PI*r*r Now enter me a radius value:"))
    print("Great, here's your result:\n" , number2*PI*number2)

elif process == 3:
    number3 = float (input("Great choice . What is the radius value of the circle?:"))
    print("When calculating the circumference of a circle, we use the following formula: 2*PI*r After performing this operation, the result is:\n" , 2*PI*number3)

elif process == 4:
    number4 = float(input("Good choice. In general, we use two things when calculating the area of a triangle : First, the height, can you enter the height value of the triangle here? :"))
    number5 = float(input("OK. Now we need the base length to which that height belongs:"))
    print("Now if we multiply these two values ​​and divide by two, we will get the correct result. Here is the result:\n" , number4*number5/2 )
else:
    print("You entered incorrectly :(")

