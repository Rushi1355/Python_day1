#num = int(input("Enter a number: "))
num = 9345

num_str = str(num)     # convert to string to loop over digits
length = len(num_str)

terms = []  # to collect each expanded value

for i in range(length):
    digit = int(num_str[i])
    place_value = digit * (10 ** (length - i - 1))
    if place_value != 0:    # skip zeros
        terms.append(str(place_value))

# Join terms with " + "
expansion = " + ".join(terms)

print(f"{num} = {expansion}")

