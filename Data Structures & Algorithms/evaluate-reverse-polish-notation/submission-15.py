class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        values = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                values.append(int(token))
                continue

            b = values.pop()
            a = values.pop()

            if token == '-':
                res = a-b
            elif token == '+':
                res = a+b
            elif token == '*':
                res = a*b
            else:
                res = abs(a)// abs(b)
                if (a<0) != (b<0):
                    res =-res
        
            values.append(res)

        return values[-1]
