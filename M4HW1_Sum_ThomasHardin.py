# This program accepts number and gives an error if the number is negative.
#6/25/2017
#CTI-110 M4HW1-Sum of Numbers
#Thomas P. Hardin
#
#
#Varible init
keep_going = 'y'
total = 0.0
#
#Start of the loop
while keep_going == 'y':
#
#
# Get a number
    number = float(input('Enter a number:  '))
    if number <= 0:
       print('Error:  The number cannot be a negative ')
    else:
     if number > 0:
        total = total + number
        print('The total is' ,  format(total, ',.2f'))
        keep_going = input('Enter y to keep going?  ')
	
    

