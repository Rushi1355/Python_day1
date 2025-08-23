#num = int(input("enter 4 digit number:"))
num = 1234
num2 = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev *10 + digit
    num = num // 10

print(f"original_number is = {num2}")
print(f"reverce_number is = {rev}")
