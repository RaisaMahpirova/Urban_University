def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '+':
        print(f'{operand_1} + {operand_2} = {operand_1 + operand_2}')
    elif operation == '-':
        print(f'{operand_1} - {operand_2} = {operand_1 - operand_2}')
    elif operation == '*':
        print(f'{operand_1} * {operand_2} = {operand_1 * operand_2}')
    elif operation == '/':
        print(f'{operand_1} / {operand_2} = {operand_1 / operand_2}')
    elif operation == '//':
        print(f'{operand_1} // {operand_2} = {operand_1 // operand_2}')
    elif operation == '%':
        print(f'{operand_1} % {operand_2} = {operand_1 % operand_2}')


with open('calc.txt', 'r') as file:
    cnt = 0
    for lines in file:
        cnt += 1
        try:
            calc(lines)
        except ValueError as exp:
            if 'unpack' in exp.args[0]:
                print(f'Ошибка в строке {cnt}, недостаточно данных для расшифровки : {lines[:-1]}')
            else:
                print(f'Ошибка в строке {cnt}, неверный формат данных : {lines[:-1]}')
