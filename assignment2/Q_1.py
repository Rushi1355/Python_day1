numbers = []
for i in range(5):
    num = int(input(f"enter 5 digit {i + 1}:"))
    numbers.append(num)

def cube(n):
         """make a cube of number"""
         return n ** 3
temp = 0
for num in numbers:
    temp += cube(num)





print(f"addition of cubes of provided numbers = {(temp)}")

