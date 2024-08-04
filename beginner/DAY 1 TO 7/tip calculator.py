print("Welcome to tip caculator")

Bill = float(input("Enter Your Bill price $ "))
person = int(input("How many members are you? "))
tip = int(input("How many persentage you want to tip "))

tip_pesentage = (Bill*tip/100)
amount_pay = round((tip_pesentage+Bill)/person , 2)

print(amount_pay)