status_code = int(input("Enter your choice: "))

match status_code:
    case 200:
        print("Student grade is high")
        print("This is success")
    case 400:
        print("Student grade is low")
        print("This is failure")
    case _:
        print("Student grade is low")
        print("This is not success")