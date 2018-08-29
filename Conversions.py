#this program forces the data to print results in a list format
#printing metric conversions in a list
#formatting the data to look like a table
def main():
    miles = [0,0]
    print('miles,','kilometers')
    for mileage in range(-10,100,10):
        miles[0] = mileage #assign position 0 in list as mileage from range
        miles[1] = mileage*1.6 #assign position 1 in list as mileage*1.6
        print(miles) #print for mileage in range -10 to 100
    print()
    print('F,','\t','C')
    temperature = [0,0]
    for f in range(0,100,10): # f stands for fahrenheit temperature
        temperature[0] = f
        temperature[1] =format(((f-32)*5/9),',.2f')
        print(temperature)
    print()
    print('lbs,','kilograms')
    pounds = [0,0]
    for pound in range(0,100,10):
        pounds[0] = pound
        pounds[1] = pound*0.45
        print(pounds)
    print()
    print('Inches, Centimeters')
    inches = [0,0]
    for inch in range(0,100,10):
        inches[0] = inch
        inches[1] = inch*2.54
        print(inches)
    print()
    gallons = [0,0]
    print('Gallons, Liters')
    for gallon in range(0,100,10):
        gallons[0] = gallon
        gallons[1] = gallon*3.9
        print(gallons)
        
    
    
main()
