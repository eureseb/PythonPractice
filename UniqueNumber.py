def find_uniq(arr):
    # your code here
    value = []
    value.append(arr[0])
    if(arr[1] == arr[2] and arr[0] != arr[1]):
        return arr[0]
    for i in range(len(arr)):
        if arr[i] not in value:
            if i > 2:
                return arr[i]
            if arr[i+1] == arr[i] and i > 1:
                return value[0]
            else:
                return arr[i]
    # n: unique integer in the array
    
arr = [ 1, 1, 1, 2, 1, 1 ]
print(find_uniq(arr ))   