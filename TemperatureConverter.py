# Fun fact cik: Temperature itu bukan hanya panas dan dingin temperature itu adalah skala rata rata energi kinetic pada vibrasi dan tumbukan antar atom dan molekul

#CELSIUS
print('❄️Celsius Converter🔥')
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_to_reamur(celsius):
    return (celsius * 4/5)
def celsius_to_kelvin(celsius):
    return (celsius + 273)

C = float(input("Celsius Temperature: "))
C_F = celsius_to_fahrenheit(C)
print(f"{C}°C is equal to {C_F}°F")
C_R = celsius_to_reamur(C)
print(f"{C}°C is equal to {C_R}°R")
C_K = celsius_to_kelvin(C)
print(f"{C}°C is equal to {C_K}°K")

#FAHRENHEIT
print('\n🔥Fahrenheit Converter❄️')
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * 5/9
def fahrenheit_to_reamur(fahrenheit):
    return (fahrenheit - 32) * 4/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

F = float(input("Fahrenheit Temperature: "))
F_C = fahrenheit_to_celsius(F)
print(f"{F}°F is equal to {F_C}°C")
F_R = fahrenheit_to_reamur(F)
print(f"{F}°F is equal to {F_R}°R")
F_K = fahrenheit_to_kelvin(F)
print(f"{F}°F is equal to {F_K}°K")

#REAMUR
print('\n❄️Reamur Converter🔥')
def reamur_to_celcius(reamur):
    return (reamur * 5/4)
def reamur_to_fahrenheit(reamur):
    return (reamur * 9/4) + 32
def reamur_to_kelvin(reamur):
    return (reamur * 5/4) + 273.15

R = float(input("Reamur Temperature: "))
R_C = reamur_to_celcius(R)
print(f"{R}°R is equal to {R_C}°C")
R_F = reamur_to_fahrenheit(R)
print(f"{R}°R is equal to {R_F}°F")
R_K = reamur_to_kelvin(R)
print(f"{R}°R is equal to {R_K}°K")

#KELVIN
print('\n🔥Kelvin Converter❄️')
def kelvin_to_celcius(kelvin):
    return (kelvin - 273.5)
def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67
def kelvin_to_reamur(kelvin):
    return (kelvin - 273.15) * 4/5

K = float(input("Kelvin Temperature: "))
K_C = kelvin_to_celcius(K)
print(f"{K}°K is equal to {K_C}°C")
K_F = reamur_to_fahrenheit(K)
print(f"{K}°K is equal to {K_F}°F")
K_R = reamur_to_kelvin(K)
print(f"{K}°K is equal to {K_R}°R")
