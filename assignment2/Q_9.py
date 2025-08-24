p = int(input(f"enter principal amount: "))
r = float(input(f"enter rate amount: "))
n = float(input(f"enter number of year amount: "))

def simple_interest(n, p ,r):
    return (n * p * r)/100

result = simple_interest(p,n,r)
print(f"simple interesterst is {result}")