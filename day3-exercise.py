#Day-3 Notes and palying around the code
print ("'Welcome'! I love to learn, how to code \n")
#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#if height >= 120:
 # print ("You can ride the roalercoaster :D")
#else:
 # print ("Sorry you can't ride, bcz you are smaller")

# exercise to calculate if a number is even or odd
#number = int(input("Which number do you want to check? "))

#if number % 2 == 0:     # this is the mathematical formula so if there isn't any remainder (or 0), the number is even else odd
 #   print ("This is an even number")
#else:
 #   print ("This is an odd number")

# if-elif-else statement exercise. based on height it will decide if rollercoaster can be ride or not and based on age ticket price.
age = int(input("Please enter your age: "))
height = int(input("Please enter your height in centimeters: "))
if height >= 120:
  print ("You can ride the rollercoaster hurrah :D")
  if age <= 11:
    print ("Please pay $5 for your ticket")
  elif age <= 18:
    print ("Please pay $ 8 as your ticket")
  else:
    print ("Please pay full price of $ 15")
else:
  print ("Sorry!! Your height is smaller, You can't ride! ")
## BMI calculator 2.3 code challange.
# Notice here if we are checking the same condition, we follow as this, if we are check two different condition see above example, where we use nested if-else.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round (weight/height ** 2)
if bmi < 18.5:   
    print (f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print (f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print (f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
   
else:
    print (f"Your BMI is {bmi}, you are clinically obese.")
