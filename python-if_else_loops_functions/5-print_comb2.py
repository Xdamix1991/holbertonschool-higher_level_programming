#!/usr/bin/python3
for i in range(0, 100):
    #print til 9 int to digit expl"01"
    if i < 10:
        print(f"0{i}",end=', ' if i < 9 else'')

    else:
        print(i, end=', ' if i < 99 else '\n')

