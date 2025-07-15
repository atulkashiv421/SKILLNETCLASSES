# Water bottle calculator

total_bottles = int(input("Enter total water bottles: "))
daily_use = int(input("Enter bottles you drink per day: "))

day = 1  

while total_bottles > 0:
    print(f"\nDay {day}:", end=" ")
    
    if total_bottles >= daily_use:
        total_bottles -= daily_use
        print(f"Drank {daily_use} bottles. {total_bottles} left.")
    else:
    
        print(f"Drank {total_bottles} bottle{'s' if total_bottles > 1 else ''}. 0 left.")
        total_bottles = 0  
    
    day += 1
