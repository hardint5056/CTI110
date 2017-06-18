#Measure a persons Body Max Index "BMI" 
#6/16/17
#CTI-110  M4HT1 - Bug Collector
#Thomas Hardin
#
print ("This program will keep a running total of the number of bugs collected in 5 days.")
max	=	5		#Maximum number
total	=	0.0 #Initalize the accumulator varible.
#	Get the numbers and accumulate them.
for counter in range(max):
	number = int(input('Enter the number of bugs collected today: ' ))
	total = total + number
# Dispaly the total
print('The total is', format(total, ',.2f'))	
