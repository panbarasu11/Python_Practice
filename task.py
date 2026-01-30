#1 )
vowel=input().lower()
if vowel in 'aeiou':
    print(f"{vowel} is a vowel")
else:
    print(f"{vowel} is not a vowel")
    
a = 20
b = 34
# Swapping the values of a and b
a,b = b,a
print("After swapping:", a, b)

#3)
dividend=int(input())
divisor=int(input())
qut=dividend//divisor
rmd=dividend%divisor
print(f"quotient is {qut} and remainder is {rmd}")

#4)
num=int(input())
if num<0:
    print(f"{num} is negative")
else:
    print(f"{num} is positive")
    
#5)
num=int(input())
if num%2!=0:
    print("odd")
else:
    print("even")
#6)
a=int(input())
b=int(input())
c=int(input())
print(f"{max(a,b,c)} is the largest number")


#4) Convert Minutes to Hours and Minutes
m = int(input("Enter minutes: "))
h = m // 60
print(f"{h} hours {m-(h*60)} minutes")

#5)
num=int(input())
if num<0:
    print("Invalid Input")
else:
    last=num%10
    print(f"last digit is {last}")


#6)
unit=float(input())
if unit<=100:
    bill=unit*2
elif unit<=200:
    bill=100*2+(unit-100)*3
elif unit<=300:
    bill=100*2+100*300+(unit-200)*5
elif unit<=500:
    bill=100*2+100*3+100*5+(unit-300)*7
else:
    bill=100*2+100*3+100*5+200*7+(unit-500)*10
print(f"electicity bill={bill}")

#7)
num=int(input())
if num<0:
    print("Invalid Input")
else:
    if num%5==0 and num%11==0:
        print("Divisible")
    elif num%5==0 and num%11!=0:
        print("Divisible by 5 only")
    elif num%5!=0 and num%11==0:
        print("Divisible by 11 only")
    else:
        print("Not Divisible")

# 8) Convert Days to Years, Weeks, and Days
total_days = int(input('Enter the total days :'))
week = 0
year = 0
days = 0
if total_days<365:
    week = total_days // 7
    days = total_days-week*7
else:
    year = total_days // 365
    total=total_days-365
    week = total//7
    days = (total % 7)

# 9) Leap Year Check
year=int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")     
else:
    print(f"{year} is not a leap year")

#10)    ATM Withdrawal Validation
balance=float(input())
withdrawl=float(input())
if withdrawl%100!=0:
    print("please enter amount in multiple of 100")
elif withdrawl>balance:
    print("entered amount is more than balance enter less than balance")
elif balance-withdrawl<500:
    print("minium balance of 500 should be there after withdrawl")
else:
    print(f"withdrawl is successful new balance is {balance-withdrawl}!!")

#11)Area and Perimeter of Rectangle and Circle
from math import pi
inputt=input("Enter R for rectange and C for circle :" ).lower()
if inputt=='r':
    l=float(input())
    b=float(input())
    area=l*b
    perimeter=2*(l+b)
    print(f"area of rectangle is {area} and perimeter is {perimeter}")
elif inputt=='c':
    r=float(input())
    area=pi*r*r
    perimeter=2*pi*r
    print(f"area of circle is {area} and perimeter is {perimeter}")

#12) Alphabet / Digit / Special Character
character=input()
if character.isalpha():
    print(f"{character} is an alphabet")
elif character.isdigit():
    print(f"{character} is a digit")
elif character.isalnum():
    print(f"{character} is an alphanumeric character")
else:
    print(f"{character} is a special character")

#13)    Compound Interest
P=float(input("Enter principal amount: "))
R=float(input("Enter rate of interest: "))
T=float(input("Enter time in years: "))
CI=P*(1+R/100)**T - P
print("Compound Interest:", CI)