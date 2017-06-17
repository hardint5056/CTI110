#Area of Rectangles compare two rectangles and determine if they are equal or not.
#Date 6/15/2017
#CTI-110
#Thomas Hardin
#
#
print ("This program will calculate the area " + \
           "of a 2 rectangles and compare to see if one is greater than the other\.")
#Input from the keyboard to calculate the area of the first rectangle
length_rec_1 = int(input("Enter the Length of the first rectangle: "))
height_rec_1 = int(input("Enter the height of the first rectangle: "))
#   
area_rec_1 = length_rec_1 * height_rec_1
#	    
#Input from the keyboard to calculate the area of the second rectangle	
length_rec_2 = int(input("Enter the Length of the second rectangle: "))
height_rec_2 = int(input("Enter the height of the second rectangle: "))
#   
area_rec_2 = length_rec_2 * height_rec_2
#Compare the two rectangles to see if one has greater area than the other or are they the same size
if area_rec_1  ==  area_rec_2:
   print ("The Rectangles are Equal")
   print("The area of Retangle 1 is", format(area_rec_1, ',.2f'))
   print("The area of Retangle 2 is", format(area_rec_2, ',.2f'))
else:
   if area_rec_1  >  area_rec_2:
     print("Rectangle 1 is greater than Rectangle 2")
     print("The area of Retangle 1 is", format(area_rec_1, ',.2f'))
     print("The area of Retangle 2 is", format(area_rec_2, ',.2f'))
   else:
      if area_rec_1 < area_rec_2:
        print("Rectangle 2 is greater than Rectangle 1")
        print("The area of Retangle 1 is", format(area_rec_1, ',.2f'))
        print("The area of Retangle 2 is", format(area_rec_2, ',.2f'))   

	
