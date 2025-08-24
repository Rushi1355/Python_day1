quatntity = int(input(f"enter the quatity:"))


def calcute_price(a,r = 5):
    
    if a <= 0:
        print("'OOPS ERROR,'enter valid quantity")
    elif a < 30:
        return (f"{r * a } \nis final price")
    elif 30 <= a < 50 :
        return (f"{r * a * (1 - 0.10)} \napplies 10 % discount")
    
    elif a >= 50:
        return  (f"{r * a * (1 - 0.15)} \napplies 15 % discount")
    


result = calcute_price(quatntity)
print(f"price for {quatntity} quantity is {result}")



