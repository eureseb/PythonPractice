# def productFib(prod):
#     fib = [0,1]
#     i = 2
#     #edge cases
#     if prod==0:
#         return [0,1, True]
#     elif prod==1:
#         return [1,1, True]
    
#     while(True):
#         fib.append(fib[i-1] + fib[i-2])
#         i += 1
#         res = fib[i-1]*fib[i-2]
#         if(res == prod):
#             return [fib[i-2],fib[i-1], True]
#         elif res > prod:
#             return [fib[i-2],fib[i-1], False]

def productFib(prod):
    a,b = 0,1
    while(prod > a*b):
        a, b = b, a+b
    return [a, b, a*b == prod]    
    
prod = 715
print(productFib(prod))