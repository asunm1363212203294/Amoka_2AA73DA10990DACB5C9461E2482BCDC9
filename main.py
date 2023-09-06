#Unit -I Challenge
#Factorial of a given number using recursion


def fact(x):
  if x == 0 or x == 1:
    return 1
  else:
    return x * fact(x - 1)


num = int(input("Enter a number:"))
res = fact(num)
print("Factorial of {} is {}.".format(num, res))
