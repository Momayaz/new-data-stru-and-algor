def multi_bracket(input):
    """
    function to cheack if we have any extra  or missing Bracket or parenthesis or curly braces 
     
    """
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
    stack = []
    for y in input:
        if y in open_list:
            stack.append(y)
            
        elif y in close_list:
            index_position = close_list.index(y)
            if ((len(stack) > 0) and (open_list[index_position] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
if __name__ == "__main__":
    pass
