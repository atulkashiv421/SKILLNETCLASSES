def restaurant_tip_simulator():
    try:
        
        bill_amount = float(input("Enter the total bill amount: $"))
        if bill_amount <= 0:
            print("Bill amount must be greater than zero.")
            return

        
        num_friends = int(input("Enter the number of friends to split the bill: "))
        if num_friends <= 0:
            print("Number of friends must be at least 1.")
            return

        
        tip_percentage = float(input("Enter the tip percentage (10 to 50): "))
        if tip_percentage < 10 or tip_percentage > 50:
            print("Tip percentage must be between 10% and 50%.")
            return

        
        tip_amount = bill_amount * (tip_percentage / 100)
        total_with_tip = bill_amount + tip_amount
        per_person_no_tip = bill_amount / num_friends
        per_person_with_tip = total_with_tip / num_friends

        
        print("\n--- Bill Summary ---")
        print(f"Total Bill: ${bill_amount:.2f}")
        print(f"Tip Percentage: {tip_percentage}%")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total with Tip: ${total_with_tip:.2f}")
        print(f"Each person pays (without tip): ${per_person_no_tip:.2f}")
        print(f"Each person pays (with tip): ${per_person_with_tip:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

restaurant_tip_simulator()
