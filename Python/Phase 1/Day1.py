                             #Variables and Data Types (int, float, str, bool, None)

#Store your name, age, and height in variables. Print all with their types.
'''
name="poorna"
age=21
height=5.10
print(type(name),type(age),type(height))'''

#Take two numbers, one integer and one float. Add them and print the result and type.
'''
a,b=1,2.3
c=a+b
print(c)
print(type(c))'''

# Assign a None value to a variable. Print it and its type.
'''
name=None
print(name)
print(type(name))'''

#Create a variable is_student and assign True. Print its type.
'''
is_student= True
print(type(is_student))'''

#Use input() to take a string from the user. Print the value and type.
'''
a=input()
print(type(a))'''

#Convert a float to int and print both.
'''
a=5.5
b=int(a)
print(a)
print(b)'''

#Check the type of each variable in a list of mixed values: [10, 3.5, "yes", False, None]
'''
l=[10, 3.5, "yes", False, None]
for i in l:
    print(i,type(i))'''

#Write a program that takes two numbers from user input and prints their sum and data types.
'''
a=int(input())
b=int(input())
sum=a+b
print(sum)
print(type(sum))'''

#Try to add an int and a string. What happens? Try to fix it using type casting.
'''
a=7
b='10'
c=a+int(b)
print(c)'''

#Write a code that checks if a number is even or odd using boolean logic.
'''
a=10
is_even=(a%2==0)
print(is_even)'''

                            #Input/Output (input(), print())
                            
#Ask the user their name and print a greeting. Example Output: Hello, Poorna!

'''
name=input()
print("Hello,",name,sep=" ",end="!")'''

#Ask the user to enter their age and print what their age will be next year.
'''age=int(input())
print("your age next year is",age+1)'''

#Ask the user to enter their city and state, then print in this format:
"You live in Hyderabad, Telangana."
'''city=input()
state=input()
print(f"You live in {city}, {state}.")'''

#Take user input and print the same input 3 times in one line, separated by - Example: input = hello → Output: hello-hello-hello

'''a=input()
print(f"{a}-{a}-{a}")'''

                            #Operators (Arithmetic, Comparison, Logical, Assignment)

#Take two numbers from the user and print their:Sum,Difference,Product,Quotient (using /),Remainder
'''a=int(input())
b=int(input())
print("sum=",a+b)
print("sub=",a-b)
print("prod=",a*b)
print("quo=",a/b)
print("rem=",a%b)'''

#Take a number and print its square and cube (use ** operator).
'''a=int(input())
print("square=",a**2)
print("cube=",a**3)'''

#Take hours and convert to minutes using multiplication.
'''hours=int(input())
print("minutes=",hours*60)'''

#Take total marks and number of subjects, print average marks using /.
'''total_marks=int(input())
no_of_subjects=int(input())
print("avg=",total_marks/no_of_subjects)'''

#input price and quantity of a product, calculate and print total cost.
'''price=120
quantity=4
total=price*quantity
print(total)'''

#Create a variable x = 10, then add 5 to it using +=, print final value.
'''x=10
x+=5
print(x)'''

#Take a number and double it using *= operator.
'''num=5
num*=2
print(num)'''

#Subtract 3 from a number using -= and print.
'''num=5
num-=3
print(num)'''

#Take two numbers and print whether they are equal or not.
'''a=3
b=4
c=(a==b)
print(c)'''

#Take two inputs and print which one is greater.
'''a=3
b=4
c=a>b
if c:
    print(" a is greater")
else:
    print("b is greater")'''
    
#Check if a given number is less than or equal to 100.
'''a=65
print(a<=100)'''

#Take two numbers and check if both are greater than 10 (use and).
'''a=3
b=3
print(a> 100 and b > 100)'''

#Take age and city, print if person is eligible: Eligible if age ≥ 18 or city is "Hyderabad".
'''age=34
city="hyderabad"
if(age>=18 or city=="hyderabad"):
    print("eligible")'''
    
#Use not to reverse a boolean input.Example: is_registered = True → print False
'''num=True
print(not num)'''


                        #Control Flow (if, elif, else)

#Take a number and check if it's positive.
'''a=int(input())
if a>=0:
    print("positive")
else:
    print("negative")'''

#Input a number and check if it is even or odd.
'''a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")'''
    
#Ask user for age and check if they are eligible to vote (18+).
'''age=int(input())
if age>18:
    print("eligible")
else:
    print("not eligble")'''
    
