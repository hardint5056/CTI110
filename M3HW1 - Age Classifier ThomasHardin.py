#6/15/17
#CTI-110-M3HW1 - Age Classifier
#Thomas Hardin
#
print ("This program will compare a persons" +
       "and display what their age clissification is\.")
Persons_age = float(input("Enter the Person age: "))
if  Persons_age <= 1:  
    print ("This person is an infant")
else:
 if  Persons_age == 1 or Persons_age <=12:
   print ("This person is an child")
 else:
  if  Persons_age == 13 or Persons_age <=20:
       print ("This person is an teenager")
  else:
    if Persons_age == 20 or Persons_age > 20:
        print ("This person is an adult")
				
				
 
	
