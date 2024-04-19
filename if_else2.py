
print("Welcome to our riding world")
height = float(input("first check your height (cm):"))

if height >= 120:
    price = 0
    print("child ticket are $5 /n youth ticket are $7 /n adult tickets are $12")
   
    age = int(input("how old are you"))
    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    else:
        price = 12

    photo_taken = input("phtot khchoni? Y or N")
    if photo_taken.lower() == "y":
        price += 5
    print(f"Your final bill is ${price}")

else:
    print("You are small now")
 