class Solution:
    def evaluatePostfix(self, arr):
        stack = []

        for token in arr:
            if token not in {"+", "-", "*", "/", "^"}:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = left // right
            else:  # ^
                result = left ** right

            stack.append(result)

        return stack[-1]