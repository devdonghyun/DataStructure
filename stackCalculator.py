class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def get_token_list(expr):
    token_list = []

    operstack = Stack()
    for token_s in expr:
        if token_s in '+-/*^()':
            if operstack.isEmpty():
                token_list.append(token_s)
            else:
                temp_list = []
                while (not operstack.isEmpty()):
                    temp_list.append(operstack.pop())
                temp_list.reverse()
                token_list.append(''.join(temp_list))
                token_list.append(token_s)
        elif token_s == ' ':
            continue
        else:
            operstack.push(token_s)

    if not operstack.isEmpty():
        temp_list = []
        while (not operstack.isEmpty()):
            temp_list.append(operstack.pop())
        temp_list.reverse()
        token_list.append(''.join(temp_list))
    print(token_list)
    return token_list


def infix_to_postfix(token_list):
    opstack = Stack()
    token_list = []

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while (not opstack.isEmpty() and opstack.top() != '('):
                token_list.append(opstack.pop())
            opstack.pop()
        elif token in '+-/*^':
            while (not opstack.isEmpty() and prec[token] <= prec[opstack.top()]):
                token_list.append(opstack.pop())
            opstack.push(token)
        else:  # operand일 때
            token_list.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    # ... ... ...
    while (not opstack.isEmpty()):
        token_list.append(opstack.pop())

    return token_list


def compute_postfix(token_list):
    calstack = Stack()
    for token in token_list:
        if token in '+-*/^':
            second_oper = float(calstack.pop())
            first_oper = float(calstack.pop())
            if token == '+':
                val = first_oper + second_oper
            elif token == '-':
                val = first_oper - second_oper
            elif token == '*':
                val = first_oper * second_oper
            elif token == '/':
                val = first_oper / second_oper
            else:
                val = first_oper ** second_oper
            calstack.push(val)

        else:
            calstack.push(token)
    return calstack.pop()


    # 아래 세 줄은 수정하지 말 것!
expr = input()
value = infix_to_postfix(get_token_list(expr))
# value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
