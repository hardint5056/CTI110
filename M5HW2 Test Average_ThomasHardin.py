#Test Average and Grade
#7/12/17
#CTI-110 M5HW2 Test Average 
#Thomas Hardin
#
def calc_average():
            # Open a file for writing.
            outfile = open('numbers.txt', 'w')
            # Initilize my variables
			
            total = 0.0
            A_score = 90
            B_score = 80
            C_score = 70
            D_score = 60
            F_score = 50
            
            # Get five numbers from the user.
            num1 = int(input('Enter a test_score: '))
            num2 = int(input('Enter a test_score: '))
            num3 = int(input('Enter a test_score: '))
            num4 = int(input('Enter a test_score: '))
            num5 = int(input('Enter a test_score: '))
			
            #calculate the average
            total = total +  num1 + num2 + num3 + num4 + num5
            total = total /5
            print('This is your average. ', total)
            
            # Do comparision to see what the grade 
            # average is
            if total >= A_score:
                    print('Your grade is A.')
            else:
                    if total >= B_score:
                            print('Your grade is B.')
                    else:
                            if total >= C_score:
                                    print('Your grade is C.')
                            else:
                                    if total >= D_score:
                                            print('Your grade is D.')
                                    else:
                                          if total >= F_score:
                                              print('Your grade is F.')                         
            
            
calc_average()	
	
	
	
	
