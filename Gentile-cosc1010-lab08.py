# Joshua Gentile
# UWYO COSC 1010
# Submission Date 11/07/2024
# Lab 08
# Lab Section: 18
# Sources, people worked with, help given to: Austin Barner
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def string_converter(num):
    "check if string is int or float"
    isneg = False
    if num[0] == "-":
        num = num.replace("-","")
        isneg = True
    if "." in num:
        num_list = num.split(".")
        if len(num_list) == 2 and num_list[0].isdigit() and num_list[1].isdigit():
            if isneg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isneg:
            return -1 * int(num)
        else:
            return int(num)
    return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_x, upper_x):
    "calculates y for a given range of x"
    list1 = []
    for v in range(lower_x, upper_x+1):
        out1 = (m*v)+b
        list1.append(out1)
    return list1

while True:
    m_input = input("Enter slope ")
    if m_input.lower() == "exit":
        break
    b_input = input("Enter Y intercept ")
    if b_input.lower() == "exit":
        break
    low_x = input("Enter low range of x ")
    if low_x.lower() == "exit":
        break
    high_x = input("Enter high range of x ")
    if high_x.lower() == "exit":
        break
    else:
        m_input = string_converter(m_input)
        b_input = string_converter(b_input)
        low_x = string_converter(low_x)
        high_x = string_converter(high_x)
        out2 = slope_intercept(m_input, b_input, low_x, high_x)
        print(out2)


print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def quadratic_formula(a, b, c):
    "finds the solution to a quadratic function"
    list2 =[]
    list3 = []
    o1 = (b**2) - 4*a*c
    if "-" in o1:
        return "null"
    o1 = o1**(.5)
    list2[0] = -b + o1
    list2[1] = -b - o1
    for i in list2:
        n = i/(2*a)
        list3.append(n)
        return list3


while True:
    a_input = input("Enter A ")
    if a_input.lower() == "exit":
        break
    d_input = input("Enter B ")
    if d_input.lower() == "exit":
        break
    c_input = input("Enter C ")
    if c_input.lower() == "exit":
        break

    else:
        c_input = string_converter(a_input)
        d_input = string_converter(d_input)
        c_input = string_converter(c_input)
        out3 = quadratic_formula(a_input, d_input, c_input)
        print(out3)

# I don't know whats wrong or how to fix it. I give up.