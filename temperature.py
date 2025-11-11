import sys

if len(sys.argv) >= 2:
    script_name = sys.argv[0]
    temp = float(sys.argv[1])
else:
    temp = 25.0

if temp < 15:
    print("cold")
elif temp <= 30:
    print("normal")
else:
    print("hot")