#Take temperature as input and print whether it is hot (>30) or cold (≤30).
'''temp=int(input())
if temp<=30:
    print("cold")
else:
    print("hot")'''

#Ask user for a number and check if it is divisible by 5.
'''num=int(input())
print(num%5==0) '''   

#Take marks from the user and print:
'''
A if ≥90

B if 75–89

C if 60–74

D if 40–59

Fail if <40 '''
'''marks=int(input())
if marks>=90:
    print("A")
elif 75<=marks<=89:
    print("B")
elif 60<=marks<=74:
    print("C")
elif 40<=marks<=59:
    print("D")
else:
    print("Fail")'''
    
#Ask user to enter a day number (1 to 7). Print the day name using if-elif.
'''num=int(input())
if num==1:
    print('mon')
elif num==2:
    print('tue')
elif num==3:
    print('wed')
elif num==4:
    print('thu')
elif num==5:
    print('fri')
elif num==6:
    print('sat')
elif num==7:
    print('sun')
else:
    print("invalid")'''
    
#Take number of working hours from user:
'''
If ≥40 → "Full-time"

If 20–39 → "Part-time"

If <20 → "Intern" '''

''''whrs=int(input())
if whrs>=40:
    print("Full-time")
elif 20<=whrs<=39:
    print("Part-time")
else:
    print("Intern")'''

#Input a number and:
'''
If it is 0 → print "Zero"

If it is >0 → print "Positive"

Else → print "Negative"'''

'''num=int(input())
if num==0:
    print("Zero")
elif num>0:
    print("Positive")
else:
    print("Negative")'''
    
#Ask user for speed:

'''If speed > 100 → "Over Speeding"

If 60–100 → "Normal"

Else → "Too Slow"'''

'''speed=int(input())
if speed>100:
    print("Over Speeding")
elif 60<=speed<=100:
    print("Normal")
else:
    print("Too Slow")'''

#Take age and gender. Print:
'''
"Eligible for job" if age ≥ 21 and gender is "Male"

"Eligible for training" if age ≥ 18 and gender is "Female"

Else → "Not eligible"'''
'''age=int(input())
gender=input()
if age>=21 and gender =="male":
    print("Eligible for job")
elif age>=18 and gender == "female":
    print("Eligible for training")
else:
    print("Not eligible")'''

#Ask user to enter a character. Print:

''' "Vowel" if it's a, e, i, o, u (case-insensitive)

Else → "Consonant" '''

'''char=input()
if char in "aeiou":
    print("vowel")
else:
    print("consonant")'''
    
#take three numbers and print the largest one.
'''a=int(input())   
b=int(input())
c=int(input())
if(a>b) and (a>c):
    print("a")
elif b>a and b>c:
    print("b")
else:
    print("c")'''
    
#Take a year as input and print if it's a leap year or not.
'''year=int(input())
if( year%4==0 and year%100!=0  ) or year%400==0:
    print("leap year")
else:
    print("not a leap year")'''

#Take username and password input. Check if they match with pre-stored values.
'''username="admin"
password=123
user=input()
passw=int(input())
if username ==user and password==passw:
    print("login successful")
else:
    print("invalid ")'''

#Build a basic calculator:
'''
Take two numbers and an operator (+, -, *, /)
Perform the operation using if-elif'''
'''a=int(input())
b=int(input())
c=input()
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print("invalid")'''
    
#ATM Program:

'''Ask user to enter pin

If correct → print balance

Else → print "Invalid pin"'''

'''stored_pin=1234
pin=int(input())
if pin==stored_pin:
    print("your balance is 1000")
else:
    print("invalid pin")'''
    
#Exam Grading System:
'''
Take 3 subject marks

Calculate average

Give grade based on average'''

'''tel=int(input())
eng=int(input())
soc=int(input())
avg=(tel+eng+soc)/3
if avg>90:
    print("A grade")
elif 80<=avg<=90:
    print("B grade")
elif 70<=avg<80:
    print("C grade")
elif 60<=avg<70:
    print("D grade")
else:
    print("Fail")'''
    
#Input 3 angles and check if they can form a triangle (sum = 180)
'''a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
if (a+b+c)==180:
    print("Triangle")
else:
    print("not a triangle")'''


#Train Ticket Discount:

'''If age < 5 → Free

5–18 → Half

60+ → Senior citizen discount

Else → Full fare'''

'''age=int(input())
if age<5:
    print("Free")
elif 5<=age<=18:
    print("half")
elif 18<age<=59:
    print("Full")
else:
    print("Senior citizen discount")'''
    




