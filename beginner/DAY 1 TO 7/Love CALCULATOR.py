print("The Love CALCULATOR is calculating your score...")
name1 = input()
name2 = input() 
combined_name = name1 + name2
Lower_names = combined_name.lower()
t = Lower_names.count("t")
r = Lower_names.count("r")
u = Lower_names.count("u")
e = Lower_names.count("e")

first_letter = t + r + u + e

l = Lower_names.count("l")
o = Lower_names.count("o")
v = Lower_names.count("v")
e = Lower_names.count("e")

second_leeter = l + o + v + e

score = str(first_letter) + str(second_leeter)
score = int(score)
if score <10 or score>90:
  print(f"Your score is {score} %, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score} %, you are alright together.")
else:
  print(f"Your score is {score} %.")