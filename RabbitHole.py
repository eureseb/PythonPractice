import random as rand
def step(pos):
    if(rand.uniform(0, 1) > .5):
        new_pos = pos+1
    else:
        new_pos = pos-1
             
    return new_pos
pos = 1#rand.randint(1,3)
guess = input("enter: ")
while True:
    print(pos)
    guess = input()
    step(pos)
    
            
# print("Hello")
# pos = step(pos)
# print(pos)