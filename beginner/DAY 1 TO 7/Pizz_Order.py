print("Thank you for choosing Python Pizza Deliveries!")
size = input("Enter Your Pizz size : ") 
add_pepperoni = input("Are You Want Extra pepperoni : ") 
extra_cheese = input("Are you Want Extra Cheese, (It Will charge $1) ") 
Bill = 0
total_Bill = 0
if size == "S":
  Bill = 15
  if  add_pepperoni == "Y":
    total_Bill = Bill + 2
  else:
    total_Bill = Bill
  if extra_cheese == "Y":
    total_Bill = total_Bill + 1
  else:
    total_Bill = total_Bill
elif size == "M":
  Bill = 20
  if  add_pepperoni == "Y":
    total_Bill = Bill + 3
  else:
    total_Bill = Bill
  if extra_cheese == "Y":
    total_Bill = total_Bill + 1
  else:
    total_Bill = total_Bill
elif size == "L":
  Bill = 25
  if  add_pepperoni == "Y":
    total_Bill = Bill + 3
  else:
    total_Bill = Bill
  if extra_cheese == "Y":
    total_Bill = total_Bill + 1
  else:
    total_Bill = total_Bill
else:
  print(input)
print(f"Your Total Bill is ${total_Bill}")