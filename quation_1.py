length = int(input("enter length:"))
breadth = int(input("enter breadth: "))

def area(num1,num2):
    return length * breadth

def perimeter(num1,num2):
    return 2 * (num1 + num2)

result1 = area(length,breadth)
result2 = perimeter(length,breadth)
print(f"area = {result1}")
print(f"perimeter = {result2}")
