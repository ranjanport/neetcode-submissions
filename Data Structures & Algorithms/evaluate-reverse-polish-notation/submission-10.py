class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        k = int(tokens[0])
        temp_list = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                b = temp_list.pop()
                a = temp_list.pop()
                if token == '+':
                    k = a + b
                elif token == '-':
                    k = a - b
                elif token == '*':
                    k = a * b
                elif token == '/':
                    if b != 0:
                        k = a / b
                        k = int(k)
                    else:
                        k = 0
                temp_list.append(k)
            else:
                temp_list.append(int(token))
        return k