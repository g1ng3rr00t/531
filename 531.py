#!/usr/bin/env python3

## https://stackoverflow.com/questions/2272149/round-to-5-or-other-number-in-python
def myround(x, base=5):
    return(base * round(x/base))

bench = 0.9 * int(input("[+] Max Bench?: "))
squat = 0.9 * int(input("[+] Max Squat?: "))
deadlift = 0.9 * int(input("[+] Max Deadlift?: "))
overhead_press = 0.9 * int(input("[+] Max Overhead Press?: "))

print("\n")

lifts = {"bench" : bench, "squat" : squat, "deadlift" : deadlift, "overhead_press" : overhead_press}

week_1 = (1, 0.65,0.75,0.85)
week_2 = (2, 0.7,0.8,0.9)
week_3 = (3, 0.75,0.85,0.95)

weeks = [week_1, week_2, week_3]

## Main loop

for i in weeks:
    print("[*] Week {}".format(i[0]))

    ## Iterate on lifts
    for j in lifts:
        weight = lifts[j]
        attempts = [str(myround(weight * i[1])),str(myround(weight * i[2])), str(myround(weight * i[3]))]
        print("[-] {} {}".format(j,"/".join(attempts)))
    print("\n")
