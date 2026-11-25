
# Attendance Recovery Computation

attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
target = 75

if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details")

else:
    current = (attended / conducted) * 100
    print("\nCurrent Attendance:", round(current, 2), "%")

    if current >= target:
        print("You are eligible for examination.")
    else:
        print("You are not eligible for examination.")

    print("\n--- Attendance Recovery Scenarios ---")

    scenarios = [100, 90, 75]

    for rate in scenarios:
        future = 0
        new_attended = attended
        new_conducted = conducted

        while (new_attended / new_conducted) * 100 < target and future < 1000:
            future += 1
            new_conducted += 1

            # Simulate future attendance pattern
            if rate == 100:
                new_attended += 1
            elif rate == 90 and future % 10 != 0:
                new_attended += 1
            elif rate == 75 and future % 4 != 0:
                new_attended += 1

        if (new_attended / new_conducted) * 100 >= target:
            print("At", rate, "% future attendance:",
                  future, "classes required")
        else:
            print("At", rate, "% future attendance:",
                  "Target cannot be reached")
