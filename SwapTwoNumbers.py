# a = 20
# b = 34
# # Swapping the values of a and b
# a,b = b,a
# print("After swapping:", a, b)

#4) Convert Minutes to Hours and Minutes
# m = int(input("Enter minutes: "))
# h = m // 60
# print(f"{h} hours {m-(h*60)} minutes")

# 5) Convert Days to Years, Weeks, and Days
# total_days = int(input('Enter the total days :'))
# week = 0
# year = 0
# days = 0
# if total_days<365:
#     week = total_days // 7
#     days = total_days-week*7
# else:
#     year = total_days // 365
#     total=total_days-365
#     week = total//7
#     days = (total % 7)

# print(f"{year} Years {week} Weeks {days} Days")

# #16) Alphabet / Digit / Special Character
# a=input("enter the character:")
# if (a >= 'a' and  a<= 'z') or (a>='A' and a<='Z'):
#     print("ALPHABET")
# elif a >="0" and a<="9":
#     print("digit")
# else:
#     print("special character")

#19) ATM Withdrawal Validation

amount = int(input("Enter the account amount:"))
withdraw = int(input("Enter the withdraw amount: "))

if withdraw % 100 == 0:
    if amount >= withdraw :
        balance=amount-withdraw
        if balance <= 500:
            print("balance must be > 500")
        else:
            print("withdraw successful")

        
    