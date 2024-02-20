import re

tokens = [
    ('NUMBER', r'\d+(\.\d*)?'),  
    ('PLUS', r'\+'),               
    ('MINUS', r'\-'),              
    ('TIMES', r'\*'),              
    ('DIVIDE', r'\/'),             
    ('LPAREN', r'\('),             
    ('RPAREN', r'\)')              
]

def lexer(expression):
    tokens_list = []
    while expression:
        match = None
        for token in tokens:
            token_type, pattern = token
            regex = re.compile(pattern)
            match = regex.match(expression)
            if match:
                value = match.group(0)
                tokens_list.append((token_type, value))
                expression = expression[len(value):].lstrip()
                break
        if not match:
            raise ValueError('Carácter no válido: ' + expression[0])
    return tokens_list

expresion = "3.5 + 2 * (4 - 2)"
resultado_tokens = lexer(expresion)
print("Tokens generados:", resultado_tokens)