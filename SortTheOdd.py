# def sort_array(source_array):
#     res = source_array.copy()
#     res_len = len(res)
#     if not res:
#         return res
#     min = res[0]
#     for i in range(res_len):
#         if(res[i]%2 == 1):
#             for j in range(res_len):
#                 if (res[j]%2): 
#                     if(res[i] < res[j]):
#                         min = res[i];
#                         res[i] = res[j];
#                         res[j] = min; 
#                 else: 
#                     continue
#     return res
#     # Return a sorted array.
    
def sort_array(source_array):
    #For every odd number in source array, put append into result in ascending order
    result = sorted([l for l in source_array if l % 2 == 1]) # if spec is descending order, ", reverse=True" can be added 
    #Iterated over the source array
    for index, item in enumerate(source_array):
        #If currect number is even, insert into result list with its corresponding index
        if item % 2 == 0:
            result.insert(index, item)
    #Return result list
    return result

arr = [5, 3, 2, 8, 1, 4]
print(sort_array(arr))