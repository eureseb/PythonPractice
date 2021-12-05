def likes(names):
    
    if not names: return "no one likes this"
    name_length = len(names)
    
    if(name_length == 1): return f"{names[0]} likes this"
    elif(name_length == 2): return f"{names[0]} and {names[1]} like this"
    elif(name_length == 3): return f"{names[0]}" + ", " + f"{names[1]} and {names[2]} like this"
    else: return f"{names[0]}" + ", " + f"{names[1]} and {name_length-2} others like this"
