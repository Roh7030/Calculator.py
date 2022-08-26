#calculator project
import math 
import numpy

def simple_maths():
    print("\n**Simple Mathematical Calculation**")
    print("1. Addition, Subtraction, Divide, Multiplication, Quotient")
    print("2. Square, Square root, Cube, Cube root")
    print("3. Percentage")
    print("4. Mainmenu")
    value=int(input("Enter your choice: "))
    
    if value==1:
        ad_sub()
        simple_maths()
        
    elif value==2:
        sq_sqrt_cb_cbrt(num)
        simple_maths()
        
    elif value==3:
        percentage()
        simple_maths()
        
    elif value==4:
        mainmenu()

def ad_sub():
    #python program for simple calculator
    #function to add two numbers
    def add(num1,num2):
        return num1+num2
    #function to subtract two numbers
    def subtract(num1,num2):
        return num1-num2
    #function to multipy two numbers
    def multiply(num1,num2):
        return num1*num2
    #function to divide two numbers
    def divide(num1,num2):
        return num1/num2
    print("select the operation\n"\
          "1.add\n"\
          "2.subtract\n"\
          "3.multiply\n"\
          "4.division\n")
    #input from user
    select=int(input("select operation from 1,2,3,4:"))
    num1=int(input("enter the 1st number:"))
    num2=int(input("enter the 2nd number:"))
    
    if select==1:
        print(num1,"+",num2,"=",add(num1,num2))
    elif select==2:
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif select==3:
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif select==4:
        print(num1,"/",num2,"=",divide(num1,num2))
    else:
        print("invalid input")

def percentage():
    #percentage formula
    x=float(input("Enter value : "))
    y=float(input("Enter Total value : "))
    p=(x/y)*100
    
    print(p,"%")

def sq_sqrt_cb_cbrt(num):
    print("select the operation\n"\
        "1. square\n"\
        "2. cube\n"\
        "3. square root\n"\
        "4. Cube root\n"\
        "5. Back")
    #input from server
    select=int(input("select the operation from 1,2,3:"))
    num=int(input("enter the number:"))
    if select==1:
        print("square of",num,"is",num**2)
        sq_sqrt_cb_cbrt(num)
       
    elif select==2:
        print("cube of",num,"is",num**3)
        sq_sqrt_cb_cbrt(num)
        
    elif select==3:
        print("squareroot of",num,"is",math.sqrt(num))
        sq_sqrt_cb_cbrt(num)
        
    elif select==4:
        print("cuberoot of",num,"is",numpy.cbrt(num))
        sq_sqrt_cb_cbrt(num)
        
    elif select==5:
        simple_maths()
        
    else:
        print("**Incorrect Value**")
        sq_sqrt_cb_cbrt(num)

def equation():
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    c = int(input("Enter 3rd value: "))
    
    if a == 0: 
        print("not possible")
        
    else:
        d=(b*b)-(4*a*c)   #discriminant = square of b - 4*a*c
        sqroot = math.sqrt(abs(d))
        
        # when discriminant is greater than 0
        if d > 0: 
            print("roots are real and distinct") 
            print((-b + sqroot)/(2 * a)) 
            print((-b - sqroot)/(2 * a)) 
        
        # when discriminant is equal to 0  
        elif d == 0: 
            print("roots are real and equal") 
            print(-b / (2 * a)) 
          
        # when discriminant is less than 0
        else:
            print("roots are imaginary Complex") 
            print(- b / (2 * a), " + i", sqroot) 
            print(- b / (2 * a), " - i", sqroot)

