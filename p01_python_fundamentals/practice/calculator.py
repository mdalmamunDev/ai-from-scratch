"""
Create a calculator that:

Takes two numbers from the user.
Takes an operator: +, -, *, /.
Performs the operation.
Handles division by zero.
Displays the result.

Example:

First number: 20
Operator: *
Second number: 5
Result: 100

"""


def calculate(num1, num2, operator):
  match operator:
    case "+":
      return num1 + num2
    case "-":
      return num1 - num2
    case "*":
      return num1 * num2
    case "/":
      if num2 == 0:
        print("Divided by zero")
        return
      return num1/num2
    case _:
      print("Invalid operator")


num1 = int(input('Enter num_1: '))
num2 = int(input('Enter num_2: '))
op = input("Enter operator: ")

result = calculate(num1, num2, op)
print(f'Result of {num1} {op} {num2} is {result}')