# def disemvowel(string):
#     vowels = ['a','e','i','o','u']
#     result = []
#     # result = [letter for letter in string if letter.lower() not in vowels]
#     for letter in string:
#         if letter.lower() not in vowels:
#             result.append(letter)
#     result = ''.join(result)
#     return result

def disemvowel(string):
    return ''.join(letter for letter in string if letter not in "aeiouAEIOU")
    
    

str = "This website is for losers LOL!"
print(disemvowel(str))