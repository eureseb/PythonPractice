def get_sum(a,b):
    res = 0
    l = min(a,b)
    h = max(a,b)
    if a == b:
        return a
    else:
        for i in range(l,h+1):
            res += i
            print(i)
    return res

a = -1
b = 0
print(get_sum(a,b))