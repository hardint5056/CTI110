
#Debugging A program
#6/16/17
#CTI-110 M3T2_Debugging
#Thomas Hardin
#
#Corrected code i.e. debugged code.
print('This Program has several nested if-else statements. That need to be properly aligned.')
#Need to set some varibles to test the Boolean.
A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50
#Accept input from the keyboard
score = int(input('Enter your test score.'))
if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
         if score >= C_score:
            print('Your grade is C.')
         else:
             if score >= D_score:
                 print('Your grade is D.')
             else:
                  if score >= F_score:
                      print('Your grade is F.')
	
	
