print("welcome to BMi calculator")

height = float(input("Enter Your height "))
weight = float(input("Enter Your Weight(Kg) "))

bmi = weight / (height * height)
print(bmi)

if bmi<18.5:
    print("You are Under weight")
elif bmi<25:
    print("Your weight is normal")
elif bmi<30:
    print("you are over weight")
else:
    print("Your are Obesity")