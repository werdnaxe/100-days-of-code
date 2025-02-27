height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))
    if 45 <= age <= 55:
        bill = 0
        print("Tickets are free.")
    elif age > 18:
        bill = 12
        print("Adult tickets are 12.")
    elif age >= 12:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 5
        print("Child tickets are $5.")
    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo == "Y":
        #Add $3 to bill
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You need to grow taller")
