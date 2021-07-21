"""
@author: Nabeel Raza
"""

class Solution:
    def __init__(self, expression):
        """
        Constructor
        """
        self.expression = expression
        self.value_stack = []
        self.op_stack = []
        self._allowed_operators = ["+", "-", "/", "*", "^"]
        self.processed = self.preprocess()
        

    def preprocess(self):
        processed = []
        word = ""
        start_num = False
        for i in range(len(self.expression)):
            if self.expression[i] == "-" and word != "":
                processed.append(float(word))
                processed.append("-")
                start_num = False
                word = ""
                continue
            if self.expression[i] == "x" or self.expression[i] == "X":
                processed.append("x")
            elif self.expression[i] == " ":
                if word != "":
                    processed.append(float(word))
                start_num = False
                word = ""
            elif self.expression[i].isnumeric() or self.expression[i] == "." or self.expression[i] == "-":
                if (len(processed) != 0 and processed[-1] != "(" and processed[-1] != "/" and processed[-1] != "+" and processed[-1] != "*" and processed[-1] != "^") and self.expression[i] == '-':
                   
                    processed.append("+")
                start_num = True
                word += self.expression[i]
            else:
                if word != "":
                    processed.append(float(word))
                start_num = False
                word = ""
            if self.expression[i] in ['+', '*', '/', '^', '(', ')']:
                processed.append(self.expression[i])
        if word != "":
            processed.append(float(word))
        return processed


    def _solve_atomic_expression(self):
        """
        Solves an atomic expression!
        Atomic expression: The one that cannot be subdivided!
        """
        op = self.op_stack.pop()
        operand1 = self.value_stack.pop()
        operand2 = self.value_stack.pop()
        self._apply_operation(op, operand1, operand2)

    def _apply_operation(self, op, operand1, operand2):
        """
        Applies the operator op on the operands (1 and 2)
        It also pushes the result on the value stack.
        """
        if op == "+":
            result = operand2 + operand1
        elif op == "^":
            result = operand2**operand1
        elif op == "-":
            result = operand2 - operand1
        elif op == "*":
            result = operand2 * operand1
        elif op == "/":
            if operand2 == "0":
                raise ZeroDivisionError ("Cannot divide by zero!")
            else:
                result = operand2 / operand1
        self.value_stack.append(result)

    def _is_operator(self, op):
        return op in self._allowed_operators

    def _precedence(self, op):
        if op == "^":
            return 3
        if op == "/" or op == "*":
            return 2
        if op == "+" or op == "-":
            return 1
        return 0

    def solve(self):
        """
        Solves the expression passed in.
        """
        for ch in self.processed:
            if type(ch) == float:
                self.value_stack.append(ch)
            if ch =="(":
                self.op_stack.append(ch)
            if ch == ")":
                while self.op_stack[-1] != "(":
                    self._solve_atomic_expression()
                self.op_stack.pop() # only left paranthesis would be left at this point.
            if self._is_operator(ch):
                while len(self.op_stack) != 0 and self._precedence(self.op_stack[-1]) >= self._precedence(ch):
                    self._solve_atomic_expression()
                self.op_stack.append(ch)
        while len(self.op_stack) != 0:
            self._solve_atomic_expression()
        return self.value_stack.pop()


if __name__ == "__main__":
    string = "6-14"
    plot = []
    import numpy as np
    for i in range(-500, 500+1):
        s = Solution(string.replace("x", "(" + str(i) + ")"))
        try:
            temp = np.float32(s.solve())
            plot.append(temp)
        except ZeroDivisionError:
            plot.append(np.nan)
    print(plot)
