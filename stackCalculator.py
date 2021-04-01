class Stack:


def get_token_list(expr):


def infix_to_postfix(token_list):


def compute_postfix(token_list):


    # 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
