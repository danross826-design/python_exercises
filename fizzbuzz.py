print("Give me a positive integer.")

number = input();

if number.isnumeric() && number >= 1:
  for i in range(1, (int)number + 1):
    if i%3 == 0 and i%5 == 0:
      print("FizzBuzz")  
    elif i%3 == 0:
      print("Fizz")
    elif i%5 == 0:
      print("Buzz")
    else:
      print(i)
else:
  print("That wasn't a positive integer.")
 