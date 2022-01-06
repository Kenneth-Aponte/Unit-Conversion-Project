# Filename: AponteKenneth_016_p1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: Kenneth R. Aponte Mendez
# STUDENT ID: 802 19 9075
# SECTION: 016
############      DEFINE CONSTANTS BELOW      ############
KILOMETERS_PER_MILE = 1.60934
MILES_PER_KILOMETER = 0.621371
KILOGRAMS_PER_POUND = 0.453592
POUNDS_PER_KILOGRAM = 2.20462
KMH_PER_MPH = 1.60934
MPH_PER_KMH = 1.60934

############       ADD YOUR CODE BELOW        ############

def convert_miles_to_kilometers():
    miles = input("Enter the miles to be converted: ")
    if is_float(miles) and float(miles) >= 0:
        # Convert string to numeric miles
        miles = float(miles)
        # Conversion should be rounded to 2 decimal places.
        km =  round(miles * KILOMETERS_PER_MILE, 2)
        print(miles, "miles are equivalent to", km, "kilometers")
    else:
        print("Illegal unit of conversion. Input miles is not a number.")


def convert_kilometers_to_miles():
    km = input('Enter the kilometers to be converted: ')
    if is_float(km) and float(km) >= 0:
        km = float(km)
        miles = round(km * MILES_PER_KILOMETER, 2)
        print(km, 'kilometers are equivalent to', miles, 'miles')
    else:
        print('Illegal unit of conversion. Input kilometers is not a number.')


def convert_pounds_to_kilograms():
    pounds = input('Enter the pounds to be converted: ')
    if is_float(pounds) and float(pounds) >= 0:
        pounds = float(pounds)
        kg = round(pounds * KILOGRAMS_PER_POUND, 2)
        print(pounds, 'pounds are equivalent to', kg,'kilograms')
    else:
        print('Illeagl unit of convesion. Input pounds is not a number.')


def convert_kilograms_to_pounds():
    kilograms = input('Enter the kilograms to be converted: ')
    if is_float(kilograms) and float(kilograms) >= 0:
        kg = float(kilograms)
        pounds = round(kg * POUNDS_PER_KILOGRAM, 2)
        print(kg, 'kilograms are equivalent to', pounds, 'pounds')
    else:
        print('Illegal unit of conversion. Input kilograms is not a number.')


def convert_celsious_to_fahrenheit():
    celsious = input('Enter the Celsius to be converted: ')
    if is_float(celsious):
        c = float(celsious)
        f = round((c * 9/5) + 32, 2)
        print(c, 'Celsius are equivalent to', f,'Fahrenheit')
    else:
        print('Illegal unit of conversion. Input Celsius is not a number.')


def convert_fahrenheit_to_celsious():
    fahrenheit = input('Enter the Fahrenheit to be converted: ')
    if is_float(fahrenheit):
        f = float(fahrenheit)
        c = round((f - 32) * 5/9, 2)
        print(f, 'Fahrenheit are equivalent to', c, 'Celsius')
    else:
        print('Illegal unit of conversion. Input Fahrenheit is not a number.')


def convert_milesperhour_to_kilometersperhour():
    milesperhour = input('Enter Miles/hour to be converted: ')
    if is_float(milesperhour) and float(milesperhour) >= 0:
        mph = float(milesperhour)
        kmh = round(mph * KMH_PER_MPH, 2)
        print(mph, 'Miles/hour are equivalent to', kmh, 'Kilometer/hour')
    else:
        print('Illegal unit of conversion. Input Miles/hour is not a number.')


def convert_kilometersperhour_to_milesperhour():
    kilometersperhour = input('Enter kilometers/hour to be converted: ')
    if is_float(kilometersperhour) and float(kilometersperhour) >= 0:
        kmh = float(kilometersperhour)
        mph = round(kmh / MPH_PER_KMH, 2)
        print(kmh, 'Kilometers/hour are equivalent to', mph, 'Miles/hour')
    else:
        print('Illegal unit of conversion. Input Kilometers/hour is not a number.')


def process_conversion(numericOption):
    if numericOption == 1:
        convert_miles_to_kilometers()
    # Add code to handle other menu selections.
    elif numericOption == 2:
        convert_kilometers_to_miles()
    elif numericOption == 3:
        convert_pounds_to_kilograms()
    elif numericOption == 4:
        convert_kilograms_to_pounds()
    elif numericOption == 5:
        convert_celsious_to_fahrenheit()
    elif numericOption == 6:
        convert_fahrenheit_to_celsious()
    elif numericOption == 7:
        convert_milesperhour_to_kilometersperhour()
    elif numericOption == 8:
        convert_kilometersperhour_to_milesperhour()



############ DO NOT MODIFY THE SECTION BELOW  ############

def is_float(s):
    try:
        float(s)
        # Return True if no exception is thrown
        return True
    except ValueError:
        return False


def print_program_menu():
    print("\n--------")
    print( "Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Miles/hour to kilometers/hour")
    print("8. Kilometers/hour to miles/hour")
    print("9. Exit")


def identify_option(option):
    # Verify that a number was input
    if option.isdigit():
        numericOption = int(option)
        # Check if the selection is within permitted range
        if numericOption >= 1 and numericOption <= 9:
            return numericOption
        else:
            return -1 # Invalid option
    else:
        return -1 # Invalid option


def main():
    done = False
    while not done:
        print_program_menu()
        userOption = input("Enter option: ")
        optionInfo = identify_option(userOption)
        if optionInfo != -1:
            # Option was valid
            if optionInfo == 9:
                done = True
                print ("Thanks for using the unit conversion program!")
            else:
                process_conversion(optionInfo)
        else:
            # Option was invalid
            print ("Invalid option\n")


# This line makes python start the program from the main function
if __name__ == "__main__":
    main()
