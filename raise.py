def set_age(age):
  if age < 0:

    raise ValueError("Age cannot be negative!")
    print(f"Age set to {age}")


try:
  set_age(-9999)

expect ValueError as error:
 print(f"Caught an error: {error}")
