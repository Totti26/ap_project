'''
def conv_types():
    print('1) Length')
    print('2) Time')
    print('3) Temperature')
    print('4) Mass')
'''
#dist conversions
def dist_conv():
    print('1) Mi to Km')
    print('2) Km to Mi')
    print('3) Cm to In')
    print('4) In to Cm')

def mi_to_km():
    mi = float(input('Enter mi: '))
    km = mi * 1.60934
    print(f'{mi} mi = {round(km,2)}km')

def km_to_mi():
    km = float(input('Enter km: '))
    mi = km / 1.60934
    print(f'{km} km = {round(mi,2)}mi')

def cm_to_in():
    cm = float(input('Enter cm: '))
    inch = cm * 0.393701  
    print(f'{cm} cm = {round(inch,2)}in')

def in_to_cm():
    inch = float(input('Enter in: '))
    cm = inch / 0.393701
    print(f'{inch} in = {round(cm,2)}cm')

def mi_to_in():
    mile = float(input('Enter mi: '))
    inch = mile / 63360
    print(f'{mile} mi = {round(inch,2)}in')

def in_to_mi():
    inch = float(input('Enter in: '))
    mi = inch * 1.57828e-5
    print(f'{inch} in = {round(mi,2)}mi')


#game loop
while True:    
    dist_conv()
    user_choice = input('Which conversion would you like to do?(enter #): ')
    print(user_choice)
    
    if user_choice =='1':
        mi_to_km()
    if user_choice =='2':
        km_to_mi()
    if user_choice == '3':
        cm_to_in()
    if user_choice == '4':
        in_to_cm()
    
    if input('Would you like to make another conversion? (y/n): ') != 'y':
        break
