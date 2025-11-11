import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    temp = sys.argv[1]
    
else:
    temp = '25'
    
if temp<15:
    print("Cold Weather")
    
elif temp<=30:
    print("Normal Weather")
else:   
    print("Hot Weather")
    
        