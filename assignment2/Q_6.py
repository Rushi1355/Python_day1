sub1 = int(input(f"Enter marks in 1st subject: "))
sub2 = int(input(f"Enter marks in 2nd subject: "))
sub3 = int(input(f"Enter marks in 3rd subject: "))
#print(f"{type(sub1)}")
def average(a,b,c):
    return (a + b + c)/3

result = average(sub1,sub2,sub3)
if 90 <= result <= 100:
    print(f"Grade A")
elif 80 <= result < 90:
    print(f"Grade B")
elif 70 <= result < 80:
    print(f"Grade C")
elif 60 <= result < 70:
    print(f"Grade D")
elif 0 <= result < 60:
    print(f"Grade F")
