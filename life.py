def life_in_weeks():
    current_age = int(input("Enter your current age!"))
    yearremain=90-current_age
    weeks=yearremain*52
    print(f"You have {weeks} weeks left.")
life_in_weeks()