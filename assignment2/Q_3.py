number = int(input(f"enter a number: "))

def compare(number):
    if number > 0:
        return (f"{number} is positive")
    elif number < 0:
        return (f"{number} is negative")
    else:
        return (f"zero")
    
result = compare(number)
print(f"{result}")