# 1 <= tokens.length <= 10^4
# tokens[i] is either valid (+, -, *, /) or int between [-200, 200]
# The input represents a valid arithmetic expression in a reverse polish notation.

#Beast mode solution, 3ms, clean and easier to understand
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:                #  Ex:  tokens = ["4","13","5","/","+"]
        stack = []
                                                                #      t     operation    stack
        for t in tokens:                                        #    –––––   –––––––––    ––––––––– 
            if t not in '/+-*':                                 #      4                    [4]
                stack.append(int(t))                            #     13                    [4,13]
                                                                #      5                    [4,13,5]
            else:                                               #      /     13 / 5 = 2     [4,2]
                num = stack.pop()                               #      +      4 + 2 = 6     [6]
                if   t == '+': stack[-1]+=  num
                elif t == '-': stack[-1]-=  num
                elif t == '*': stack[-1]*=  num
                else         : stack[-1]= int(stack[-1]/num)    

        return stack[0]


#Initial solution, verbose, 10ms but logic is correct
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        polish = []
        for i in tokens:
            eval = 0
            if i.lstrip('-').isdigit():
                polish.append(int(i))
                print(f"Pushed: {i}")
            else:
                digit1 = polish.pop()
                digit2 = polish.pop()
                match (i):
                    case '+':
                        eval = digit2 + digit1
                        polish.append(eval)
                    case '-':
                        eval = digit2 - digit1
                        polish.append(eval)
                    case '*':
                        eval = digit2 * digit1
                        polish.append(eval)
                    case '/':
                        eval = int(digit2/digit1)
                        polish.append(eval)
                print("Last digit: ", polish[-1])
                
        return polish.pop()