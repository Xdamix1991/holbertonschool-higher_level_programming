#!/usr/bin/python3
import sys


result = 0
for arg in range(1, len(sys.argv)):
    number = int(sys.argv[arg])
    result += number
print(result)

if __name__ == "__main__":
    pass
