"""
Fahrenheit to Celsius Converter
Author: Timothy Shine

This program shows some tested values with their expected values first,
then it gives the user the opportunity to test their own values.
When the user is done with the program, they can type stop and the program will terminate.

"""


def f2c(f):
    """If the input is one of the 6 Craignms train spots it will use the corresponding celsius value to each stop
       if it is not, the formula will be used to calculate the temperature"""
    value = f2c_6train(f)
    if value == -9999:
        return fahrenheit2celsius(f)
    else:
        return value


def fahrenheit2celsius(f):
    """This function will convert fahrenheit degrees into celsius using the formula
       T(C) = [T(F)-32]*5/9"""
    f = (f - 32) * 5 / 9
    return f


def f2c_6train(f):
    """This function checks to see if any of the inputted values correspond to the
       Craignm's 6 Train algorithm. If it doesn't it'll return -9999"""
    if f == 86:
        return 30
    elif f == 77:
        return 25
    elif f == 68:
        return 20
    elif f == 59:
        return 15
    elif f == 50:
        return 10
    elif f == 41:
        return 5
    elif f == 32:
        return 0
    elif f == 23:
        return -5
    elif f == 14:
        return -10
    else:
        return -9999


def is_number(x):
    """Checks to see if any variable x is a number and therefore valid for conversion before executing
        If it is not a number the function returns False
        If it is a value, the function returns it with the correct type (integer or float)"""
    try:
        return float(x)
    except ValueError:
        return False


def test(temperature):
    """Tests the inputted values for validity.
        If the value is a number it'll return a conversion, if it is not, you must try again with valid input"""
    if is_number(temperature) is not False:
        return 'Temperature in Celsius: ' + str(f2c(is_number(temperature)))
    else:
        return "Please Enter Valid Input"


def main():
    """Asks for input from the user for temperature conversion. Continuous loop until user types stop"""
    print("These were the values used to test the program")
    print('Temperature (Fahrenheit) = 12        Calculated : ', test(12), '   Expected (Celcius): -11.1111111')
    print('Temperature (Fahrenheit) = 0         Calculated : ', test('0'), '   Expected (Celcius): -17.7777778')
    print('Temperature (Fahrenheit) = -24       Calculated : ', test('-24'), '   Expected (Celcius): -31.1111111')
    print('Temperature (Fahrenheit) = -10.2     Calculated : ', test(-10.2), '  Expected (Celcius): -23.4444443')
    print('Temperature (Fahrenheit) = -40       Calculated : ', test('-40'), '                  Expected (Celcius): -40')  #these spaces are used for output formatting
    print('Temperature (Fahrenheit) = wrong     Calculated : ', test('wrong'),'                     Expected (Celcius): Please Enter Valid Input') #these spaces are used for output formatting
    print('Temperature (Fahrenheit) = 1.1.2     Calculated : ', test('1.1.2'),'                     Expected (Celcius): Please Enter Valid Input')  # these spaces are used for output formatting
    print('Temperature (Fahrenheit) = 1+2-4     Calculated : ', test('1+2-4'),'                     Expected (Celcius): Please Enter Valid Input')  # these spaces are used for output formatting
    print()
    print("Type stop at any point to end the program, otherwise, feel free to try out your own numbers!")
    print()
    while True:
        temperature = input('Please enter a temperature in Fahrenheit to be converted to Celsius: ')
        if temperature.lower() == 'stop':
            break
        print(test(temperature))


if __name__ == '__main__':
    main()
