
import  random
def random_number(any_positive_number):
    alfa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = '0123456789'
    x = 0
    code_list = []
    while x <= any_positive_number:
        x = x + 1
        y = random.randint(1 , 2)
        
        if y == 1:
            z = random.randint(0 , 25)
            g = alfa[z]
            code_list.append(g)
        else:
            z = random.randint(0 , 9)
            g = nums[z]
            code_list.append(g)
    code = '#'
    for u in range(len(code_list) - 1):
        code = code + str(code_list[u])
    return code
