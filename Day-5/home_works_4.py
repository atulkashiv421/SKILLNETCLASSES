def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

student_info(name="atul", age=18, roll_number=353)
