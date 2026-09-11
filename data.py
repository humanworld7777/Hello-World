import csv
import os
print(f"Searching for CSV in{os.getcwd()}")

roll_input = input("Enter a Roll Number: ").strip()
found = False
try:
  with open('students.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader,None)
    for row in reader:
      if row and row[0].strip() == roll_input:
        print(f"\nName  : {row[1].strip()}")
        print(f"Grade : {row[2].strip()}")
        print(f"Age   : {row[3].strip()}")
        found = True
        break
  if not found:
    print("Student not found.")

except FileNotFoundError:
  print("\n[Error] 'students.csv' was not found in this directory.")
