#!/usr/bin/python3

for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
# print til 9 int to digit expl"01"
    else:
        print("{:02}".format(i), end=', ')
