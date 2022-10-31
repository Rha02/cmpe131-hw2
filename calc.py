import collections


def calculator(query: str):
    n, iter = 0, 0
    stack = collections.deque()
    operation = "+"

    # helper method to update stack to reduce repeated code
    def updateStack(val):
        if operation == "+":
            stack.append(val)
        elif operation == "-":
            stack.append(-1 * val)
        elif operation == "*":
            stack.append(stack.pop()*val)
        elif operation == "/":
            stack.append(stack.pop()/val)
        

    while iter < len(query):
        # if ASCII value is between '0' and '9' inclusive, then it is a digit
        if ord(query[iter]) >= ord('0') and ord(query[iter]) <= ord('9'):
            n = n*10 + int(query[iter])
        elif query[iter] == "(":
            # use recursion to compute subproblem inside parantheses
            pair = calculator(query[iter+1:])
            n = pair[0]
            iter += pair[1]
        elif query[iter] == ")":
            updateStack(n)
            # return the calculated value inside parantheses along with the index of closing parantheses
            return [sum(stack), iter+1]
        elif query[iter] in "+-*/":
            updateStack(n)
            n, operation = 0, query[iter]
        iter += 1
    
    updateStack(n)
    return sum(stack)

            
