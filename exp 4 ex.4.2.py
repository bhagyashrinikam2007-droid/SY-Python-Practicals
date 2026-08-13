status = input("Enter atmospheric status (hot/cold/normal):").lower()
if status == "hot":
    print("Recommendation: Turn on AC.")

elif status == "cold":
    print("Recommendation: Activate heater.")

elif status == "normal":
    print("Recommendation: System is idle.")

else:
    print("Invalid status. Enter hot, cold, or normal")