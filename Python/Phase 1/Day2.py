        #Nested if-else
#Grading System with Pass/Fail Check
'''Take 3 subject marks from the user.

If average ≥ 40 → Pass

Then: if avg ≥ 90 → Grade A
elif avg ≥ 75 → Grade B
else → Grade C

Else → Print “Fail”'''

'''tel=int(input())
eng=int(input())
soc=int(input())
avg=(tel+eng+soc)/3
if avg>=40:
    print("pass")
    if avg >=90:
        print("A grade")
    elif avg>=75:
        print("B grade")
    else:
        print("C grade")
else:
    print("Fail")'''
    

#Login Check (Nested Condition)
'''Ask for username.

If username is correct:

Ask for password.

If password is correct → Print “Login successful”

Else → Print “Wrong password”

Else → Print “Invalid username”'''

'''s_user='admin'
s_pass=1234
username=input()
password=int(input())
if username==s_user:
    if password==s_pass:
        print("login successful")
    else:
        print("wrong password")
else:
    print("wrong username")'''
    
#Triangle Type Checker
'''Take 3 angles.

If sum = 180:

Then:

If all angles are equal → Equilateral

Else if any two equal → Isosceles

Else → Scalene

Else → Not a triangle'''

'''a,b,c=input().split()
a=float(a)
b=float(b)
c=float(c)
if (a+b+c)==180:
    if a==b and b==c and c==a :
        print("equilateral traingle")
    elif a==b or b==c or c==a:
        print("isosceles traingle")
    else:
        print("scalene")
else:
    print("not a triangle")'''
    
# Sports Eligibility
'''Ask for age and gender.

If age ≥ 18:

If gender is "male" → Eligible for football

If gender is "female" → Eligible for volleyball

Else → Not eligible'''

'''age=int(input())
gender=input()
if age>=18:
    gender=gender.lower()
    if gender=='male':
        print("eligible for football")
    elif gender=='female':
        print("eligible for volleyball")
else:
    print(" not eligible ")'''
  
# ATM Withdrawal Logic
'''Ask for PIN.

If correct:

Ask for withdrawal amount.

If amount ≤ balance → Show success

Else → Print “Insufficient balance”

Else → Print “Invalid PIN” ''' 

'''balance=50000
pin=1234
user_pin=int(input())
amount=int(input("enter amount"))
if user_pin==pin:
    if amount<=balance:
        print("success")
    else:
        print("Insufficient balance")
else:
    print("invalid pin")'''
    
#Online Order Check
'''Ask if item is in stock (yes/no).

If yes:

Ask for payment method (online/cash)

If online → Confirm order

If cash → Ask for delivery address

Else → Print “Out of stock”'''

'''stock=input("is stock available").lower()
if stock=='yes':
    pay_method=input("payment method?").lower()
    if pay_method=='online':
        print("order confirmed")
    elif pay_method=='offline':
        print("enter your address")
    else:
        print("something went wrong")
else:
    print("out of stock")'''
    
    
    
    
                        #Loops (for, while)
                        
#Print numbers 1 to 10 (basic range)
'''for i in range(1,11):
    print(i)'''
    
#Display even numbers between 1 and 30
'''for i in range(2,31,2):
    print(i)'''
    
#Ask the user for a number and display its multiplication table from 1 to 10
'''num=int(input())
for i in range(1,11):
    multi=num*i
    print(num,'*',i,'='," ",multi)'''
    
#Print the squares of numbers from 1 to 5
'''for i in range(1,6):
    print(i*i)'''
#Print each character of the word “PYTHON” vertically
'''word="PYTHON"
for i in word:
    print(i)'''
    
#Count how many vowels are in the string entered by the user
'''name=input().lower()
count=0
for i in name:
    if i in "aeiou":
        count+=1
print(count)'''

#Ask the user for a number and print all numbers less than it that are divisible by 3
'''num=int(input())
for i in range(1,num):
    if i %3==0:
        print(i)'''
        
#Take a string and print only the letters that are uppercase
'''name=input()
for i in name:
    if i in name.upper():
        print(i)'''
    
#Print first 10 multiples of 7
'''for i in range(1,11):
    print(7*i)'''
    
#Take 5 numbers from the user and print their average
'''total=0
for i in range(5):
    num=int(input(f"enter {i+1}"))
    total+=num
avg=total/5
print(avg)'''

#Print numbers from 10 to 1 (reverse)
'''for i in range(10,0,-1):
    print(i)'''
    
#Print factorial of a number (e.g., 5! = 120)
'''n=5
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''

#Print all numbers from 1 to 50 that are divisible by both 3 and 5
'''for i in range(1,51):
    if i%3==0 and i%5==0:
        print(i)'''
        
#while loops 
#Print numbers from 1 to 10 using a while loop
'''i=0
while(i<=10):
    print(i)
    i=i+1'''
    
#Print a countdown from 10 to 1
'''i=10
while(i>=1):
    print(i)
    i-=1'''

#Keep asking the user for a password until they enter the correct one
'''s_pass=1234
while True:
    password=int(input("enter pass"))
    if s_pass==password:
        print("success")
        break
    else:
        print("enter again")'''

#Keep taking numbers from user and add to a total until user enters 0 (zero)
'''total=0
while True:
    num=int(input())
    if num==0:
        break
    else:
        total+=num
print("total",total)'''

#Ask user for a number and print its factorial using while
'''num=int(input())
fact=1
while(num>=1):
    fact=fact*num
    num-=1
print(fact)'''

#Keep asking for marks until a valid mark (0–100) is entered
'''while True:
    marks=int(input("marks"))
    if 0<marks<=100:
        break
    else:
        print("enter value 0-100") '''

#Menu-based system:

'''Add

Subtract

Exit
Keep repeating until user selects Exit '''

choice=0
while choice!=0:
    print("1.add")
    print("2.sub")
    print("3.exit")
    choice=int(input("enter your action"))
    a=int(input("enter 1st number"))
    b=int(input("enter 1st number"))
    if choice==1:
        print("add=",a+b)
    elif choice==2:
        print("add=",a-b)
    else:
        print("exiting...")

    
        
    
    
    
    
        




