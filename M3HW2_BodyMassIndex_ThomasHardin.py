#Measure a persons Body Max Index "BMI" 
#6/16/17
#CTI-110  M3HW2 Body Mass Index
#Thomas Hardin
#
print ("This program will calculate a persons" + \
          "Body Max Index and display it\.")
#Varible to use for the converion
your_weight	=	float(input("Enter the your weight in pounds: "))
your_height	=	float(input("Enter the your height in inches: "))
your_BMI = your_weight * 703 / your_height**2
if your_BMI < 18.5: 
    print("Your BMI is your_BMI")
	print("You are underweight!")
else:
