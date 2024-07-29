def test_brackets(inp_str):
    stack = []
    op_brack = set("({[")
    cl_brack = set(")}]")
    matches = {")": "(", "}": "{", "]": "["}
    
    for char in inp_str:
        if char in op_brack:
            stack.append(char)
        elif char in cl_brack:
            if not stack or stack[-1] != matches[char]:
                return "Несиметрично"
            stack.pop()
    
    return "Симетрично" if not stack else "Несиметрично"

# Приклади для перевірки програми
inp_str = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for s in inp_str:
    print(f"{s}: {test_brackets(s)}")