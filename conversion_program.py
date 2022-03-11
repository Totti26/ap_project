#conversion prog, will be able to convert weight, distace, time

def dist_conversion():
    print('1) Mi to Km')
    print('2) Km to Mi')

def mi_to_km():
    mi = float(input('Enter mi: '))
    km = mi * 1.60934
    print(f'{mi} mi = {round(km,2)}km')

def km_to_mi():
    km = float(input('Enter km: '))
    mi = km / 1.60934
    print(f'{km} km: {round(mi,2)}mi')

    
conversion_options()
user_choice = input('Which conversion would you like to do(enter #)? ')


if user_choice =='1':
    mi_to_km()
if user_choice =='2':
    km_to_mi()
