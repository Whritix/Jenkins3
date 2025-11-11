import sys

if len(sys.argv) == 8:
    script_name = sys.argv[0]
    name = sys.argv[1]
    rollno = sys.argv[2]
    mark1 = sys.argv[3]
    mark2 = sys.argv[4]
    mark3= sys.argv[5]
    mark4 = sys.argv[6]
    mark5 = sys.argv[7]
    print("User provided input values:")
else:
    name = "Aditya"
    rollno = "43"
    mark1 = "50"
    mark2 = "50"
    mark3= "50"
    mark4 = "50"
    mark5 = "50"
    print("No input given, using default values:")

total = int(mark1) + int(mark2) + int(mark3) + int(mark4) + int(mark5)
average = total / 5 

print(" Name:", name)
print("Rollno:", rollno)
print("Subject 1 marks :", mark1)
print("Subject 2 marks :", mark2)
print("Subject 3 marks :", mark3)
print("Subject 4 marks :", mark4)
print("Subject 5 marks :", mark5)
print("Total Marks:", total)
print("Average Marks:", average)

if (total > 400):
    print(" Grade: A")
elif (total > 300):
    print(" Grade: B")
elif (total > 200):
    print(" Grade: C")  
else:
    print(" Grade: F")