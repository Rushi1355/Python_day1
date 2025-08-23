"""write a code for max of three numbers"""
#numbers = []

#for i in range(3):
#    num  = int(input(f"enter three numbers of list {i+1}: "))
#    numbers.append(num)
#result1 = max(numbers)

num1 = int(input(f"enter number 1: "))
num2 = int(input(f"enter number 2: "))
num3 = int(input(f"enter number 3: "))


def max_of_three(a,b,c):
    """finding maximum number """
    if a > b and a > c:
        return (f"maximum numbr is {a} ")
    elif a < b and b > c:
        return (f"maximum numbr is {b}")
    else:
        return (f"maximum numbr is {c}")
    
result = max_of_three(num1,num2,num3)
print(f"{result}")

