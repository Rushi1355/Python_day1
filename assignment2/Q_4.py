year = int(input(f"enter year:"))

def leap_year(a):
    if a % 4 == 0 and(a % 100 != 0 or a % 400 == 0):
        return (f"{year} is leap year")
    
    else:
        return (f"{year} is not leap year") 
        
result = leap_year(year)
print(f"{result}")

#1992  2000  1900 1995
  
  
 