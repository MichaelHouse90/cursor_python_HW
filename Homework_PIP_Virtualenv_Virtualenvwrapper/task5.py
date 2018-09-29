# Write a function that prints numbers from 1 to 30. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

def funcFizzBuzz():

  list = []
  for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
      list.append("FizzBuzz")
    elif i % 3 == 0:
      list.append("Fizz")
    elif i % 5 == 0:
      list.append("Buzz")
    else:
      list.append(str(i))
  print(list)

funcFizzBuzz()
