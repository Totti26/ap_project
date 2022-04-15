'''
def conv_types():
    print('1) Length')
    print('2) Time')
    print('3) Temperature')
    print('4) Mass')
'''
#dist conversions
distConversions = {
    "meter-meter": 1,
    "mile-meter": 1609.34,
    "inch-meter": 0.0254,
    "kilometer-meter": 1000,
    "centimeter-meter": 0.01,
    "foot-meter": 0.3048,
    "millimeter-meter": 0.001,
    "yard-meter":0.9144
}

def convert(input1, currentUnits, outputUnits):
    return input1 * distConversions[f"{currentUnits}-meter"] / distConversions[f"{outputUnits}-meter"]


#time conversions
timeConversions = {
    "minute-minute": 1,
    "second-minute": 0.0166667,
    "millisecond-minute": 1.66667e-5,
    "hour-minute": 60,
    "microsecond-minute": 1.66667e-8,
    "decasecond-minute": 0.166667   
}

def convert(input1, currentUnits, outputUnits):
    return input1 * timeConversions[f"{currentUnits}-minute"] / timeConversions[f"{outputUnits}-minute"]



#game loop
while True:    
    currentUnits = input('Which type of unit would you like to convert?: ')
    outputUnits = input('what would you like to convert to?: ')
    input1 = float(input(f'Enter {currentUnits}: '))
    
    print(convert(input1, currentUnits, outputUnits))
    
    if input('Would you like to make another conversion? (y/n): ') != 'y':
        break
