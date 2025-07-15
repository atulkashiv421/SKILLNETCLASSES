
print("Enter your gender:")
print("1 for Male")
print("2 for Female")
gender = int(input("Your choice: "))

age = int(input("Enter your age: "))


if age >= 18:
    print("You are an adult.")


if gender == 1:  
    if age >= 21:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
elif gender == 2:  
    if age >= 18:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
else:
    print("Invalid gender selected.")