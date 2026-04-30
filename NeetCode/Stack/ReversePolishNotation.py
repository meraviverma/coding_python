# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
#
# Return the integer that represents the evaluation of the expression.
#
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:
#
# Input: tokens = ["1","2","+","3","*","4","-"]
#
# Output: 5
#
# Explanation: ((1 + 2) * 3) - 4 = 5

#You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

from typing import List
# Import List type hint from typing module
from typing import List


# Define a class named solution
class solution():
    # Method to evaluate Reverse Polish Notation (RPN) expressions
    def evalRPN(self, token: List[str]) -> int:
        stack = []  # Initialize an empty stack to store operands

        # Iterate through each token in the input list
        for c in token:
            if c == "+":
                # If token is '+', pop two elements and add them
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # If token is '-', pop two elements (order matters)
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # If token is '*', pop two elements and multiply them
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                # If token is '/', pop two elements (order matters)
                a, b = stack.pop(), stack.pop()
                # Perform integer division (truncate toward zero)
                stack.append(int(b / a))
            else:
                # If token is a number, convert to int and push onto stack
                stack.append(int(c))

        # Final result will be the only element left in the stack
        return stack[0]


# Driver code to test the solution
if __name__ == "__main__":
    obj = solution()
    tokens = ["1", "2", "+", "3", "*", "4", "-"]  # Example RPN expression
    print(obj.evalRPN(tokens))  # Expected output: 5



