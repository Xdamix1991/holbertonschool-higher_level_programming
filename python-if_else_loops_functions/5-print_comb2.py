#!/usr/bin/python3
for i in range(0, 100):
    #print til 9 int to digit expl"01"
    if i < 99:
        print("{:02}".format(i), end=', ')

    else:
        print("{}".format(i))

