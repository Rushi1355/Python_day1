P = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of interest: "))

n = float(input("Enter Number of times interest compounds in a year: "))
t = float(input("Enter Number of years: "))

def compound_interest(P, r, n, t):
    
    r = r / 100
    A =  P * (1 + (r / n)) ** (n * t)
    return A - P

result = compound_interest(P, r, n, t)
print(f"Compound interest is {result:.2f}")
