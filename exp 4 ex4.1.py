status = input("Enter order status(pending/shipped/delivered):").lower()

if status == "pending":
    print("Your order is being processed. Please wait for dispatch.")
    
elif status =="shipped":
    print("Your order has been shipped and is on the way.")

elif status == "delivered":
    print("Yous order has been successfully delivered.")
    print("Thankyou for shopping")

else:
    print("Invalid status. Please enter pending, shipping, or delivered.")