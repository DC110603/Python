""""Write a program to perform given tasks
Declare & initialize a number.
Check whether the number is in range 0-100 or not.
If not in range print INVALID INPUT
Else – if the number is in range 91-100 then print SUPER SMART,
81-90 print SMART,
71-80 print SMART ENOUGH,
61-70 print JUST SMART,
36-60 print NO SMART,
0-35 print DUMB."""
s=int(input("Enter your marks: "))
if s>=0 and s<=100:
    if s<=100 and s>91:
        print("Super Smart")
    elif s<=90 and s>81:
        print("Smart")
    elif s<=80 and s>71:
        print("Smart Enough")
    elif s<=70 and s>61:
        print("Just Smart")
    elif s<=60 and s>36:
        print("No Smart")
    else:
        print("Dumb")
else:
    print("Invalid Input")