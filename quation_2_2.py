f = float(input("enter a temprature to convert in celcious:"))

def Fahrenheit_to_celcious(f):
    return (f - 32) * 5/9

result = Fahrenheit_to_celcious(f)
print(f"IN_celsious = {result}")