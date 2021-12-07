# def high_and_low(numbers):
#     res = []
#     for t in numbers.split():
#         try:
#             res.append(int(t))
#         except ValueError:
#             pass
#     return "{} {}".format(max(res), min(res))   

# def high_and_low(numbers):
#     res = [ int(s) for s in numbers.split(' ')]
#     return "{} {}".format(max(res), min(res))  

def high_and_low(numbers):
    res = sorted(numbers.split(), key=int)
    return "{} {}".format(res[-1], res[0])  

param = ("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
print(high_and_low(param))