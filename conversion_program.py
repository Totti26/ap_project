
'''
def conv_types():
    print('1) Length')
    print('2) Time')
    print('3) Temperature')
    print('4) Weight')
'''

dist = ['meter', 'mile', 'inch', 'kilometer', 'centimeter', 'foot', 'millimeter', 'yard']
time = ['minute', 'second', 'millisecond', 'hour', 'microsecond', 'decasecond']
temp = ['fahrenheit', 'celsius']
weight = ['gram', 'pound', 'kilogram', 'milligram', 'ounce', 'stone', 'microgram', 'US ton', 'metric ton']

#dist conversions
def conv_dist(input1, currentUnits, outputUnits):
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

    return input1 * distConversions[f"{currentUnits}-meter"] / distConversions[f"{outputUnits}-meter"]


#time conversions
def conv_time(input1, currentUnits, outputUnits):
    timeConversions = {
        "minute-minute": 1,
        "second-minute": 0.0166667,
        "millisecond-minute": 1.66667e-5,
        "hour-minute": 60,
        "microsecond-minute": 1.66667e-8,
        "decasecond-minute": 0.166667   
    }

    return input1 * timeConversions[f"{currentUnits}-minute"] / timeConversions[f"{outputUnits}-minute"]


#temp conversions
def conv_temp(input1, currentUnits, outputUnits):
    if currentUnits == 'celsius' and outputUnits == 'fahrenheit':
        return input1 * 9 / 5 + 32
    elif currentUnits == 'fahrenheit' and outputUnits == 'celsius':
        return (input1 - 32) * 5 / 9


#weight conversions
def conv_weight(input1, currentUnits, outputUnits):
    weightConversions = {
        "gram-gram": 1,
        "pound-gram": 453.592,
        "kilogram-gram": 1000,
        "milligram-gram": 0.001,
        "ounce-gram": 28.3495,
        "stone-gram": 6350.29,
        "microgram-gram": 1e-6,
        "US ton-gram": 907185,
        "metric ton-gram": 1e+6   
    }

    return input1 * weightConversions[f"{currentUnits}-gram"] / weightConversions[f"{outputUnits}-gram"]

    

#intro
print(f'''
Hello there, welcome to my conversion program! 
You will be able to convert units of distance {dist}, 
weight {weight}, temperature {temp},
and time {time}.
''')


#game loop
while True:    
    currentUnits = input('Which type of unit would you like to convert?: ')
    outputUnits = input('What would you like to convert to?: ')
    input1 = float(input(f'Enter {currentUnits}: '))
    
    if currentUnits in dist:
        print(conv_dist(input1, currentUnits, outputUnits))
    if currentUnits in time:
        print(conv_time(input1, currentUnits, outputUnits))
    if currentUnits in temp:
        print(conv_temp(input1, currentUnits, outputUnits))
    if currentUnits in weight:
        print(conv_weight(input1, currentUnits, outputUnits))
    else:
        print('sorry, this can not be converted. ')
    
    if input('Would you like to make another conversion? (y/n): ') != 'y':
        break
