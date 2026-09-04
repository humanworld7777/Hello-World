try:
  numerator = 10 
denominator = int(input("Enter a numberto divide by:"))
result = numerator / denominator

except ZeroDivisionError:
  print("Error: You cannot divide by Zero!")

except ValueError:
    print("Error: Please enter a valid integer!")

else:
  print(f"Sucess! The result is {result}")

finally:
  print("Execution completed.")
  
