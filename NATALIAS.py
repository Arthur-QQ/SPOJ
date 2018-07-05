def get_arguments(functions):
    parenthesis = 0
    functions = functions[4 if functions.startswith('AND') else 3:-1]
    for i in range(len(functions)):
        c = functions[i]
        if c == '(':
            parenthesis += 1
        elif c == ')':
            parenthesis -= 1
        elif parenthesis == 0 and c == ',':
            return (functions[:i], functions[i+1:])
 
def evaluar(expr):
    if len(expr) == 1:
        return expr
    if expr.startswith('NOT'):
        dentro = evaluar(expr[4:-1]) # Do quarto index ate o ultimo sem contar com o ultimo
        if dentro == 'F':
            return 'T'
        else:
            return 'F'
    a1, a2 = get_arguments(expr)
    a1 = evaluar(a1)
    a2 = evaluar(a2)
    if expr.startswith('AND'):
        if a1 == 'T' and a2 == 'T':
            return 'T'
        else:
            return 'F'
    if expr.startswith('OR'):
        if a1 == 'T' or a2 == 'T':
            return 'T'
        else:
            return 'F'
 
for _ in range(int(input())):
    print(evaluar(input().replace(' ', ''))) 
