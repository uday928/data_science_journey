def simple_interest_cal(principal, rate, time):
    si=principal*rate*time/100
    return si,principal+si

principal=int(input("Enter principle amount: "))
rate=float(input("Enter rate of interest: "))
time=int(input("Enter time in years: "))

si,total=simple_interest_cal(principal,rate,time)
print(si,total)
