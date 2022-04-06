class FormulaError(Exception): pass
def parse_input(user_input):
  input_list = user_input.split()
  if len(input_list) != 3:
    raise FormulaError('Input does not consist of three elements')
  number1, op, number2 = input_list
  try:
    number1 = float(number1)
    number2 = float(number2)
  except ValueError:
    raise FormulaError('The first and third input value must be numbers')
  return number1, op, number2
def cal(number1, op, number2):
  if op == '+':
    return number1 + number2
  if op == '-':
    return number1 - number2
  if op == '*':
    return number1 * number2
  if op == '/':
    return number1 / number2
  raise FormulaError('{0} is not a valid operator'.format(op))
while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  number1, op, number2 = parse_input(user_input)
  result = cal(number1, op, number2)
  print(result)