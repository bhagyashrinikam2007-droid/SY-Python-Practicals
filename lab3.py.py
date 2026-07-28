print("Admission Eligibility Check")

age = int(input("Enter age of Student: "))
marks = int(input("Enter marks: "))

if age >= 17 and age <= 25:
    print("Eligible for Admission by age")

    if marks > 60:
        print("Eligible for B.Tech")

        if marks > 85:
            print("Eligible for AIML")
        elif marks > 75:
            print("Eligible for CSE")
        else:
            print("Eligible for Mech, ENTC, Civil")

    else:
        print("Not eligible for B.Tech")

else:
    print("Not eligible for Admission by age")

print("Thank you")