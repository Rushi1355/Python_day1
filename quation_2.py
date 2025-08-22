c = float(input("enter the °c temprature to convert:"))

def Celsius_to_Fahrenheit(c):
    return (c * 9/5) + 32

in_Fahrenheit = Celsius_to_Fahrenheit(c) 
print(f"in_Fahrenheit = {in_Fahrenheit}")