def Trigonometric_functions():
    print("1. Using Degree value")
    print("2. Using Radian value")
    print("3. Mainmenu")
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        ch=int(input("Enter Your Choice: "))
        
        if ch==1:
            theta=float(input("enter value theta: "))
            print("sin(",theta,") =",math.sin(theta))
            Trigonometric_functions()
            
        elif ch==2:
            theta=float(input("enter value theta: "))
            print("cos(",theta,") =",math.cos(theta))
            Trigonometric_functions()
            
        elif ch==3:
            theta=float(input("enter value theta: "))
            print("tan(",theta,") =",math.tan(theta))
            Trigonometric_functions()
            
    elif ch==2:
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        ch=int(input("Enter Your Choice: "))
        
        if ch==1:
            theta=float(input("enter value theta: "))
            print("sin(",theta,") =",math.asin(theta))
            Trigonometric_functions()
            
        elif ch==2:
            theta=float(input("enter value theta: "))
            print("cos(",theta,") =",math.acos(theta))
            Trigonometric_functions()
            
        elif ch==3:
            theta=float(input("enter value of theta: "))
            print("tan(",theta,") =",math.atan(theta))
            Trigonometric_functions()
            
    elif ch==3:
        mainmenu()
        
    else:
        print("**Incorrect Value**")
        Trigonometric_functions()

def Convert_Degree_To_Radian():
    print("1. Degree -> Radian")
    print("2. Radian -> Degree")
    print("3. Mainmenu")
    ch=int(input("Enter Your Choice: "))
    if ch==1:
        value=float(input("Enter value: "))
        print("Radian(",value,")=",math.radians(value))
        Convert_Degree_To_Radian()
        
    elif ch==2:
        value=float(input("Enter value: "))
        print("Degree(",value,")=",math.degrees(value))
        Convert_Degree_To_Radian()
        
    elif ch==3:
        mainmenu()
        
    else:
        print("**Incorrect Value**")
        Convert_Degree_To_Radian()

def calculate_area():
     #define a function for calculating
    #the area of shapes
    print("1. rectangle \n 2. square \n 3. triangle \n 4.circle \n 5. parallelogram \n 6. back to mainmenu \n")
    ch==int(input("Enter your choice: "))
    
    if ch==1:
        l = int(input("Enter rectangle's length: "))
        b = int(input("Enter rectangle's breadth: "))
        rect_area= l * b
        print(f"the area of rectangle is{rect_area}.")
        calculate_area()
        
    elif ch==2:
        s = int(input("Enter square's side length: "))
        sqt_area = s * s
        print(f"The area of square is{sqt_area}.")
        calculate_area()
    
    elif ch==3:
        h = int(input("Enter triangle's height length: ")) 
        b = int(input("Enter triangle's breadth length: ")) 
        tri_area = 0.5 * b * h
        print("The area of triangle is{tri_area}.")
        calculate_area()
        
    elif ch==4:
        r = int(input("Enter circle's radius length: ")) 
        pi = 3.14 
        circ_area = pi * r * r
        print("The area of triangle is{circ_area}.")
        calculate_area()
     
    elif ch==5:
        b = int(input("Enter parallelogram's base length: ")) 
        h = int(input("Enter parallelogram's height length: ")) 
        para_area = b * h 
        print("The area of parallelogram is{para_area}.")
        calculate_area()
        
    elif ch==6:
        mainmenu()
     
    else: 
        print("Sorry! This shape is not available")
        calculate_area()

def mainmenu():
    print("\n\n**Welcome to Main Menu**")
    print("1. Simple Mathematical Calculation")
    print("2. Find Area")
    print("3. Solve Quadratic Equation")
    print("4. Trigonometric Function")
    print("5. Conversion of Angle\n")
    ch=int(input("Enter your choice:"))
    
    if ch==1:
        simple_maths()
        
    elif ch==3:
        equation()
        
        y=input("Do you want to go Mainmenu(if yes type 'y'): ")
        if(y=='y'):
            mainmenu()
            
        else:
            equation()
        
    elif ch==4:
        Trigonometric_functions()
        
    elif ch==5:
        Convert_Degree_To_Radian()

    else:
        print("**Incorrect Value**\n**Please try again**")
        mainmenu()

mainmenu()
1
100
kkk
