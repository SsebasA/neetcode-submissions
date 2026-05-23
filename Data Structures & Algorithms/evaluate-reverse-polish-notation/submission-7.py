class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        for token in tokens:
            if token == '+':
                if len(stack) > 0:
                    first_num = int(stack.pop())
                    secn_num = int(stack.pop())
                    res = first_num + secn_num
                    stack.append(res)
            elif token == '-':
                if len(stack) > 0:
                    first_num = int(stack.pop())
                    secn_num = int(stack.pop())
                    res = secn_num - first_num
                    stack.append(res)
            elif token == '*':
                if len(stack) > 0:
                    first_num = int(stack.pop())
                    secn_num = int(stack.pop())
                    res = first_num * secn_num
                    stack.append(res)
            elif token == '/':
                if len(stack) > 0:
                    first_num = int(stack.pop())
                    secn_num = int(stack.pop())
                    res = int(secn_num / first_num)
                    stack.append(res)
            else:
                stack.append(token)
        
        if len(stack) > 0:
            return stack.pop()
        else:
            return 0



