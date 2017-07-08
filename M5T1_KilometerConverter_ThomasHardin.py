# This program converts kilometers into miles.
print('This program will convert kilometers to miles')
def main():
    distance_kilo = float(input("Enter the distance in kilometers: "))
    distance_kilo = distance_kilo * 0.6214
    print("The distance traveled in miles is:", format(distance_kilo,  ',.2f'))
main()
