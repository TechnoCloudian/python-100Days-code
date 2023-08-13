# Uncomment what you want to RUN
print ('"I love to learn coding, and these are my personal notes from the lectures"\n')
#print ('123 \n') # print the string

#define two variables, sum them, and prin the result
#a = 20
#b = 30
#c = a + b
#print (c)

#x = 7.5
#y = 12.5
#z = x + y
#print (z)

#num = input('insert something \n')
#print ("you entered " + num)
#print (type(num))  # type() function shows the type of the data. 

# converting data type with functions
#a = 30
#print (type(a))
#print (a)


#b = str(a) #now the data stored in b will be a string
#print (type(b))
#print (b)
#word = input('something ')
#type(word)
#new_word = type(str(word))
#print (new_word)

#print (70 + float("100.5"))
#print (200 + int("100"))
#print (str(20) + str(20))


#two_digit_number = input("Type a two digit number: ")

# This program take the two number as input, and then add then like 39 -> 3+9 =12
#num1 = two_digit_number[0]  # we can subcript str only, so here we store the first number in a new variable

#num2 = two_digit_number[1]

#a = int(num1)    # Here we convert the new variable from str to int. 
#b = int(num2)

#print (a+b)
# we can do it either way, like above or below
#sum = int(num1) + int(num2)
#print (sum)
#print (int(num1) + int(num2))

#print (3*3+3/3-3)   #PEMDAS-LR rule-> [Parnentheses, exponent, Multiplication, division, addition, subraction -> from left to right]
#print (3/3 * 3 - 3 +3)

# BMI calculator    (BMI = weight/height**2)

#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")

#height = float(height)
#weight = float(weight)  # weight = int(weight)
#bmi    = int(weight / (height ** 2)) # if we want the result to be integer/float
#print (bmi)

# round () function is used to round the result to a nearst or some point in a decimal digit system, like 2-3 decimal points;
#print (round(8/3)) # here the result of 8/3 is rounded to 3 instead of 2.6666. 
#print (round(8/3, 2)) #here we round the number to two decimal point as 2.67 instead of 2.66666 or 3. 

#print (8//3) #Here we use flow-division, where the result is integer but not rounded, as it will neglect anything after the decimal.

#result = 8//2
#result /= 2
#print (result)    

# we can use +=, /=, -= etc to treat that number or result. 
score = 0

#score = score +1 # increment by 1, and can be simplified as bellow,
#score += 1     # Here it function same as above. 
#print (score)
#print ("Your score is " + str(score))
# F-string- f"xxxxxx {}" is another great function which simplifies the conversion of data, as we have seen in the above examples, so if we have many different data types, we don't need to convert them one by one to print it as a string. see below;
#print (f"your score is {score}")
# Now let say we have many different type of data types; 
#name = input("Please enter your name: ")
#age = input("Please enter your age in years: ")  # age in years
#height = input("please enter your height in meters: ") #height in meters
#weight = input ("Please enter your weight in kg: ") # weight in Kg
#weight = float(weight)
#height = float(height)
#BMI = int(weight / (height ** 2))
#print (f"Hey {name},your age is {age} years, and height is {height} meters, while your weight is {weight} kg")
#print (f"Your BMI is {BMI}")
# 🚨
#age = input("What is your current age? ")
# 🚨 
#age = int(age) #convert the input string to float or int. 
#fix_age = 90     # this is a given age, if we would live this long
#left_age = (90 - age) # remaing age in years
#days = int(left_age * 365) # in days
#weeks = int(left_age * 52)  # in weeks
#months = int(left_age * 12)  # in months
#print (f"You have {days} days, {weeks} weeks, and {months} months left")

#🚨 DAY2 Project
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print ("Welcome to the TIP calculator")
guest = input("How many guest are there?\n ")
bill = input ("How much is the actual bill? \n")
tip = input ("How much you want to pay in tip-percentage? \n")
guest = int(guest)
bill = float(bill)
tip = float(tip)
tip_per = (tip / 100)

total_bill_tip = (bill * tip_per)
final_bill = bill + total_bill_tip
payment_person = round(final_bill / guest, 2)
print (f"Each person should pay {payment_person}") 
