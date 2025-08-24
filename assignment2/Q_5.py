calls = int(input("enter number of calls:"))

def price_per_call(a,r=2):
        if a <= 0:
                print("'OOPS ERROR,'enter valid number of calls")
        elif a <= 100:    
                return a * r
        elif 100 < a <=150:
                r = r + 0.6
                return a * r
        elif 150 < a <= 200:
                r = r + 0.5
                return a * r
        elif 200 < a:
                r = r + 0.4
                return a * r
        
result = price_per_call(calls)
print(f"total Rs.{result}")
        
             
