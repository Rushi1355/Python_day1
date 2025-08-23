num = int(input("Enter a number: "))
num_str = str(num)   # ✅ define num_str first
length = len(num_str)

for i in range(length):
    digit = int(num_str[i])   # now num_str is defined
    face_value = str(digit)
    print(f"{int(face_value[::-1])}")
