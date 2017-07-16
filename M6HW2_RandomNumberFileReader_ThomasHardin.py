# This program reads all of the values in the
# selected file
# 07/13/2017 
# CTI-110 M6HW1 - Random Number File Reader
# Thomas Hardin
#
def main():
        total = 0.0
        try:
                infile = open('numbers.txt', 'r')

                for line in infile:
                    number = float(line)
                    total += number
                    num_lines = sum(1 for line in open('numbers.txt'))
                infile.close()
        except Exception as err:
             
                print(err)
        else:
                print('total of the numbers:' , total)
                print('total lines:', num_lines)
main()		
	
