'''
@Author: Shubham shirke
@Date: 2023-06-21 14:02:30
@Last Modified by: Shubham shirke
@Last Modified time: 2023-06-21 14:02:30
@Title : Implement a stack to convert a infix expression to postfix expression.
'''

from stack_log import logger

class StackOperations:
    def __init__(self,expression) -> None:
        self.Operators= set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators
        self.Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
        self.expression = expression

    def infix_to_postfix(self):
        """
        Description : 
                This function converts infix expression to postfix expression.
        Parameters  :
                self : get operators , priority and expression from constructor.
        Returns     :
                output : postfix expression output
        """
        try:
            stack = []
            output = ''

            for character in self.expression:
                if character not in self.Operators:
                    output += character
                
                elif character=='(':
                    stack.append('(')

                elif character == ')':
                    while stack and stack[-1] !='(':
                        output +=stack.pop()
                    stack.pop()
                else:
                    while stack and stack[-1]!='(' and self.Priority[character]<=self.Priority[stack[-1]]:
                        output+=stack.pop()
                    stack.append(character)

            while stack:

                output+=stack.pop()

            return output
        except Exception as e:
            logger.error(f"{str(e)}")



def main():
    logger.info("Infix to Postfix program started")
    expression = "a+b*(c+d)-e/f"
    stack = StackOperations(expression)
    output = stack.infix_to_postfix()
    print(f"The postfix expression is: {output}")
    logger.info("Infix to Postfix program finished")


if __name__ == "__main__":
    main()