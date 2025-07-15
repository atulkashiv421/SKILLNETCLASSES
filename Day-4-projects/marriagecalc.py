print("=== Welcome to the Marriage Calculator ===")

while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()

    
    if gender == "male":
        if age >= 21:
            print(f"{name}, you are eligible for marriage ")
        else:
            print(f"{name}, you need to wait {21 - age} more year(s) to be eligible")
    elif gender == "female":
        if age >= 18:
            print(f"{name}, you are eligible for marriage ")
        else:
            print(f"{name}, you need to wait {18 - age} more year(s) to be eligible")
    else:
        print("Invalid gender input. Please enter 'male' or 'female'.")

    
