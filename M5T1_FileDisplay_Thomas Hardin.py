# This program reads all of the values in the
# selected file
# 07/13/2017 
# CTI-110 M5T1_FileDisplay_Thomas Hardin
# Thomas Hardin
#
# This program displays all of the numbers in a file
number_file = open('numbers.txt', 'r')
def main():
        # Read the first line from the file.
        line = number_file.readline()
                       
        # As long as any empty string is not returned
        # from readline, continue processing.
        while line != '':
            line = number_file.readline()
            print('This is the line being processed.', line)
            # Close the file.
        number_file.close()
# Call the main function.         
main()
	
