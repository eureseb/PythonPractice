import math
# def bouncing_ball(h, bounce, window):
#     if (h<=0):
#         return -1
#     if(bounce<=0 or bounce >= 1):
#         return -1
#     if(window >= h):
#         return -1
    
#     #Assume it passes through window while falling down before bouncing
#     result = 1
#     new_height = h*bounce
    
#     #Everytime it bounces and new height is greater than window, you can see it going and down (result+=2)
#     while(new_height > window):
#         new_height = new_height * bounce
#         result += 2
        

#     return result

''' 
Logarithmic approach
'''
def bouncing_ball(h, bounce, window):
    #For the ball to pass the window height must be greater than 0,
    #bounce coef greater then 0 and less than 1,
    #height of the window must be less than orginal height
    if not(h>0 and 0<bounce<1 and window < h):
        return -1    
    
    '''Another Verision using floored_num'''
    # num_past_window = math.log(window/h, bounce)
    # floored_num = int(num_past_window)
    # incase after than nth bounce it lands equal to window height
    # if num_past_window == floored_num:
    #     return num_past_window
    # else:
    #     return floored_num*2 +1
    
    #Bounce as base and window/h as numberic value
    num_past_window = math.ceil(math.log(window/h, bounce)) - 1 
    return num_past_window * 2 + 1
    
    
    
    
params = (30, 0.75, 1.5)
print(bouncing_ball(params[0], params[1], params[2]))