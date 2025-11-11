import sys

if len(sys.argv) == 3:
    name = sys.argv[0]
    rollno = sys.argv[1]
    mark1 = sys.argv[2]
    mark2 = sys.argv[3]
    mark3= sys.argv[4]
    mark4 = sys.argv[5]
    mark5 = sys.argv[6]
    print("User provided input values:")
else:
    name = "Srujan"
    rollno = "42"
    mark1 = "35"
    mark2 = "35"
    mark3= "35"
    mark4 = "35"
    mark5 = "35"
    print("No input given, using default values:")

print(" Name:", name)
print("Student Name:", name)
print("Roll Number:", rollno)