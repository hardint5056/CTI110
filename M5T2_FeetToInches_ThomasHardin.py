#This program will convert feet into inches
#6/29/17
#CTI-110-M5T2 - feet to inches Converter
#Thomas Hardin
#
print ("This program will convert feet to inches" )
       
length_in_feet = float(input("Enter the distance in feet: "))
length_in_feet = length_in_feet * 12
print("The length in inches is:", format(length_in_feet,  ',.2f'))
	
